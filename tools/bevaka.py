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
import json
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (compatible; belagt-bevakning; +https://github.com/kanintespela/belagt)"}
ATOM = "{http://www.w3.org/2005/Atom}"
MAX_PER_KÄLLA = 15


def hämta(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


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


def läs_flöde(data):
    """Poster ur ett RSS- eller Atom-flöde som (titel, länk, datum)."""
    rot = ET.fromstring(data)
    for item in rot.iter("item"):  # RSS
        yield text(item, "title"), text(item, "link"), datum(text(item, "pubDate", "{http://purl.org/dc/elements/1.1/}date"))
    for entry in rot.iter(f"{ATOM}entry"):  # Atom
        länk = next((l.get("href") for l in entry.findall(f"{ATOM}link") if l.get("rel") in (None, "alternate")), "")
        yield text(entry, f"{ATOM}title"), länk, datum(text(entry, f"{ATOM}published", f"{ATOM}updated"))


def läs_riksdagen(data):
    lista = json.loads(data).get("dokumentlista", {}).get("dokument") or []
    for d in lista:
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
            poster = list((läs_riksdagen if k.get("format") == "riksdagen" else läs_flöde)(data))
        except Exception as e:  # nätverksfel, flytt eller ändrat format: syns i ärendet
            trasiga.append(f"- {k['namn']}: {type(e).__name__}: {e} ({k['url']})")
            continue
        nya = [(t, l, d) for t, l, d in poster
               if t and l and l not in kända and l not in sedda and (d is None or d >= gräns)]
        nya.sort(key=lambda x: x[2] or datetime.date.min, reverse=True)
        if nya:
            per_grupp[k["grupp"]].append((k, nya[:MAX_PER_KÄLLA]))
        sedda.update(l for _, l, _ in nya)
    if not per_grupp and not trasiga:
        return
    ut = [f"Nytt i de bevakade källorna sedan {gräns}. Det här är tips: följ länken till primärkällan, "
          "hämta den och skriv en post bara om ett ordagrant citat bekräftar påståendet "
          "([METOD.md](https://github.com/kanintespela/belagt/blob/main/METOD.md)). Listan över källor finns i "
          "[bevakning.yaml](https://github.com/kanintespela/belagt/blob/main/bevakning.yaml).\n"]
    for grupp, rader in per_grupp.items():
        ut.append(f"\n## {grupp}\n")
        for k, nya in rader:
            ut.append(f"\n**{k['namn']}**\n\n")
            ut += [f"- [ ] {d or 'okänt datum'}: [{t}]({l})\n" for t, l, d in nya]
    if trasiga:
        ut.append("\n## Flöden som inte gick att läsa\n\nAdressen kan ha ändrats. Rätta den i bevakning.yaml.\n\n")
        ut.append("\n".join(trasiga) + "\n")
    print("".join(ut), end="")


if __name__ == "__main__":
    main()
