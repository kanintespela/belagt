#!/usr/bin/env python3
"""Kontrollera att varje citat fortfarande står i sin källa, och att länkarna fungerar.

    python tools/kontrollera_citat.py              # alla poster
    python tools/kontrollera_citat.py ISR-01 KIN-09 # bara vissa poster
    python tools/kontrollera_citat.py --fil sida.html --citat "…"  # pröva ett citat mot en sparad fil

Källtexten hämtas helst från arkivkopian (källa.arkiv), eftersom det är den som ska gå att
kontrollera i efterhand, och annars från källa.url. Citatet söks i texten efter att båda har
normaliserats (blanksteg, citattecken, bindestreck, versaler). Ett utelämnande (…) i citatet
betyder att delarna före och efter ska finnas i den ordningen.

Skriver markdown till stdout, eller ingenting om allt stämmer. Körs varje månad av
.github/workflows/citat.yml, som lägger rapporten i ett ärende. Kontrollen kan köras av vem som
helst, så att ingen behöver lita på att citaten kontrollerades när posten skrevs.
"""
import argparse
import html.parser
import io
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/kanintespela/belagt/blob/main/"
UA = {"User-Agent": "Mozilla/5.0 (compatible; belagt-citatkontroll; +https://github.com/kanintespela/belagt)"}
CJK_RE = re.compile(r"[぀-ヿ㐀-鿿가-힯]")
UTELÄMNANDE_RE = re.compile(r"\s*(?:\[…\]|\[\.\.\.\]|…|\.\.\.)\s*")
WAYBACK_RE = re.compile(r"^(https://web\.archive\.org/web/\d+)(/)")

TECKEN = str.maketrans({
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'", "`": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"', "«": '"', "»": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "―": "-", "−": "-",
    "­": None, "​": None, "‌": None, "‍": None, "﻿": None,
})


class Text(html.parser.HTMLParser):
    """Plockar ut den synliga texten ur en HTML-sida."""
    HOPPA = {"script", "style", "noscript", "template", "svg"}
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "td", "th", "section",
             "article", "blockquote", "header", "footer", "figcaption"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.delar, self.djup = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.HOPPA:
            self.djup += 1
        elif tag in self.BLOCK:
            self.delar.append("\n")

    def handle_endtag(self, tag):
        if tag in self.HOPPA and self.djup:
            self.djup -= 1
        elif tag in self.BLOCK:
            self.delar.append("\n")

    def handle_data(self, data):
        if not self.djup:
            self.delar.append(data)


def html_text(rå):
    t = Text()
    t.feed(rå)
    return "".join(t.delar)


def pdf_text(data):
    from pypdf import PdfReader  # bara här, så att resten av verktygen klarar sig utan
    return "\n".join((sida.extract_text() or "") for sida in PdfReader(io.BytesIO(data)).pages)


def normalisera(s, cjk=False):
    s = unicodedata.normalize("NFKC", s).translate(TECKEN).lower()
    # Avstavning vid radbrytning i PDF: "kontroll-\nerad" -> "kontrollerad".
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)
    if cjk:
        return re.sub(r"\s+", "", s)
    s = re.sub(r"\s+", " ", s)
    # Mellanslag före skiljetecken varierar mellan sidor och PDF-utdrag.
    return re.sub(r" ([,.;:!?)\]'\"])", r"\1", s).strip()


def finns(citat, text):
    """True om citatet (med eventuella utelämnanden) står i texten, i rätt ordning."""
    cjk = bool(CJK_RE.search(citat))
    text = normalisera(text, cjk)
    pos = 0
    for del_ in UTELÄMNANDE_RE.split(citat):
        del_ = normalisera(del_, cjk).strip(" .,;:")
        if not del_:
            continue
        i = text.find(del_, pos)
        if i < 0:
            return False
        pos = i + len(del_)
    return True


def rå_arkivlänk(arkiv):
    """Wayback Machine visar sidan med en egen meny runt. Med id_ efter tidsstämpeln fås originalet."""
    return WAYBACK_RE.sub(r"\1id_\2", arkiv) if arkiv else arkiv


def hämta(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data, typ = r.read(), r.headers.get("Content-Type", "")
    if "pdf" in typ or data[:5] == b"%PDF-":
        return pdf_text(data)
    tecken = re.search(r"charset=([\w-]+)", typ)
    return html_text(data.decode(tecken[1] if tecken else "utf-8", "replace"))


def ladda(ids):
    poster = [yaml.safe_load(f.read_text()) for f in sorted((ROOT / "påståenden").glob("*/*.yaml"))]
    return [p for p in poster if not ids or p["id"] in ids]


def länk(p):
    return f"[{p['id']}]({REPO}påståenden/{p['datum'][:4]}/{p['id']}.yaml)"


def kontrollera(poster, paus=2):
    """Returnerar {"saknas": [...], "död": [...], "ohämtbar": [...]} med (post, förklaring)."""
    utfall = defaultdict(list)
    per_källa = defaultdict(list)
    for p in poster:
        per_källa[(p["källa"]["url"], p["källa"]["arkiv"])].append(p)
    for (url, arkiv), grupp in per_källa.items():
        text, varifrån, fel = None, None, []
        for försök, kandidat in (("arkivkopian", rå_arkivlänk(arkiv)), ("källan", url)):
            if not kandidat:
                continue
            try:
                text, varifrån = hämta(kandidat), försök
                break
            except urllib.error.HTTPError as e:
                fel.append((försök, e.code))
            except Exception as e:  # nätverksfel, tidsgräns, trasig PDF
                fel.append((försök, type(e).__name__))
            time.sleep(paus)
        död = [kod for försök, kod in fel if försök == "källan" and kod in (404, 410)]
        if död:
            for p in grupp:
                utfall["död"].append((p, f"källan svarar {död[0]}" + (", arkivkopian används" if text else "")))
        if text is None:
            if not död:
                for p in grupp:
                    utfall["ohämtbar"].append((p, ", ".join(f"{f}: {k}" for f, k in fel)))
            continue
        for p in grupp:
            if not finns(p["källa"]["citat"], text):
                utfall["saknas"].append((p, f"söktes i {varifrån}"))
        time.sleep(paus)
    return utfall


RUBRIKER = {
    "saknas": ("Citatet hittades inte i källan",
               "Antingen har källan ändrats, eller så är citatet inte ordagrant. Kontrollera för hand. "
               "Står citatet kvar men på ett sätt kontrollen inte känner igen, går det bra att lämna det."),
    "död": ("Döda länkar",
            "Källan finns inte kvar på sin adress. Finns det en arkivkopia gäller citatet fortfarande, "
            "men leta gärna upp den nya adressen."),
    "ohämtbar": ("Gick inte att hämta",
                 "Sidan blockerar automatiska hämtningar, kräver JavaScript eller svarade inte. Det betyder "
                 "inte att något är fel, men citatet har inte kunnat kontrolleras den här gången."),
}


def rapport(utfall, antal):
    if not any(utfall.values()):
        return ""
    ut = [f"Kontrollen gick igenom {antal} poster. "
          f"Citatet hittades inte i {len(utfall['saknas'])}, {len(utfall['död'])} har döda länkar och "
          f"{len(utfall['ohämtbar'])} gick inte att hämta.\n"]
    for nyckel, (rubrik, förklaring) in RUBRIKER.items():
        if utfall[nyckel]:
            ut.append(f"\n## {rubrik}\n\n{förklaring}\n\n")
            ut += [f"- [ ] **{länk(p)}** ({orsak}): {p['källa']['url']}\n" for p, orsak in utfall[nyckel]]
    return "".join(ut)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", nargs="*")
    ap.add_argument("--fil", help="pröva ett citat mot en sparad HTML-, text- eller PDF-fil")
    ap.add_argument("--citat")
    ap.add_argument("--paus", type=float, default=2)
    a = ap.parse_args()
    if a.fil:
        data = Path(a.fil).read_bytes()
        text = pdf_text(data) if data[:5] == b"%PDF-" else html_text(data.decode("utf-8", "replace"))
        ok = finns(a.citat, text)
        print("Citatet finns i filen." if ok else "Citatet finns inte i filen.")
        sys.exit(0 if ok else 1)
    poster = ladda(set(a.id))
    print(rapport(kontrollera(poster, a.paus), len(poster)), end="")


if __name__ == "__main__":
    main()
