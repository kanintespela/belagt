#!/usr/bin/env python3
"""Lista poster som har passerat bäst_före, eller som gör det inom kort.

    python tools/bast_fore.py              # passerade och de som går ut inom 31 dagar
    python tools/bast_fore.py --dagar 0    # bara passerade

Skriver markdown till stdout, eller ingenting om ingen post behöver kontrolleras.
Körs varje månad av .github/workflows/bast-fore.yml, som lägger listan i ett ärende.
Poster med ersatt_av är redan hanterade och tas inte med.
"""
import argparse
import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/kanintespela/belagt/blob/main/"


def rad(p):
    f = f"påståenden/{p['datum'][:4]}/{p['id']}.yaml"
    return (f"- [ ] **[{p['id']}]({REPO}{f})** (bäst före {p['bäst_före']}): {p['påstående']}  \n"
            f"  Källa: {p['källa']['url']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dagar", type=int, default=31)
    ap.add_argument("--idag", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    gräns = (datetime.date.fromisoformat(a.idag) + datetime.timedelta(days=a.dagar)).isoformat()

    poster = [yaml.safe_load(f.read_text()) for f in sorted((ROOT / "påståenden").glob("*/*.yaml"))]
    aktuella = sorted((p for p in poster if p["bäst_före"] and not p["ersatt_av"]
                       and p["bäst_före"] <= gräns), key=lambda p: (p["bäst_före"], p["id"]))
    passerade = [p for p in aktuella if p["bäst_före"] <= a.idag]
    snart = [p for p in aktuella if p["bäst_före"] > a.idag]
    if not aktuella:
        return

    ut = [f"Genererat {a.idag} av `tools/bast_fore.py`. Uppdateras varje månad.\n",
          "Kontrollera varje post mot källan. Sedan finns tre utfall:\n",
          "1. **Stämmer fortfarande:** sätt `kontrollerad` till dagens datum och flytta fram `bäst_före`.",
          "2. **Har ändrats:** lägg till en ny post med det nya läget och sätt `ersatt_av` på den gamla.",
          "3. **Går inte att kontrollera längre** (källan borta): använd `källa.arkiv`, "
          "och skriv i förbehållet att originalet är borta.\n"]
    if passerade:
        ut += [f"## Passerat bäst före ({len(passerade)})\n", *map(rad, passerade), ""]
    if snart:
        ut += [f"## Går ut inom {a.dagar} dagar ({len(snart)})\n", *map(rad, snart), ""]
    print("\n".join(ut))


if __name__ == "__main__":
    main()
