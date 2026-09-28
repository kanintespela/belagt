# Metod

## Vad som räknas som belagt

1. **Primärkällan är hämtad och läst.** Primärkällan är till exempel företagets egen rapport,
   forskningsartikeln, lagtexten, myndighetens pressmeddelande eller intervjun där personen
   säger det. En nyhetsartikel duger som källa bara när den är primärkällan, till exempel när
   den har intervjun, eller när originalet inte går att nå (det står då i förbehållet).
2. **Ett ordagrant citat ur källan bekräftar påståendet.** Citatet kontrolleras maskinellt mot
   den hämtade källtexten innan posten publiceras.
3. **En människa har granskat posten.** Varje ny post kommer in via en pull request.

Källor bakom betalvägg eller inloggning (till exempel x.com) kan inte kontrolleras på det här
sättet, och påståenden som bara bygger på sådana källor tas inte med.

## Hur ett påstående formuleras

- **Ett påstående per post.** Om det finns ett "och" som går att dela, ska posten delas.
- **Attribuera, generalisera inte.** "Amodei bedömer att …", inte "AI kommer att …". En bedömning
  blir inte ett faktum för att den upprepas.
- **Partsuppgifter återges som partsuppgifter.** När ett företag skriver om sin egen produkt står
  det "OpenAI uppger".
- **Posten ska kunna läsas ensam**, utan sammanhang.

## Fält

Varje post är en fil, `påståenden/<år>/<id>.yaml`:

```yaml
id: KIN-02                 # ändras aldrig, andra texter kan hänvisa hit
påstående: Kina införde från juli 2026 bindande regler för …
typ: händelse              # händelse · mätning · bedömning · prognos · förslag
vem: Kinas myndigheter, återgivet av Concordia AI
datum: 2026-07             # när det hände eller sades, så exakt som källan medger
tema: [styrning]           # se README
källa:
  url: https://…           # primärkällan
  titel: 'Concordia AI: State of AI Safety in China 2026'
  citat: New Interim Measures on …   # ordagrant, högst 50 ord
  hämtad: '2026-09-24'     # när källtexten hämtades och kontrollerades
  arkiv: https://web.archive.org/…   # arkivkopia, fylls i automatiskt varje vecka
förbehåll: Nyanser och sådant som behöver vägas in, eller null
vikt: 3                    # 1–3, hur central posten är (3 = kärnpåstående)
bäst_före: '2027-07-01'    # när posten bör kontrolleras igen, null om den inte åldras
kontrollerad: '2026-09-28' # senaste kontrollen mot källan
ersatt_av: null            # id för en nyare post, om den här blivit inaktuell
```

## Arkivet som historisk dokumentation

- **Ingenting tas bort.** När ett påstående blir inaktuellt, till exempel när en ny mätning
  ersätter en gammal, läggs en ny post till och den gamla får `ersatt_av`. Då går det att se hur
  kunskapsläget har förändrats.
- **Källorna arkiveras.** Varje vecka söker ett skript upp eller skapar en kopia av källan i
  Wayback Machine, så att citatet går att kontrollera även om sidan försvinner eller ändras.
- **Ändringar syns.** Varje ändring görs som en commit med förklaring, och historiken är öppen.

## Arbetsgång

```
pip install -r requirements.txt
python tools/bygg.py            # validera och bygg tidslinje, teman, data och webbsidans data
python tools/bygg.py --kontroll # det som körs i CI
python tools/arkivera.py        # hämta arkivkopior (körs också varje vecka)
```

Nya poster tas fram i ett separat arbetsrepo där källtexterna finns hämtade och citaten
kontrolleras mot dem. De kommer in hit som pull requests. Du kan också föreslå en post direkt:
skapa en fil enligt mallen ovan, kör `python tools/bygg.py` och öppna en pull request med länk
till källan. Id:t får då prefixet `BID-` följt av nästa lediga nummer.

Allt i `tidslinje.md`, `teman/`, `data/` och `docs/belagt.json` genereras och redigeras aldrig
för hand.
