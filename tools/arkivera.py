#!/usr/bin/env python3
"""Fyll i källa.arkiv med en arkivkopia i Wayback Machine för poster som saknar en.

    python tools/arkivera.py            # högst 20 källor per körning
    python tools/arkivera.py --max 50

Finns en kopia redan används den närmaste kopian från det datum källan hämtades. Annars
begärs en ny kopia. Körs varje vecka av .github/workflows/arkivera.yml.
"""
import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "belagt-arkivering (+https://github.com/kanintespela/belagt)"}


def hämta(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace"), r.geturl()


def befintlig(url, datum):
    tid = (datum or "").replace("-", "")
    q = urllib.parse.urlencode({"url": url, "timestamp": tid})
    text, _ = hämta(f"https://archive.org/wayback/available?{q}")
    snap = json.loads(text).get("archived_snapshots", {}).get("closest")
    return snap["url"].replace("http://", "https://", 1) if snap and snap.get("available") else None


def ny(url):
    _, slut = hämta(f"https://web.archive.org/save/{url}", timeout=180)
    return slut if "/web/" in slut else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=20)
    a = ap.parse_args()
    klara, cache = 0, {}
    for f in sorted((ROOT / "påståenden").glob("*/*.yaml")):
        text = f.read_text()
        p = yaml.safe_load(text)
        k = p["källa"]
        if k["arkiv"]:
            continue
        if k["url"] not in cache:
            if klara >= a.max:
                continue
            try:
                cache[k["url"]] = befintlig(k["url"], k["hämtad"]) or ny(k["url"])
            except Exception as e:  # nätverksfel, blockering eller hastighetsgräns: försök nästa vecka
                print(f"{p['id']}: {e}")
                cache[k["url"]] = None
            klara += 1
            time.sleep(5)
        if cache[k["url"]]:
            # Byt bara raden, så att resten av filen står orörd i diffen.
            f.write_text(text.replace("  arkiv: null\n", f"  arkiv: {cache[k['url']]}\n", 1))
            print(f"{p['id']}: {cache[k['url']]}")


if __name__ == "__main__":
    main()
