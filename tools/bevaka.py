#!/usr/bin/env python3
"""Lista det som är nytt i de bevakade källorna (bevakning.yaml).

    python tools/bevaka.py              # det som publicerats de senaste 8 dagarna
    python tools/bevaka.py --dagar 30

Skriver markdown till stdout, eller ingenting om inget är nytt. Länkar som redan är källor i
arkivet hoppas över. Körs varje vecka av .github/workflows/bevaka.yml, som lägger listan i ett
ärende. Det som listas är tips: en post skrivs bara när primärkällan har hämtats och ett ordagrant
citat bekräftar påståendet.
"""
import argparse
import datetime
import email.utils
import gzip
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (compatible; belagt-bevakning; +https://github.com/kanintespela/belagt)"}
ATOM = "{http://www.w3.org/2005/Atom}"
MAX_PER_KÄLLA = 5
# Källor med kräv_ai: true tar bara med poster där något av orden står i titeln.
AI_ORD = re.compile(r"\b(AI|KI|A\.I\.|AGI)\b|artificiell intelligens|artificial intelligence|kunstig intelligens"
                    r"|maskininlärning|machine learning|språkmodell|language model|chatbot|chattbot|generativ",
                    re.IGNORECASE)
# Sajter som aldrig kan vara källa enligt METOD.md (avsnittet Vilka avsändare som kan vara källa):
# maskinöversatta eller troligen automatgenererade sajter, återpublicering av andras texter och
# tjänster för betalda pressmeddelanden.
BLOCKERADE = {
    # maskinöversatt, automatgenererat eller utan identifierbar redaktion
    "vietnam.vn", "news55.se", "news.lavx.hu", "streamlinefeed.co.ke", "powersofafrica.com", "inyheter.no",
    # återpublicerar andras texter, gå till originalet
    "tradingview.com",
    # kryptonyheter och fackpress inom reklam och tv
    "tokenpost.com", "adgully.com", "indiantelevision.com",
    # betalda pressmeddelanden
    "markets.businessinsider.com", "prnewswire.com", "globenewswire.com", "businesswire.com",
    "einpresswire.com", "openpr.com", "accessnewswire.com", "newsfilecorp.com",
}
# Riksdagsdokument som kan bära ett påstående. Protokoll, dagordningar och EU-dokument hoppas över.
RIKSDAGSTYPER = {"mot", "ip", "fr", "frs", "prop", "sou", "ds", "dir", "bet", "skr", "rir"}
MAX_TECKEN = 60000  # GitHub tar högst 65 536 tecken i ett ärende


def hämta(url, timeout=60, försök=2):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except (urllib.error.URLError, TimeoutError) as e:
        # Tillfälliga fel (till exempel 503 från news.google.com) får ett nytt försök.
        if försök <= 1 or (isinstance(e, urllib.error.HTTPError) and e.code < 500):
            raise
        time.sleep(10)
        return hämta(url, timeout, försök - 1)
    # deepmind.google skickar gzip även när ingen har bett om det
    return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data


def datum(s):
    """Tolka datum i RSS (RFC 822), Atom (ISO 8601) och riksdagens format (ÅÅÅÅ-MM-DD)."""
    if not s:
        return None
    s = s.strip()
    try:
        return email.utils.parsedate_to_datetime(s).date()
    except (TypeError, ValueError, IndexError):
        pass
    try:
        return datetime.date.fromisoformat(s[:10])
    except ValueError:
        return None


def text(el, *namn):
    for n in namn:
        hit = el.find(n)
        if hit is not None and (hit.text or "").strip():
            return " ".join(hit.text.split())
    return ""


def blockerad(url):
    värd = urllib.parse.urlparse(url or "").hostname or ""
    return any(värd == b or värd.endswith("." + b) for b in BLOCKERADE)


def läs_flöde(data, kategorier=None):
    """Poster ur ett RSS- eller Atom-flöde som (titel, länk, datum).

    Med kategorier tas bara RSS-poster med någon av de kategorierna med."""
    rot = ET.fromstring(data)
    for item in rot.iter("item"):  # RSS
        källa = item.find("source")  # Google News anger den egentliga sajten här
        if källa is not None and blockerad(källa.get("url")):
            continue
        if kategorier and not {c.text for c in item.findall("category")} & set(kategorier):
            continue
        yield text(item, "title"), text(item, "link"), datum(text(item, "pubDate", "{http://purl.org/dc/elements/1.1/}date"))
    for entry in rot.iter(f"{ATOM}entry"):  # Atom
        länk = next((l.get("href") for l in entry.findall(f"{ATOM}link") if l.get("rel") in (None, "alternate")), "")
        yield text(entry, f"{ATOM}title"), länk, datum(text(entry, f"{ATOM}published", f"{ATOM}updated"))


def läs_riksdagen(data):
    lista = json.loads(data).get("dokumentlista", {}).get("dokument") or []
    for d in lista:
        if d.get("typ") not in RIKSDAGSTYPER:
            continue
        titel = " – ".join(x for x in (d.get("titel"), d.get("undertitel")) if x)
        länk = d.get("dokument_url_html") or ""
        if länk.startswith("//"):
            länk = "https:" + länk
        yield f"{d.get('typ', '').upper()}: {titel}", länk, datum(d.get("datum"))


def befintliga():
    return {yaml.safe_load(f.read_text())["källa"]["url"] for f in (ROOT / "påståenden").glob("*/*.yaml")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dagar", type=int, default=8)
    ap.add_argument("--idag", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    gräns = datetime.date.fromisoformat(a.idag) - datetime.timedelta(days=a.dagar)
    källor = yaml.safe_load((ROOT / "bevakning.yaml").read_text())
    kända, sedda = befintliga(), set()
    per_grupp, trasiga = defaultdict(list), []
    for k in källor:
        try:
            data = hämta(k["url"])
            if k.get("format") == "riksdagen":
                poster = list(läs_riksdagen(data))
            else:
                poster = list(läs_flöde(data, k.get("kategorier")))
        except Exception as e:  # nätverksfel, flytt eller ändrat format: syns i ärendet
            trasiga.append(f"- {k['namn']}: {type(e).__name__}: {e} ({k['url']})")
            continue
        nya = [(t, l, d) for t, l, d in poster
               if t and l and l not in kända and l not in sedda and (d is None or d >= gräns)
               and not blockerad(l) and (not k.get("kräv_ai") or AI_ORD.search(t))
               and (not k.get("kräv_ord") or re.search(rf"\b({k['kräv_ord']})", t, re.IGNORECASE))]
        nya.sort(key=lambda x: x[2] or datetime.date.min, reverse=True)
        if nya:
            per_grupp[k["grupp"]].append((k, nya))
        sedda.update(l for _, l, _ in nya)
    if not per_grupp and not trasiga:
        return
    # Färre tips per källa tills ärendet ryms, så att alla källor syns.
    for högst in range(MAX_PER_KÄLLA, 0, -1):
        text_ut = rapport(gräns, per_grupp, trasiga, högst)
        if len(text_ut) <= MAX_TECKEN:
            break
    print(text_ut[:MAX_TECKEN], end="")


def rapport(gräns, per_grupp, trasiga, högst):
    utelämnade = sum(max(len(nya) - högst, 0) for rader in per_grupp.values() for _, nya in rader)
    ut = [f"Nytt i de bevakade källorna sedan {gräns}. Det här är tips: följ länken till primärkällan, "
          "hämta den och skriv en post bara om ett ordagrant citat bekräftar påståendet "
          "([METOD.md](https://github.com/kanintespela/belagt/blob/main/METOD.md)). Listan över källor finns i "
          "[bevakning.yaml](https://github.com/kanintespela/belagt/blob/main/bevakning.yaml).\n"]
    if utelämnade:
        ut.append(f"\nÄrendet rymmer högst {högst} tips per källa, så {utelämnade} äldre tips är utelämnade.\n")
    for grupp, rader in per_grupp.items():
        ut.append(f"\n## {grupp}\n")
        for k, nya in rader:
            ut.append(f"\n**{k['namn']}**\n\n")
            ut += [f"- [ ] {d or 'okänt datum'}: [{t}]({l})\n" for t, l, d in nya[:högst]]
    if trasiga:
        ut.append("\n## Flöden som inte gick att läsa\n\nAdressen kan ha ändrats. Rätta den i bevakning.yaml.\n\n")
        ut.append("\n".join(trasiga) + "\n")
    return "".join(ut)


if __name__ == "__main__":
    main()
