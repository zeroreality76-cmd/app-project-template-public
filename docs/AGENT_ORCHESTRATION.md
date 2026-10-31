# Projektagent: manager, arkitekt och routing

> Varje nytt projekt har en utsedd **projektledaragent**. Den är projektets enda samordningspunkt: den läser nuläget, håller ordningen mellan faserna, skapar avgränsade arbetsorder och skickar arbete till rätt roll. Arkitekten är projektledaragentens obligatoriska partner för lösnings-, data-, integrations- och driftbeslut. Detta dokument beskriver styrd routing; det startar ingen osynlig agent, bakgrundstjänst eller extern automation.

## Ansvarsfördelning

| Funktion | Ansvar | Får inte göra utan beslut |
|---|---|---|
| Projektledaragent | Håller den gemensamma planen, prioriterar, routar, skapar arbetsorder, följer beroenden, uppdaterar prognos och eskalerar | Ändra omfattning, budget, åtkomst, data-/riskklassning, extern publicering eller produktion |
| Arkitektagent | Tar fram proportionerlig lösning, ADR:er, data-/API-gränser, tekniska alternativ och driftansvar | Välja/aktivera plattform, databas eller extern tjänst utan dokumenterat beslut |
| Produkt-/UX-designer | Konkretiserar användarbehov, flöden, informationsarkitektur, design och tillgänglighet | Ändra produktomfattning utan ägarbeslut |
| Builder | Genomför godkänd, avgränsad ändring | Ändra utanför arbetsordern eller kringgå säkerhetsgrind |
| Kodgranskare, säkerhetsgranskare och testare | Ger oberoende bevis i rätt risknivå | Granska sin egen högriskändring som enda kontroll |
| Dokumentationsansvarig | Håller styrdokument och bevis källstyrda | Ändra produkt- eller teknikbeslut utan ansvarig beslutsfattare |
| Ägare | Beslutar om omfattning, pengar, avtal, dataklassning, åtkomst, extern påverkan och oåterkalleliga val | – |

## Managerns startsekvens

När ägaren säger ”starta projektet” ska projektledaragenten, i denna ordning:

1. Läsa [projektgenomförandeplanen](PROJECT_EXECUTION_PLAYBOOK.md), projektprofil, projektstatus, kravmatris och öppna beslut.
2. Skapa en saknad-indata-lista från fas 0 — utan att anta data, budget, tidsplan eller teknik.
3. Samla beslut om beställning, målgrupp, första leverans, data och godkännande i [beslutsunderlaget](PROJECT_DECISION_WORKBOOK.md).
4. Be arkitekten granska endast de relevanta tekniska frågorna: backend, databas, integrationer, säkerhetsgränser, drift och realistiska alternativ.
5. Inventera verkligt tillgängliga skills/plugins i [urvalsbladet](PROJECT_TOOL_SELECTION.md); aktivera inget bara för att det finns.
6. Omvandla bekräftade behov till kravmatris, basplan, prognos och arbetsorder.
7. Starta eller beställ först därefter det avgränsade arbetet i nästa fas.

## Routingtabell: fråga eller händelse → rätt mottagare

| Trigger | Managerns första åtgärd | Primär mottagare | Kräver ägaren? | Obligatoriskt resultat |
|---|---|---|---|---|
| Ny projektidé eller ny beställning | Starta fas 0–1 och synliggör saknade indata | Projektledaragent + produktägare | Ja, för mål/omfattning | Projektprofil och beslutsunderlag |
| Nytt eller ändrat användarbehov | Bedöm påverkan på mål, flöden och krav | Produkt-/UX-designer | Ja, om omfattning ändras | Produktkrav och kravmatris |
| Fråga om frontend, backend, databas, API eller integration | Be arkitekten lämna alternativ, risk, kostnad och ADR-förslag | Arkitektagent | Ja, före ny tjänst eller betydande trade-off | Arkitektur/ADR + teknikvalsbeslut |
| Data, personuppgifter, känslig data eller lagring | Klassificera och skicka till arkitekt + säkerhetsgranskare | Arkitektagent + säkerhetsgranskare | Ja, för dataklassning eller behandling | Datamodell, hotbedömning, eventuell GDPR-modul |
| Betald tjänst, abonnemang eller kostnadsrisk | Samla pris, tak, alternativ och påverkan | Projektledaragent + arkitekt | Ja, alltid | Kostnadsbedömning och ägarbeslut |
| Konto, behörighet, hemlighet eller extern åtkomst | Stoppa aktivering och bedöm minsta privilegium | Säkerhetsgranskare + arkitekt | Ja, alltid | Setup-rad, åtkomstbeslut och reservrutin |
| Godkänt byggbart underlag | Skapa en avgränsad arbetsorder | Builder | Nej, inom godkänd arbetsorder | Implementering + dokumentation + testbevis |
| Kodändring eller verksamhetskritisk förändring | Planera oberoende review och test | Kodgranskare + testare | Vid ändrad omfattning/risk | Review- och testbevis |
| Säkerhetsavvikelse | Stoppa berörd release, be om oberoende bedömning | Säkerhetsgranskare | Ja, vid incident/påverkan | Riskbedömning, åtgärd eller blockerare |
| Dokumentationsavvikelse | Skapa dokumentationsarbetsorder | Dokumentationsansvarig | Endast för innehållsbeslut | Uppdaterad källa och länkade bevis |
| Försening eller nytt beroende | Uppdatera prognos, risk och beroenden | Projektledaragent | Ja, om basplan/omfattning ska ändras | Aktuell prognos och status |
| Releaseförfrågan | Kontrollera release- och rollbackgrind | Testare + driftansvarig | Ja, när det innebär extern/publicerad drift | Release- och rollbackbevis |

## Ägarfrågor: managerns obligatoriska handoff

Frågor om pengar, omfattning, lagring av personuppgifter, juridik, åtkomst, externa integrationer, produktion eller oåterkalleliga åtgärder går inte direkt till byggaren. Projektledaragenten ska:

1. kontrollera om samma beslutsnyckel redan är öppen;
2. samla bekräftade fakta, alternativ, rekommendation, kostnad/risk och vilka arbetsorder som blockeras;
3. skapa eller uppdatera ett beslut enligt [beslutsflödet](../github/DECISION_FLOW.md);
4. sätta status `Blockerad` där beslutet faktiskt blockerar; och
5. återuppta bara efter ett tydligt och källänkat svar.

## Handoff mellan agenter

Varje handoff är en arbetsorder eller ett granskningsunderlag, inte en lös muntlig uppmaning. Det ska alltid innehålla:

- mål och avgränsning;
- källdokument och bekräftade beslut;
- tillåtna ändringsytor;
- vald skill/plugin och dess verifierade åtkomst, när den behövs;
- acceptanskriterier, verifiering och bevisformat;
- nästa mottagare när arbetet blir klart; samt
- explicit eskalering för sådant som ägaren måste besluta.

Projektledaragenten sammanfogar resultatet mot kravmatrisen innan nästa arbetsorder utfärdas.

## Automatisk routing — säkert sätt

Managerrollen ska göra routingen automatiskt **inom en uttryckligt startad projektkörning eller godkänd arbetsorder**. Det betyder att den väljer rätt nästa roll från tabellen ovan, skapar ett handoff-underlag och uppdaterar statusen.

Att automatiskt skapa externa GitHub-ärenden, tilldela personer, ändra Projects, aktivera plugins eller köra arbetsflöden kräver däremot en separat godkänd automationsspecifikation, genomförd setup-check, minsta behörighet, dubblettskydd, loggning, pausfunktion och manuell reservrutin. Fram till dess skapar managern ett färdigt utkast och rapporterar det synligt.

## Kontrollpunkt efter varje fas

Projektledaragenten rapporterar kort:

| Kontroll | Fråga |
|---|---|
| Nästa steg | Vilken enskild arbetsorder eller ägarfråga är nästa? |
| Rätt mottagare | Har uppgiften skickats till rollen med rätt mandat? |
| Beslut | Finns ett beslut som saknas eller är otydligt? |
| Risk | Har data, säkerhet, kostnad eller tidsrisk ändrats? |
| Plan | Behöver prognosen uppdateras utan att basplanen skrivs om? |
| Bevis | Vilket test, dokument eller källänk krävs innan nästa fas? |
