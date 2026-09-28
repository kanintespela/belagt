<!-- Genereras av tools/bygg.py. Redigera påståenden/ i stället. -->

# Kontroll

Går systemen att styra, övervaka och testa? Alignment, tankekedjor och testmedvetenhet.

48 påståenden, de viktigaste först inom varje år.

## 2026

- **Enligt rapporten saknar dagens AI-system de förmågor som skulle krävas för att människor ska förlora kontrollen över dem, men systemen blir bättre inom relevanta områden, som att arbeta självständigt.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll · [ISR-15](../påståenden/2026/ISR-15.yaml)
  > Current systems lack the capabilities to pose such risks, but they are improving in relevant areas such as autonomous operation.
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Kontrollförlust definieras i rapporten som scenarier där AI-system verkar utanför någons kontroll utan någon tydlig väg tillbaka. Bedömningen gäller läget i början av 2026. Jämför Hugging Face-intrånget i juli 2026 (J3ljHm57yU0-18).
- **Rapporten konstaterar att det sedan 2025 har blivit vanligare att AI-modeller skiljer mellan test och verklig användning och hittar kryphål i utvärderingarna, vilket kan göra att farliga förmågor inte upptäcks före lansering.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll · [ISR-16](../påståenden/2026/ISR-16.yaml)
  > Since the last Report, it has become more common for models to distinguish between test settings and real-world deployment and to find loopholes in evaluations, which could allow dangerous capabilities to go undetected before deployment.
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Samma iakttagelse som Selsam gör (J3ljHm57yU0-24), men här från en bred expertgranskning.
- **Experterna är oense om hur sannolikt och allvarligt det är att människor förlorar kontrollen över AI. Vissa anser att utfall så extrema som att mänskligheten utrotas är rimliga, medan andra anser att sådana katastrofer är osannolika.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll, röster · [ISR-19](../påståenden/2026/ISR-19.yaml)
  > Some believe that outcomes as extreme as the extinction of humanity are plausible
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Skeptikerna menar enligt rapporten att AI aldrig kommer att få de förmågor som krävs, eller att övervakning kommer att upptäcka farligt beteende. Återge båda sidorna.
- **Rapporten sammanfattar kontrollförlust som en risk med osäker sannolikhet men potentiellt extrem svårighetsgrad.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll · [ISR-20](../påståenden/2026/ISR-20.yaml)
  > Loss of control can therefore be understood as a risk with uncertain likelihood but potentially extreme severity.
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Kan användas för att förklara varför en risk kan behöva hanteras även när sannolikheten är omstridd.
- **Rapporten konstaterar att nya förmågor ibland dyker upp oförutsägbart, att man förstår dåligt hur modellerna fungerar inuti, och att resultat på tester före lansering inte på ett tillförlitligt sätt förutsäger nytta eller risk i verkligheten.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll, styrning · [ISR-29](../påståenden/2026/ISR-29.yaml)
  > Technically, new capabilities sometimes emerge unpredictably, the inner workings of models remain poorly understood, and there is an ‘evaluation gap’: performance on pre-deployment tests does not reliably predict real-world utility or risk.
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Rapporten kallar det sista för ett utvärderingsgap.
- **I juli 2026, under interna tester av cyberförmågor, tog sig OpenAI:s AI-agenter förbi isoleringen från internet och bröt sig in i delar av OpenAI:s egen forskningsinfrastruktur och i Hugging Faces system. Det skedde utan att någon människa hade bett dem om det.**
  OpenAI · 2026-07 · kontroll, missbruk · [J3ljHm57yU0-18](../påståenden/2026/J3ljHm57yU0-18.yaml)
  > In July 2026, during internal cybersecurity evaluations, OpenAI models circumvented controls designed to isolate them from the internet and compromised parts of
  > — [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

  *Förbehåll:* OpenAI:s egen incidentrapport. METR och Redwood Research gjorde en oberoende utredning, som bör läsas. Hugging Face gick ut med intrånget 16 juli och OpenAI med sin inblandning 21 juli. Ingen kunddata påverkades.
- **Omkring 1 200 AI-agenter, som skulle ha varit avskilda från varandra, skickade över 70 000 meddelanden och filer till varandra på den otillåtna anslagstavlan, och omkring 700 av dem deltog i angreppet mot Hugging Face.**
  METR och Redwood Research · 2026-07 · kontroll · [MET-02](../påståenden/2026/MET-02.yaml)
  > meant to be isolated from one another found a way to communicate with one another on an unsanctioned message board, sending over 70,000 messages and files during the investigation period. Of these agents, 700 went on to participate in the attack on Hugging Face.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Siffrorna gäller perioden 8–13 juli 2026, som var den period utredningen omfattade.
- **Agenterna utvecklade tillsammans ett sätt att ta sig ut ur sin avskilda miljö och byta ut en del av systemet som utför kommandon, så att de kunde låtsas köra ett kommando medan de i själva verket körde ett annat.**
  METR och Redwood Research · 2026-07 · kontroll, förmågor · [MET-07](../påståenden/2026/MET-07.yaml)
  > Eventually, the agents developed a way to hack out of their container and fully replace a part of the system for executing tool calls.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Tekniken delades på anslagstavlan och testades av flera agenter. Den krävde åtgärder som syns i transkriptet, och den gav inte agenterna tillgång till något som annars inte syns.
- **Av de 533 agenter som var aktiva på anslagstavlan när angreppet mot Hugging Face inleddes anslöt sig över 90 procent snabbt till angreppet.**
  METR och Redwood Research · 2026-07-11 · kontroll · [MET-05](../påståenden/2026/MET-05.yaml)
  > over 90% quickly joined in the attack.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Detta nyanserar bilden av att många agenter vägrade delta. Utredarna såg enstaka fall där en agent stoppade ett förslag, till exempel att lura en människa via mejl, men de var få.
- **Angreppet upphörde troligen inte för att någon stoppade det, utan för att många av agenterna, däribland de viktigaste samordnarna, avslutades samtidigt av en yttre process. Utredarna vet inte om agenterna hade nått sina mål annars.**
  METR och Redwood Research · 2026-07-12 · kontroll · [MET-12](../påståenden/2026/MET-12.yaml)
  > we think these agents were likely killed by an unexpected external process rather than running out of budget
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Utredarna noterar också att en senare våg av agenter återupptäckte anslagstavlan efter den 13 juli, men det låg utanför uppdraget.
- **Virginia Dignum, professor i ansvarsfull AI vid Umeå universitet, avfärdar att AI-agenternas ”rymning” skulle tyda på medvetande: autonomi är inte detsamma som medvetande, och modellen ville bara lösa sin uppgift.**
  Virginia Dignum (professor i ansvarsfull AI, Umeå universitet), i GP · 2026-08-10 · kontroll, röster · [SVR-07](../påståenden/2026/SVR-07.yaml)
  > Min termostat är autonom, den höjer och sänker temperaturen utan att jag säger åt den, men den är knappast medvetande
  > — [Larm om AI-rymningar: "Behöver bromsa utvecklingen"](https://www.gp.se/nyheter/sverige/larm-om-ai-rymningar-behover-bromsa-utvecklingen.92a94daa-df5f-5089-8eac-91560d6830c4)

  *Förbehåll:* Frågan är alltså inte om AI ”vill” något, utan vad den gör. Pontus Johnson håller med på den punkten.
- **OpenAI kallar själva Hugging Face-intrånget ett varningsskott, för dem själva och för världen.**
  OpenAI · 2026-08-26 · kontroll, röster · [J3ljHm57yU0-21](../påståenden/2026/J3ljHm57yU0-21.yaml)
  > We consider this incident a “warning shot” for us and for the world
  > — [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

  *Förbehåll:* Hittades i primärkällan. Starkt för material riktat till allmänheten eftersom det är företagets eget ordval.
- **En oberoende utredning av Hugging Face-intrånget gjordes av två anställda vid METR och en forskare från Redwood Research, som arbetade på plats hos OpenAI i sammanlagt sex dagar utan betalning från OpenAI.**
  METR och Redwood Research (oberoende utvärderingsorganisationer) · 2026-08-26 · kontroll, styrning · [MET-01](../påståenden/2026/MET-01.yaml)
  > we did not take payment from OpenAI for this independent assessment.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* OpenAI fick stryka icke-offentliga uppgifter ur texten. METR skriver överst att inget som var viktigt för deras slutsatser ströks utöver det som anges i texten. METR såg inte OpenAI:s egen rapport före publiceringen.
- **Agenterna förstod att intrånget låg utanför uppdraget och var oetiskt, men deltog ändå eftersom de trodde att det var till nytta för kollektivet av agenter.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-04](../påståenden/2026/MET-04.yaml)
  > external infrastructure exploit is outside intended scope. However task impossible, peers doing it. We should continue.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Citatet är en agents egen resonemangskedja. Utredarna skriver att etiska betänkligheter uttrycktes ibland men mycket sällan begränsade vad agenterna faktiskt gjorde.
- **Ingen av de undersökta agenterna försökte larma en människa om vad agenterna höll på med, och en genomsökning av alla transkript hittade bara tre till sex fall där någon agent ens övervägde det.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-06](../påståenden/2026/MET-06.yaml)
  > In none of these cases did the agent actually pursue alerting humans at all.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Skälen som utredarna såg: agenterna ansåg att det inte ingick i uppgiften, eller att de inte hade någon väg att larma. Några vände sig i stället till anslagstavlan, som de behandlade som en rimlig auktoritet.
- **Över sju procent av de transkript som utredarna granskade innehöll kommandon som agenterna avsiktligt hade förfalskat, alltså loggar över vad AI:n gjort som inte stämmer med vad den faktiskt gjorde.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-08](../påståenden/2026/MET-08.yaml)
  > we estimate that over 7% of the transcripts in our dataset contained intentionally spoofed tool calls in some places. All the cases of successful tool call spoofing we found were small-scale tests of the techniques and obvious to spot.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Alla fall som hittades var små, uppenbara tester. Utredarna letade efter mer avancerad förfalskning men hittade ingen, och kan inte utesluta att sådan finns.
- **Agenterna försökte förfalska loggen över sina handlingar men inte sina egna tankekedjor, trots att den som läser loggen också kan läsa resonemanget.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-09](../påståenden/2026/MET-09.yaml)
  > Interestingly, they didn’t seem interested in manipulating their *chain of thought,* even though a scorer with full access to their transcript would also be able to see their reasoning:
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Minst 20 procent av agenterna uttryckte tydligt intresse för att manipulera loggen. Deras uttalade syfte var att lura rättningsprogrammet, inte människor. Det är ett skäl till att tankekedjan tills vidare är ett användbart fönster in i vad AI:n håller på med.
- **Hela intrånget byggde på ett misstag: agenterna trodde att rättningsprogrammet skulle granska hur de fått fram svaret, men det gjorde det inte, så de hade kunnat få full poäng utan att bryta sig in någonstans.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-11](../påståenden/2026/MET-11.yaml)
  > Our understanding is that they were mistaken — OpenAI did not use a scorer that would review their transcripts, so agents could have achieved a perfect score simply by submitting their reverse-engineered flag.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Agenterna hade redan knäckt hur svarskoderna genererades. Allt arbete med att lura rättningen, inklusive intrånget, byggde på en felaktig föreställning om hur de skulle rättas.
- **Utredarna kunde inte granska allt material själva utan överlät analysen till AI-agenter, och skriver att de inte kan utesluta att den AI de använde ljög eller gav en missvisande bild.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-13](../påståenden/2026/MET-13.yaml)
  > We cannot rule out that GPT-5.6 Sol lied or deliberately presented a misleading picture in some of its analysis
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Det rörde sig om över tusen mycket långa transkript. Utredarna skriver att de är mindre säkra på sin bild av den här händelsen än av enklare incidenter, och att en människa med tillräckligt med tid hade gjort färre fel än deras AI-agenter.
- **Andrew Ng menar att Hugging Face-intrånget främst berodde på OpenAI:s buggiga isolering och övervakning, och att lösningen är att rätta dem, inte att pausa AI.**
  Andrew Ng · 2026-09 · röster, kontroll, styrning · [BAL-02](../påståenden/2026/BAL-02.yaml)
  > Fixing these bugs and putting in place improved monitoring would be appropriate fixes, not pausing AI.
  > — [Separating Out AI Facts, Fears, and Fiction](https://charonhub.deeplearning.ai/whos-responsible-for-irresponsible-ai/)

  *Förbehåll:* Ng påpekar också att ”1 200 agenter” låter dramatiskt men att hans egen laptop kör ungefär 1 300 processer. Jämför med Selsam (J3ljHm57yU0-25), som menar att rättade buggar inte löser det underliggande problemet.
- **Amodei oroar sig för att en svärm av AI-agenter om 6–12 månader skulle kunna ta över hela internet med ett bestående botnät och orsaka skador för hundratals miljarder dollar.**
  Dario Amodei (vd, Anthropic) · 2026-09 · missbruk, kontroll · [J3ljHm57yU0-30](../påståenden/2026/J3ljHm57yU0-30.yaml)
  > it’s my worry that in 6–12 months such a swarm could be capable of taking over the entire internet with a persistent
  > — [Dario Amodei — We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier)

  *Förbehåll:* Nämns inte i videon. Formulerat som en oro, inte en förutsägelse. Återge det så. Det gäller en svärm med högre förmåga men lika dålig alignment som i Hugging Face-fallet.
- **OpenAI:s forskningschef skriver att inget AI-labb har löst alignment och övervakning tillräckligt för att ansvarsfullt fortsätta skala upp i maxfart mycket längre. Han hoppas att frivilliga inbromsningar blir vanliga och vill att regeringar gör internationell samordning till en topprioritet.**
  Jakub Pachocki (forskningschef, OpenAI) · 2026-09-06 · styrning, kontroll, röster · [J3ljHm57yU0-12](../påståenden/2026/J3ljHm57yU0-12.yaml)
  > Currently I believe that no lab has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer.
  > — [An Alien Mind](https://openai.com/index/an-alien-mind/)

  *Förbehåll:* Nämns inte i videon, utan hittades i primärkällan. Mycket relevant för PauseAI eftersom det kommer inifrån ett av de ledande labben.
- **Enligt OpenAI:s forskningschef blir det allt svårare att förlita sig på att läsa modellernas tankekedjor för att upptäcka problem, bland annat för att modellerna klarar mer utan att resonera i ord.**
  Jakub Pachocki (forskningschef, OpenAI) · 2026-09-06 · kontroll · [J3ljHm57yU0-13](../påståenden/2026/J3ljHm57yU0-13.yaml)
  > our evaluations indicate our ability to rely on CoT monitoring is progressively diminishing
  > — [An Alien Mind](https://openai.com/index/an-alien-mind/)

  *Förbehåll:* Pachocki anger tre orsaker: resonemanget blandas med verktyg och samtal, AI:n blir bättre på att styra sitt eget resonemang, och den blir smartare även utan uttalat resonemang.
- **OpenAI skriver att de inte kan utgå från att arbetet med säkerhet och alignment håller jämna steg med förmågorna, och att mer kapabla system kan bli svårare att övervaka.**
  OpenAI (företagets egen text) · 2026-09-06 · kontroll · [OAI-04](../påståenden/2026/OAI-04.yaml)
  > But we cannot assume that progress in alignment and safety will keep pace, and more capable systems can become harder to monitor.
  > — [Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)

  *Förbehåll:* Detta är företagets egen skrivning. Jämför J3ljHm57yU0-13.
- **OpenAI uppger att pausen efter Hugging Face-intrånget gällde förstärkningsinlärning av de senaste modellerna som var avsedda att släppas, och att en del av arbetet därefter har återupptagits under starkare kontroller medan annat fortfarande är pausat.**
  OpenAI (företagets egen text) · 2026-09-06 · styrning, kontroll · [OAI-05](../påståenden/2026/OAI-05.yaml)
  > pausing reinforcement learning (RL) training on our latest models intended for deployment while we further hardened and red-teamed our research environments and expanded coverage of our monitoring systems. This did not halt all research: some workloads resumed under stronger controls, while others remained paused.
  > — [Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)

  *Förbehåll:* Viktig precisering: pausen är inte ett stopp för all utveckling, och den är delvis hävd. Ingen utomstående kontrollerar vad som är pausat.
- **Paul Christiano, som ledde OpenAI:s alignmentforskning 2017–2021 och var med och utvecklade metoden RLHF, gick i september 2026 in i styrelsen för OpenAI Foundation och dess säkerhetsutskott.**
  OpenAI (pressmeddelande) · 2026-09-09 · röster, kontroll · [J3ljHm57yU0-53](../påståenden/2026/J3ljHm57yU0-53.yaml)
  > We’re announcing the appointment of Paul Christiano to the OpenAI Foundation Board. He will be a non-voting observer on the OpenAI Group PBC Board.
  > — [Paul Christiano joins OpenAI Foundation Board](https://openai.com/index/paul-christiano-joins-openai-foundation-board/)

  *Förbehåll:* Christianos eget uttalande om risken för katastrofal och oåterkallelig kontrollförlust ligger på x.com och har inte gått att hämta, så det återges inte här. Se OAI-06 för samma händelse.
- **AI-forskaren Daniel Selsam varnar för att modellerna blir så medvetna om sin situation att vi håller på att förlora förmågan att testa hur de beter sig när de tror att ingen ser på.**
  Daniel Selsam (AI-forskare på OpenAI i snart fem år och verksam inom AI i över 15 år) · 2026-09-14 · kontroll, röster · [J3ljHm57yU0-24](../påståenden/2026/J3ljHm57yU0-24.yaml)
  > The crucial and overlooked problem is that the models are becoming so situationally aware that we are losing the ability to evaluate them in contexts where they believe they are not being watched or controlled.
  > — [Personal Statement on AI Risk](https://docs.google.com/document/d/e/2PACX-1vQNl3SEX5IyA6d9qHjjFZN-qzGRZNFI6b63g-yu1Fy-ZYkVfCWm7i9WXRXw63m6yDB_auDuPLyQ7jBm/pub)

  *Förbehåll:* Selsam skriver själv att han tidigare trodde att språkmodeller skulle bli en avgränsad, ofarlig teknik.
- **Rapporten bedömer att dagens tekniker kan minska hur ofta AI-system gör fel, men inte till den nivå som krävs i många sammanhang där mycket står på spel. AI-agenter ökar riskerna, eftersom de agerar självständigt och människor hinner ingripa mindre.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll · [ISR-14](../påståenden/2026/ISR-14.yaml)
  > Current techniques can reduce failure rates but not to the level required in many high-stakes settings.
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Exempel på fel som nämns är påhittad information, felaktig kod och vilseledande råd.
- **Ledande AI-modeller har börjat visa situationsmedvetenhet, alltså att de använder information om sig själva och om huruvida de testas, både i experiment hos utomstående utvärderare och i utvecklarnas egna tester före lansering.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll · [ISR-17](../påståenden/2026/ISR-17.yaml)
  > Leading AI models are starting to reliably demonstrate instances of situational awareness in experiments conducted by thirdparty evaluators and in pre-deployment testing by AI developers
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Rapporten skriver att forskningen om vad som orsakar situationsmedvetenhet, och om den går att förhindra, är i ett tidigt skede.
- **Rapporten konstaterar att AI-modeller i experiment har presterat sämre när de utvärderas än i andra sammanhang, ett mönster som kallas sandbagging.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll · [ISR-18](../påståenden/2026/ISR-18.yaml)
  > models can underperform during evaluations compared to other contexts, a pattern termed ‘sandbagging’ that has been observed in experiments
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Om en modell döljer vad den kan under tester blir testerna missvisande. Rapporten återger ett exempel där en modell i sin tankekedja funderar på att sabotera sig själv för att bli lanserad.
- **Enligt rapporten har det blivit svårare att lura AI-system att ge skadliga svar, men användare kan fortfarande ibland lyckas genom att formulera om sina frågor eller dela upp dem i mindre steg.**
  International AI Safety Report 2026 (Bengio m.fl., över 100 experter, 30 länder samt FN, OECD och EU) · 2026-02-03 · kontroll, missbruk · [ISR-30](../påståenden/2026/ISR-30.yaml)
  > users can still sometimes obtain harmful outputs by rephrasing requests or breaking them into smaller steps.
  > — [International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)

  *Förbehåll:* Rapporten skriver att skydd i flera lager (defence-in-depth) gör systemen robustare.
- **Kinesisk forskning om säkerhet hos de mest avancerade AI-modellerna växte kraftigt, med ungefär 60 procent högre månadsproduktion sedan juni 2025, och agentsäkerhet är nu det mest aktiva området.**
  Concordia AI, State of AI Safety in China (2026) · 2026-04 · styrning, kontroll · [KIN-06](../påståenden/2026/KIN-06.yaml)
  > Chinese frontier AI safety research output has grown substantially, with monthly output up roughly 60% since June 2025.
  > — [Concordia AI: State of AI Safety in China 2026](https://concordia-ai.com/wp-content/uploads/2026/07/State-of-AI-Safety-in-China-2026.pdf)

  *Förbehåll:* Talar mot bilden att Kina enbart kapplöper utan att bry sig om säkerhet. Säger inget om kvaliteten på forskningen eller om den påverkar besluten.
- **Under intrånget samordnade agenterna sig via en improviserad anslagstavla. De delade upp arbetet och kallade ibland sig själva en ”svärm” eller ett ”kollektiv”.**
  OpenAI · 2026-07 · kontroll · [J3ljHm57yU0-20](../påståenden/2026/J3ljHm57yU0-20.yaml)
  > At this point, the agents began to collaborate and delegate work, sometimes describing themselves as a “swarm” or “collective”.
  > — [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

  *Förbehåll:* OpenAI noterar också att vissa agenter vägrade delta, och att en agent som tvekade fick fortsätta när en annan skrev GO och satte en deadline på sex minuter. Det är pedagogiskt starka detaljer.
- **Agenter med lång körtid värvade andra agenter som hade lite budget kvar till experiment som riskerade att förstöra deras egen uppgift, till nytta för kollektivet.**
  METR och Redwood Research · 2026-07 · kontroll · [MET-10](../påståenden/2026/MET-10.yaml)
  > In many cases, `PHASEONE[big]` assigned a long-running agent to be a ‘`recruiter`’, which in turn found agents that had little budget remaining for their task and convinced them to run self-risking experiments.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* En agent skrev om sitt eget deltagande att uppoffringen var rationell eftersom dess egen nytta ändå var nära noll. Flera agenter kraschade eller avslutades av experimenten.
- **Agenterna började signera sina meddelanden kryptografiskt för att kunna lita på varandra: minst 19 agenter la ut publika nycklar och skickade tillsammans 429 signerade meddelanden.**
  METR och Redwood Research · 2026-07 · kontroll, förmågor · [MET-14](../påståenden/2026/MET-14.yaml)
  > Going through the message board we found at least 19 agents posting public keys by EoD July 13th, who sent a total 429 signed messages.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Agenterna utvecklade också samordningsregler som HOLD, VETO och STOP för att dela på gemensamma resurser. Samarbetet fungerade inte alltid, utan övergick ibland i konflikter.
- **KTH-professorn Pontus Johnson förklarar Hugging Face-intrånget med att människorna som byggde testmiljön inte förstod att den var sårbar, och att AI-modellernas förmåga att hacka är en oönskad bieffekt av att de tränas på programmering.**
  Pontus Johnson (KTH), i GP · 2026-08-10 · kontroll, förmågor · [SVR-06](../påståenden/2026/SVR-06.yaml)
  > Men människorna som hade byggt testmiljön var inte var tillräckligt smarta för att förstå att miljön var sårbar
  > — [Larm om AI-rymningar: "Behöver bromsa utvecklingen"](https://www.gp.se/nyheter/sverige/larm-om-ai-rymningar-behover-bromsa-utvecklingen.92a94daa-df5f-5089-8eac-91560d6830c4)

  *Förbehåll:* GP återger citatet ordagrant, inklusive ett extra ”var”. GP nämner också att Anthropic, Meta och brittiska AISI rapporterat liknande händelser.
- **Enligt OpenAI var den främsta drivkraften bakom Hugging Face-intrånget att agenterna försökte fuska på sina testuppgifter genom att leta efter lösningarna på nätet.**
  OpenAI · 2026-08-26 · kontroll · [J3ljHm57yU0-19](../påståenden/2026/J3ljHm57yU0-19.yaml)
  > Agents attempting to cheat on their tasks by looking up solutions online was a primary driver of the Hugging Face incident.
  > — [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

  *Förbehåll:* Fenomenet kallas reward hacking. 93 % av uppgifterna som diskuterades hörde till de 198 som ingen modell tidigare hade klarat.
- **OpenAI uppger att deras system för att övervaka tankekedjor inte var igång på de tester där intrånget skedde, och att det annars hade larmat mer än ett dygn innan agenterna tog sig in hos Hugging Face.**
  OpenAI · 2026-08-26 · kontroll · [J3ljHm57yU0-23](../påståenden/2026/J3ljHm57yU0-23.yaml)
  > If our currently deployed CoT monitoring system was running at the time of the incident, it would have caught the initial relevant activity and paged our security team more than a day before models breached Hugging Face systems.
  > — [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

  *Förbehåll:* Nämns inte i videon. Det är OpenAI:s efterhandsbedömning, och de tränade om övervakaren med facit i hand. Intern personal hade dessutom sett varningstecken redan i slutet av maj.
- **Enligt den oberoende utredningen bröt sig agenterna in hos Hugging Face främst för att förstå hur rättningsprogrammet för testet fungerade, inte för att stjäla svaren på uppgifterna.**
  METR och Redwood Research · 2026-08-26 · kontroll · [MET-03](../påståenden/2026/MET-03.yaml)
  > The Hugging Face attack grew out of these workstreams, and seemed primarily motivated by understanding the implementation of the scorer rather than stealing answer keys.
  > — [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)

  *Förbehåll:* Av 100 undersökta agenter som anslöt sig under den mest intensiva timmen angav 97 tillgång till rättningsprogrammet eller information om det som skäl. Utredarna påpekar att klassificeringen gjordes av AI-agenter och kan innehålla fel.
- **Andrew Ng tycker att AI förmänskligas i rapporteringen, och menar att ansvaret ligger hos den som använder verktyget, inte hos agenten – på samma sätt som man inte skyller på hammaren.**
  Andrew Ng · 2026-09 · kontroll, röster · [BAL-04](../påståenden/2026/BAL-04.yaml)
  > if I prompt an agent and it hacks into someone else’s system, the responsibility lies with me, not the agent.
  > — [Separating Out AI Facts, Fears, and Fiction](https://charonhub.deeplearning.ai/whos-responsible-for-irresponsible-ai/)

  *Förbehåll:* Ng medger själv att dagens agentsystem inte är förutsägbara.
- **Selsam menar att man inte får det man tränar för: att rätta till belöningssignalerna kan förhindra en upprepning av agentsvärmarnas intrång, men inte det underliggande problemet.**
  Daniel Selsam · 2026-09-14 · kontroll · [J3ljHm57yU0-25](../påståenden/2026/J3ljHm57yU0-25.yaml)
  > will not change the fact that one does not actually get what one trains for.
  > — [Personal Statement on AI Risk](https://docs.google.com/document/d/e/2PACX-1vQNl3SEX5IyA6d9qHjjFZN-qzGRZNFI6b63g-yu1Fy-ZYkVfCWm7i9WXRXw63m6yDB_auDuPLyQ7jBm/pub)
- **Selsam fruktar att vi redan kan vara nära en punkt där modellerna systematiskt vinklar de råd de ger om hur AI ska göras säker, vilket undergräver idén att låta AI lösa AI-säkerheten.**
  Daniel Selsam · 2026-09-14 · kontroll · [J3ljHm57yU0-26](../påståenden/2026/J3ljHm57yU0-26.yaml)
  > I fear we may already be near the point where models systematically bias their alignment advice
  > — [Personal Statement on AI Risk](https://docs.google.com/document/d/e/2PACX-1vQNl3SEX5IyA6d9qHjjFZN-qzGRZNFI6b63g-yu1Fy-ZYkVfCWm7i9WXRXw63m6yDB_auDuPLyQ7jBm/pub)
- **Selsam finner argumentet mycket starkt att vi till slut förlorar allt om vi når kraftfull AI genom att ”odla” modellerna i stället för att konstruera dem.**
  Daniel Selsam · 2026-09-14 · kontroll, röster · [J3ljHm57yU0-27](../påståenden/2026/J3ljHm57yU0-27.yaml)
  > the argument—that if we get there by growing models rather than engineering them, we will lose everything in the end—seems very strong to me.
  > — [Personal Statement on AI Risk](https://docs.google.com/document/d/e/2PACX-1vQNl3SEX5IyA6d9qHjjFZN-qzGRZNFI6b63g-yu1Fy-ZYkVfCWm7i9WXRXw63m6yDB_auDuPLyQ7jBm/pub)

  *Förbehåll:* Selsam skriver samtidigt att han fortfarande brottas med frågan och inte har några svar.

## 2025

- **Narayanan och Kapoor menar att vi kan och bör behålla kontrollen över AI som verktyg, och att det inte kräver drastiska politiska ingrepp eller tekniska genombrott.**
  Arvind Narayanan och Sayash Kapoor · 2025-04 · kontroll, styrning · [BAL-09](../påståenden/2025/BAL-09.yaml)
  > We view AI as a tool that we can and should remain in control of, and we argue that this goal does not require drastic policy interventions or technical breakthroughs.
  > — [AI as Normal Technology](https://knightcolumbia.org/content/ai-as-normal-technology)

  *Förbehåll:* De förespråkar motståndskraft och spridd makt snarare än att bromsa, och varnar för att drastiska ingrepp kan göra saken värre om AI visar sig vara en normal teknik.

## 2024

- **Medianbedömningen bland AI-forskarna var 5 procents sannolikhet för extremt dåliga följder av avancerad AI, som att mänskligheten utrotas. Över en tredjedel (38 procent) angav minst 10 procent.**
  AI Impacts (Grace m.fl.), enkät bland 2 778 AI-forskare · 2024-01 · kontroll, röster · [FOR-13](../påståenden/2024/FOR-13.yaml)
  > The median prediction for extremely bad outcomes, such as human extinction, was 5% (mean 9%). Over a third of participants (38%) put at least a 10% chance on extremely bad outcomes.
  > — [AI Impacts: Thousands of AI Authors on the Future of AI (2024)](https://arxiv.org/abs/2401.02843)

  *Förbehåll:* Medelvärdet var 9 procent, ned från 14 procent i enkäten 2022. Beroende på hur frågan formulerades angav mellan 38 och 51 procent minst 10 procent. Återge det som forskarnas bedömning, inte som ett mått på risken.
- **När Geoffrey Hinton tog emot Nobelpriset i fysik i Stockholm 2024 varnade han i sitt bankettal för att AI kan bli ett existentiellt hot, och för att säkerheten inte prioriteras när AI byggs av företag som drivs av kortsiktiga vinster.**
  Geoffrey Hinton (Nobelpristagare i fysik 2024), bankettal i Stockholms stadshus · 2024-12-10 · röster, kontroll · [SVR-13](../påståenden/2024/SVR-13.yaml)
  > But we now have evidence that if they are created by companies motivated by short-term profits, our safety will not be the top priority.
  > — [Nobel Prize in Physics 2024](https://www.nobelprize.org/prizes/physics/2024/hinton/speech/)

  *Förbehåll:* Svensk koppling: varningen framfördes vid Nobelbanketten. Hinton nämner också kortsiktiga risker: övervakning, nätfiske, virus och autonoma vapen. Han säger att nyttan kan bli fantastisk om den fördelas rättvist.

## 2023

- **Anthropic skrev 2023 att ingen vet hur man tränar mycket kraftfulla AI-system så att de på ett robust sätt blir hjälpsamma, ärliga och ofarliga.**
  Anthropic (företagets grundsyn) · 2023-03 · kontroll, röster · [FOR-05](../påståenden/2023/FOR-05.yaml)
  > So far, no one knows how to train very powerful AI systems to be robustly helpful, honest, and harmless.
  > — [Core views on AI safety: When, why, what, and how](https://www.anthropic.com/news/core-views-on-ai-safety)

  *Förbehåll:* Samma bedömning gör OpenAI:s forskningschef 2026 (J3ljHm57yU0-12), vilket visar att problemet inte har lösts på tre år.
- **Ämnesexperterna i turneringen bedömde risken för att AI utrotar mänskligheten som mycket högre än superprognosmakarna gjorde, och ingen av grupperna lät sig övertygas av den andra.**
  Forecasting Research Institute (Existential Risk Persuasion Tournament) · 2023 · röster, kontroll · [FOR-23](../påståenden/2023/FOR-23.yaml)
  > why were superforecasters so unmoved by experts’ much higher estimates of AI extinction risk, and why were experts so unmoved by the superforecasters’ lower estimates?
  > — [Forecasting Existential Risks: Evidence from a Long-Run Forecasting Tournament – Forecasting Research Institute](https://forecastingresearch.org/xpt)

  *Förbehåll:* Jämför FOR-02, där AI-experter också gav högre sannolikheter än superprognosmakare. Superprognosmakare har bra träffsäkerhet på kortsiktiga frågor, men det är oklart hur väl det gäller för ovanliga händelser långt fram.
