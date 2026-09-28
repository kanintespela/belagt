# Belagt

**Verifierade påståenden om AI-utvecklingen, med primärkällor.**

Belagt är ett växande arkiv på svenska. Varje post är ett enda påstående om vad som har hänt,
mätts, bedömts eller föreslagits inom AI-utvecklingen. Till varje påstående hör vem som står
bakom det, när det hände och ett ordagrant citat ur primärkällan. Tanken är att du ska kunna
kontrollera varje påstående själv och hänvisa rätt när du skriver.

👉 **Sök i arkivet: [kanintespela.github.io/belagt](https://kanintespela.github.io/belagt/)**

## Vad kan jag använda det till?

- **Skriva eget material.** Faktablad, debattartiklar, föredrag, studiecirklar och
  lektioner kan hämta sina belägg härifrån. Varje post har en färdig källhänvisning att kopiera.
- **Kontrollera något du har hört.** Sök på ett namn, ett företag eller en händelse.
- **Följa utvecklingen över tid.** [Tidslinjen](tidslinje.md) visar allt i datumordning.
  Påståenden som blir inaktuella tas aldrig bort, utan märks med vad som ersatt dem.
- **Bygga verktyg.** Hela arkivet finns som [JSON](data/belagt.json) och [CSV](data/belagt.csv).

## Teman

| Tema | Handlar om |
|---|---|
| [förmågor](teman/förmågor.md) | Vad AI-systemen kan göra och hur det mäts |
| [tempo](teman/tempo.md) | Hur snabbt utvecklingen går och varför |
| [självförbättring](teman/självförbättring.md) | AI som används för att utveckla AI |
| [kontroll](teman/kontroll.md) | Går systemen att styra, övervaka och testa? |
| [missbruk](teman/missbruk.md) | Cyberangrepp, påverkan och biologiska risker |
| [styrning](teman/styrning.md) | Reglering, tillsyn och förslag om att bromsa |
| [geopolitik](teman/geopolitik.md) | Kapplöpningen mellan länder |
| [nytta](teman/nytta.md) | Vad AI redan gör för sjukvård, forskning och samhälle |
| [röster](teman/röster.md) | Vad forskare, insiders och politiker säger |
| [samhälle](teman/samhälle.md) | Jobb, ekonomi, beroende och AI-kompanjoner |

## Vad betyder "belagt"?

Ett påstående kommer bara in i arkivet om det har kontrollerats mot primärkällan och ett
ordagrant citat därifrån bekräftar det. Det betyder att **källan säger så**, inte att det källan
säger är sant. När OpenAI skriver om sin egen modell står det därför "OpenAI uppger" och inte
att något är ett faktum. Förbehållen under varje post anger vad som behöver vägas in.
Hur kontrollen går till står i [METOD.md](METOD.md).

## Så här hänvisar du

Hänvisa till primärkällan och gärna till posten här, till exempel:

> Epoch AI (oberoende forskningsinstitut), 2026-09. Trends in Artificial Intelligence. https://epoch.ai/trends. Via Belagt TID-01: https://kanintespela.github.io/belagt/#TID-01

Knappen *Kopiera källhänvisning* på webbsidan ger den texten. Id:t (`TID-01`) ändras aldrig.

## Ursprung och öppenhet

Arkivet började som underlag för folkbildningsmaterial som en volontär i
[PauseAI](https://pauseai.info) tar fram. PauseAI vill att utvecklingen av de mest kraftfulla
AI-systemen pausas tills de går att göra säkra. Arkivet är ändå inte ett argument för en viss
hållning. Det innehåller också motröster, osäkerheter och exempel på vad AI redan gör för nytta.
Ett arkiv som bara tar med det som passar den egna saken blir oanvändbart för alla, den egna
saken inräknad.

AI (Claude) används för att hitta, extrahera och kontrollera påståenden. Varje post granskas av
en människa innan den kommer in, och citatet kontrolleras maskinellt mot den hämtade källtexten.

## Bidra

Har du hittat ett fel, en död länk eller ett påstående som saknas? Öppna ett
[ärende](https://github.com/kanintespela/belagt/issues). Förslag på nya poster går också
att skicka som pull request, se [METOD.md](METOD.md).

## Licens

Innehållet får användas fritt, även kommersiellt, om du anger källan:
[CC BY 4.0](LICENSE). Koden i `tools/` och `docs/` är [MIT](LICENSE-kod). Citaten ur
primärkällorna är korta utdrag som återges med stöd av citaträtten, och upphovsrätten till dem
ligger kvar hos källan.
