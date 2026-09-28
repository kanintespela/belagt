#!/usr/bin/env python3
"""Validera påståendena och bygg allt som genereras ur dem.

    python tools/bygg.py              # validera och skriv om genererade filer
    python tools/bygg.py --kontroll   # validera och kontrollera att genererade filer är aktuella (CI)

Källan är påståenden/<år>/<id>.yaml. Allt annat genereras och redigeras aldrig för hand:
    data/belagt.json, data/belagt.csv   hela arkivet som data
    tidslinje.md                        alla påståenden i datumordning
    teman/<tema>.md                     ett dokument per tema
    docs/belagt.json                    underlag för webbsidan i docs/
"""
import csv
import io
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PÅST = ROOT / "påståenden"
REPO_URL = "https://github.com/kanintespela/belagt"
SIDA_URL = "https://kanintespela.github.io/belagt/"

TYPER = {"händelse", "mätning", "bedömning", "prognos", "förslag"}
TEMAN = {
    "förmågor": "Vad AI-systemen kan göra och hur det mäts.",
    "tempo": "Hur snabbt utvecklingen går och varför: beräkningskraft, investeringar och skalning.",
    "självförbättring": "AI som används för att utveckla AI.",
    "kontroll": "Går systemen att styra, övervaka och testa? Alignment, tankekedjor och testmedvetenhet.",
    "missbruk": "Hur AI används för att skada: cyberangrepp, påverkan och biologiska risker.",
    "styrning": "Reglering, standarder, tillsyn och förslag om att bromsa eller pausa.",
    "geopolitik": "Kapplöpningen mellan länder, exportkontroller, USA och Kina.",
    "nytta": "Vad AI redan gör för sjukvård, forskning och samhälle.",
    "röster": "Vad forskare, insiders, politiker och andra bedömare säger.",
    "samhälle": "Hur AI påverkar arbete, ekonomi och vardag: jobb, beroende, AI-kompanjoner och kritiskt tänkande.",
}
FÄLT = ["id", "påstående", "typ", "vem", "datum", "tema", "källa", "förbehåll", "vikt",
        "bäst_före", "kontrollerad", "ersatt_av"]
KÄLLFÄLT = ["url", "titel", "citat", "hämtad", "arkiv"]
DATUM_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
DAG_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[A-Za-z0-9_]+-\d{2,3}$")
REF_RE = re.compile(r"\b[A-Za-z0-9_]{3,}-\d{2,3}\b")
MAX_CITAT_ORD = 50


def ladda():
    poster, fel = [], []
    for f in sorted(PÅST.glob("*/*.yaml")):
        try:
            p = yaml.safe_load(f.read_text())
        except yaml.YAMLError as e:
            fel.append(f"{f.relative_to(ROOT)}: ogiltig YAML: {e}")
            continue
        p["_fil"] = f
        poster.append(p)
    return poster, fel


def validera(poster):
    fel, ids = [], {}
    for p in poster:
        f = p["_fil"].relative_to(ROOT)
        pid = p.get("id", "?")

        def err(msg):
            fel.append(f"{f} {pid}: {msg}")

        if saknas := [k for k in FÄLT if k not in p]:
            err(f"saknar {saknas}")
            continue
        if okända := [k for k in p if k not in FÄLT and k != "_fil"]:
            err(f"okända fält {okända}")
        if not ID_RE.match(str(pid)) or p["_fil"].stem != pid:
            err("id ska matcha filnamnet och ha formen PREFIX-NN")
        if pid in ids:
            err(f"dubblerat id (även i {ids[pid]})")
        ids[pid] = f
        if not isinstance(p["påstående"], str) or len(p["påstående"]) < 20:
            err("påståendet saknas eller är för kort")
        if p["typ"] not in TYPER:
            err(f"typ {p['typ']!r}, ska vara en av {sorted(TYPER)}")
        if not p["vem"]:
            err("vem saknas")
        if not isinstance(p["datum"], str) or not DATUM_RE.match(p["datum"]):
            err(f"datum {p['datum']!r} ska vara ÅÅÅÅ, ÅÅÅÅ-MM eller ÅÅÅÅ-MM-DD (inom citattecken)")
        elif p["_fil"].parent.name != p["datum"][:4]:
            err(f"ligger i {p['_fil'].parent.name}/ men datum är {p['datum']}")
        if not isinstance(p["tema"], list) or not p["tema"] or set(p["tema"]) - set(TEMAN):
            err(f"tema {p['tema']!r}, ska vara en lista ur {sorted(TEMAN)}")
        if p["vikt"] not in (1, 2, 3):
            err(f"vikt {p['vikt']!r}, ska vara 1, 2 eller 3")
        for fält in ("bäst_före", "kontrollerad"):
            v = p[fält]
            if (v is not None or fält == "kontrollerad") and not (isinstance(v, str) and DAG_RE.match(v)):
                err(f"{fält} {v!r} ska vara ÅÅÅÅ-MM-DD")
        k = p["källa"]
        if not isinstance(k, dict) or [x for x in KÄLLFÄLT if x not in k]:
            err(f"källa ska ha fälten {KÄLLFÄLT}")
            continue
        if not str(k["url"]).startswith(("http://", "https://")):
            err("källa.url ska vara en webbadress")
        if not k["citat"]:
            err("källa.citat saknas: ett verifierat påstående har alltid ett ordagrant citat")
        elif len(k["citat"].split()) > MAX_CITAT_ORD:
            err(f"källa.citat är längre än {MAX_CITAT_ORD} ord")
        if k["hämtad"] is not None and not (isinstance(k["hämtad"], str) and DAG_RE.match(k["hämtad"])):
            err(f"källa.hämtad {k['hämtad']!r} ska vara ÅÅÅÅ-MM-DD")
        if k["arkiv"] is not None and not str(k["arkiv"]).startswith("https://"):
            err("källa.arkiv ska vara en webbadress eller null")
    for p in poster:
        if not isinstance(p.get("källa"), dict):
            continue
        f = p["_fil"].relative_to(ROOT)
        if p.get("ersatt_av") and p["ersatt_av"] not in ids:
            fel.append(f"{f}: ersatt_av {p['ersatt_av']} finns inte")
        for ref in REF_RE.findall(p.get("förbehåll") or ""):
            if ref not in ids and not DATUM_RE.match(ref):
                fel.append(f"{f}: förbehållet hänvisar till {ref}, som inte finns i arkivet")
    return fel


def ren(p):
    return {k: p[k] for k in FÄLT}


def sortera(poster):
    return sorted(poster, key=lambda p: (p["datum"], p["id"]))


def citera(p):
    k = p["källa"]
    titel = f"{k['titel']}. " if k["titel"] else ""
    return f"{p['vem']}, {p['datum']}. {titel}{k['url']}. Via Belagt {p['id']}: {SIDA_URL}#{p['id']}"


def md_post(p, relativ=".."):
    k = p["källa"]
    arkiv = f" · [arkivkopia]({k['arkiv']})" if k["arkiv"] else ""
    ersatt = f"\n  *Ersatt av {p['ersatt_av']}.*" if p["ersatt_av"] else ""
    rader = [
        f"- **{p['påstående']}**{ersatt}",
        f"  {p['vem']} · {p['datum']} · {', '.join(p['tema'])} · "
        f"[{p['id']}]({relativ}/påståenden/{p['datum'][:4]}/{p['id']}.yaml)",
        f"  > {k['citat']}",
        f"  > — [{k['titel'] or k['url']}]({k['url']}){arkiv}",
    ]
    if p["förbehåll"]:
        rader.append(f"\n  *Förbehåll:* {p['förbehåll']}")
    return "\n".join(rader) + "\n"


HUVUD = "<!-- Genereras av tools/bygg.py. Redigera påståenden/ i stället. -->\n\n"


def tidslinje(poster):
    ut = [HUVUD, "# Tidslinje\n\n",
          f"Alla {len(poster)} påståenden i arkivet, i den ordning det de handlar om hände eller sades.\n"]
    år = None
    for p in sortera(poster):
        if p["datum"][:4] != år:
            år = p["datum"][:4]
            ut.append(f"\n## {år}\n\n")
        ut.append(md_post(p, "."))
    return "".join(ut)


def tema_md(tema, poster):
    urval = [p for p in sortera(poster) if tema in p["tema"]]
    ut = [HUVUD, f"# {tema.capitalize()}\n\n", f"{TEMAN[tema]}\n\n",
          f"{len(urval)} påståenden, de viktigaste först inom varje år.\n"]
    per_år = defaultdict(list)
    for p in urval:
        per_år[p["datum"][:4]].append(p)
    for år in sorted(per_år, reverse=True):
        ut.append(f"\n## {år}\n\n")
        for p in sorted(per_år[år], key=lambda p: (-p["vikt"], p["datum"], p["id"])):
            ut.append(md_post(p))
    return "".join(ut)


def data_csv(poster):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["id", "datum", "påstående", "typ", "vem", "tema", "vikt", "källa_url", "källa_titel",
                "citat", "hämtad", "arkiv", "förbehåll", "bäst_före", "kontrollerad", "ersatt_av"])
    for p in sortera(poster):
        k = p["källa"]
        w.writerow([p["id"], p["datum"], p["påstående"], p["typ"], p["vem"], ";".join(p["tema"]),
                    p["vikt"], k["url"], k["titel"] or "", k["citat"], k["hämtad"] or "",
                    k["arkiv"] or "", p["förbehåll"] or "", p["bäst_före"] or "", p["kontrollerad"],
                    p["ersatt_av"] or ""])
    return buf.getvalue()


def data_json(poster):
    return json.dumps({"källa": REPO_URL, "licens": "CC BY 4.0", "teman": TEMAN,
                       "påståenden": [dict(ren(p), citera=citera(p)) for p in sortera(poster)]},
                      ensure_ascii=False, indent=1) + "\n"


def generera(poster):
    ut = {
        "data/belagt.json": data_json(poster),
        "data/belagt.csv": data_csv(poster),
        "docs/belagt.json": data_json(poster),
        "tidslinje.md": tidslinje(poster),
    }
    for tema in TEMAN:
        ut[f"teman/{tema}.md"] = tema_md(tema, poster)
    return ut


def main():
    kontroll = "--kontroll" in sys.argv
    poster, fel = ladda()
    fel += validera(poster)
    if fel:
        print("\n".join(fel))
        sys.exit(f"{len(fel)} fel i {len(poster)} poster")
    utdata = generera(poster)
    inaktuella = []
    for namn, text in utdata.items():
        f = ROOT / namn
        if f.exists() and f.read_text() == text:
            continue
        if kontroll:
            inaktuella.append(namn)
        else:
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(text)
    if inaktuella:
        sys.exit("Genererade filer är inte aktuella, kör python tools/bygg.py:\n  " + "\n  ".join(inaktuella))
    print(f"{len(poster)} påståenden, 0 fel" + ("" if kontroll else f", {len(utdata)} filer byggda"))


if __name__ == "__main__":
    main()
