# Metod

## Vad som räknas som belagt

1. **Primärkällan är hämtad och läst.** Primärkällan är till exempel företagets egen rapport,
   forskningsartikeln, lagtexten, myndighetens pressmeddelande eller intervjun där personen
   säger det. En nyhetsartikel duger som källa bara när den är primärkällan, till exempel när
   den har intervjun, eller när originalet inte går att nå (det står då i förbehållet).
2. **Ett ordagrant citat ur källan bekräftar påståendet.** Citatet kontrolleras maskinellt mot
   den hämtade källtexten innan posten publiceras, och därefter varje månad mot arkivkopian
   (se *Citatkontroll* nedan).
3. **En människa har granskat posten.** Varje ny post kommer in via en pull request.

**Hämta primärkällan, inte den som återger den.** När en rapport eller en tidning återger vad
någon annan har sagt eller beslutat, ska posten helst bygga på originalet: lagtexten i stället för
sammanfattningen av den, myndighetens beslut i stället för analysföretagets referat. Går
originalet inte att nå står det i `vem` ("återgivet av …") och i förbehållet. Sådana poster listas
i [statistik.md](statistik.md) och ska bytas ut när originalet hittas: den nya posten läggs till och
den gamla får `ersatt_av`.

Källor bakom betalvägg eller inloggning (till exempel x.com) kan inte kontrolleras på det här
sättet, och påståenden som bara bygger på sådana källor tas inte med.

## Vilka avsändare som kan vara källa

Arkivet har ingen lista över godkända källor. Varje påstående prövas för sig, och källans tyngd
redovisas med `källa.typ` och i hur påståendet attribueras. Men ett ordagrant citat räcker inte om
avsändaren inte är värd att citera. Därför gäller också:

- **Avsändaren ska gå att identifiera.** En namngiven myndighet, organisation, forskargrupp,
  person eller redaktion med ansvarig utgivare. Anonyma sajter och sajter som ser
  automatgenererade eller maskinöversatta ut tas inte med.
- **Betalda pressmeddelanden och annonser är aldrig källa**, inte heller när de publiceras på en
  känd nyhetssajt. Ett företags pressmeddelande på den egna webbplatsen kan vara källa, som
  `partsuppgift`.
- **Återpublicering är inte källa.** Sajter som publicerar andras texter igen (till exempel
  TradingView) leder vidare till originalet, som är det som citeras.
- **Åsikter tas med från avsändare med relevans.** En `opinion` ska komma från någon vars
  bedömning väger i frågan: forskare inom området, beslutsfattare, eller ledande företrädare för
  företag, myndigheter eller organisationer. Inte vem som helst som skriver om AI.
- **Statliga medier och partsuppgifter kan vara källa för vad avsändaren hävdar**, men aldrig
  för att något är sant. De återges som det de är (se *Källor på andra språk* nedan).

Sajter som aldrig kan vara källa spärras i bevakningen (`BLOCKERADE` i
[tools/bevaka.py](tools/bevaka.py)), så att de inte heller dyker upp som tips. Samma regler gäller
för poster som tas fram automatiskt: de kommer in via en pull request som en människa granskar
mot den här metoden.

## Källor på andra språk

Citatet står alltid på **originalspråket**, till exempel kinesiska, eftersom det är det som kontrolleras
mot källtexten. Översättningen ligger bredvid och är tydligt märkt:

```yaml
källa:
  citat: 我不信任 Anthropic 或者 OpenAI 能这样做 …
  språk: zh                          # ISO 639-1
  översättning: Jag litar inte på att Anthropic eller OpenAI kan göra det här …
  översatt_av: Claude (AI)
  granskad_av: null                  # namnet på en människa som läser språket, när den är granskad
```

- Citatet kontrolleras maskinellt mot källtexten. Översättningen kan inte kontrolleras så, och därför
  syns det alltid vem som översatt och om någon som läser språket har granskat den.
- För kinesiska, japanska och koreanska bortser kontrollen från mellanslag, och citatet får vara högst
  120 tecken.
- Statliga medier återges som det de är, till exempel "enligt Xinhua (Kinas statliga nyhetsbyrå)",
  på samma sätt som företagens uppgifter om sig själva återges som partsuppgifter.

## Urval: vad som tas med

Varje enskild post kan vara korrekt och arkivet ändå ge en skev bild, om urvalet är skevt. Därför:

- **Källor bevakas systematiskt.** [bevakning.yaml](bevakning.yaml) är en fast lista med
  myndigheter, forskning, företag, kritiker och regioner. Primärkällornas egna flöden går före
  nyhetssökningar, som bara används där sådana flöden saknas. Varje vecka läser
  [tools/bevaka.py](tools/bevaka.py) flödena och lägger det som är nytt i ärendet *Nytt att granska*.
  Listan är medvetet blandad och vem som helst kan föreslå tillägg.
- **Motröster tas med.** Bedömningar som går emot varandra tas med på samma villkor. Ett påstående
  väljs inte bort för att det inte passar arkivets ursprung.
- **Ingen enskild källa ska dominera.** När en rapport eller ett företag står för en stor del av
  posterna inom ett tema prioriteras andra källor.
- **Bredd i världen.** Arkivet ska inte bara spegla USA, Storbritannien, Kina och Sverige.
  Bevakningen omfattar därför också EU, Norden, Indien, Japan, Sydkorea, Afrika och Latinamerika.
- **Fördelningen redovisas öppet.** [statistik.md](statistik.md) genereras vid varje bygge och visar
  hur posterna fördelar sig på tema, typ, källtyp, språk, år och avsändare.

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
  typ: rapport             # vilken sorts källa, se tabellen nedan
  citat: New Interim Measures on …   # ordagrant, högst 50 ord
  hämtad: '2026-09-24'     # när källtexten hämtades och kontrollerades
  arkiv: https://web.archive.org/…   # arkivkopia, fylls i automatiskt varje vecka
förbehåll: Nyanser och sådant som behöver vägas in, eller null
vikt: 3                    # 1–3, hur central posten är (3 = kärnpåstående)
bäst_före: '2027-07-01'    # när posten bör kontrolleras igen, null om den inte åldras
kontrollerad: '2026-09-28' # senaste kontrollen mot källan
ersatt_av: null            # id för en nyare post, om den här blivit inaktuell
```

### Typ av källa

`källa.typ` visar hur tung källan är, utan att läsaren behöver läsa förbehållet. Den syns på
webbsidan, går att filtrera på och finns i data.

| Typ | Betyder |
|---|---|
| `myndighet` | Regering, myndighet, parlament eller mellanstatlig organisation |
| `granskad` | Vetenskaplig artikel som har granskats av andra forskare före publicering |
| `preprint` | Forskningsartikel som inte har granskats (än), till exempel på arXiv |
| `rapport` | Rapport från forskningsinstitut, universitet, tankesmedja, analysföretag eller intresseorganisation, om något annat än den egna verksamheten |
| `partsuppgift` | Företag eller organisation som skriver om sig själv, sina produkter eller sina ståndpunkter |
| `opinion` | Person eller grupp som argumenterar i eget namn: essä, blogg, debattartikel, tal eller öppet brev |
| `media` | Nyhetsartikel, reportage eller intervju i medier |

När flera passar gäller den översta som stämmer, utom att ett företags forskningsartikel om
den egna produkten är `partsuppgift`. En preprint som senare publiceras efter granskning blir
`granskad`.

## Arkivet som historisk dokumentation

- **Ingenting tas bort.** När ett påstående blir inaktuellt, till exempel när en ny mätning
  ersätter en gammal, läggs en ny post till och den gamla får `ersatt_av`. Då går det att se hur
  kunskapsläget har förändrats.
- **Källorna arkiveras.** Varje vecka söker ett skript upp eller skapar en kopia av källan i
  Wayback Machine, så att citatet går att kontrollera även om sidan försvinner eller ändras. Sajter
  som blockerar Wayback Machine får i stället den senaste kopian i archive.today, om det finns någon.
- **Citaten kontrolleras igen, öppet.** Varje månad hämtar
  [tools/kontrollera_citat.py](tools/kontrollera_citat.py) arkivkopian (eller källan, om kopia
  saknas) och kontrollerar att citatet fortfarande står där. Citat som inte hittas, döda länkar och
  sidor som inte gick att hämta hamnar i ärendet *Citatkontroll*. Vem som helst kan köra skriptet
  själv, så att ingen behöver lita på att kontrollen gjordes när posten skrevs.
- **Länken går till citatet.** Källänken på webbsidan och i tidslinjen är en
  [textfragmentlänk](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments)
  som öppnar källan med citatet markerat, i webbläsare som stöder det. PDF-filer stöder det inte.
- **Poster kontrolleras igen.** Varje månad listar ett arbetsflöde de poster som har passerat
  `bäst_före` i ärendet *Dags att kontrollera igen*, med de som går ut inom en månad. En post
  som fortfarande stämmer får ny `kontrollerad` och ett nytt `bäst_före`. En post som inte
  längre stämmer ersätts av en ny.
- **Ändringar syns.** Varje ändring görs som en commit med förklaring, och historiken är öppen.

## Arbetsgång

```
pip install -r requirements.txt
python tools/bygg.py            # validera och bygg tidslinje, teman, data och webbsidans data
python tools/bygg.py --kontroll # det som körs i CI
python tools/arkivera.py        # hämta arkivkopior (körs också varje vecka)
python tools/kontrollera_citat.py  # kontrollera citaten mot källorna (körs också varje månad)
python tools/bevaka.py          # nytt i de bevakade källorna (körs också varje vecka)
python tools/bast_fore.py       # poster att kontrollera igen (körs också varje månad)
```

Nya poster tas fram i ett separat arbetsrepo där källtexterna finns hämtade och citaten
kontrolleras mot dem. När något nytt har verifierats där öppnas automatiskt en pull request
hit (grenar som heter `nya-ÅÅÅÅ-MM-DD`), och ingenting kommer in förrän den är granskad.

Du kan också föreslå en post direkt: skapa en fil enligt mallen ovan, kör `python tools/bygg.py`
och öppna en pull request med länk till källan. Id:t får då prefixet `BID-` följt av nästa lediga nummer.

Allt i `tidslinje.md`, `statistik.md`, `teman/`, `data/` och `docs/belagt.json` genereras och redigeras aldrig
för hand.
