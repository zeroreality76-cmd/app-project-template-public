# Projektstart: beslutsunderlag

> Fyll i detta tillsammans med [projektprofilen](PROJECT_PROFILE.md) innan arbete beställs eller arkitektur väljs. Skriv aldrig hemligheter, personnummer, API-nycklar eller råa kunduppgifter här. Ett obesvarat val som påverkar omfattning, kostnad, data eller säkerhet ska markeras `[[BESLUT KRÄVS]]` och föras in i [beslutsloggen](DECISION_LOG.md).

## Så används underlaget

1. Beskriv först vilket resultat som ska uppnås och för vem.
2. Svara på frågorna i ordning. Välj `Ej aktuell` när frågan inte gäller projektet; gissa inte.
3. Skapa en ägarfråga när beslutet ligger utanför godkänt mandat.
4. För över godkända krav till [produktkraven](product/PRODUCT_REQUIREMENTS.md), tekniska beslut till [ADR](architecture/ADR/ADR-000-template.md) och varje verifierbar leverans till [kravmatrisen](REQUIREMENTS_MATRIX.md).
5. Starta byggarbete först när startgrinden längst ned är passerad.

Använd `Beslutad`, `Ej aktuell` eller `[[BESLUT KRÄVS]]` i kolumnen **Beslutsläge**. Projektets övergripande status hanteras separat i [projektstatus](PROJECT_STATE.md).

## 1. Beställning, mål och omfattning

| Fråga | Svar/beslut | Beslutsläge | Ägare | Bevis eller nästa steg |
|---|---|---|---|---|
| Vad ska produkten göra i en mening? | `[[UTFALL, INTE LÖSNING]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Vilket problem, för vilken målgrupp och i vilken situation? | `[[...]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Vilka 1–3 användarresultat avgör om första leveransen lyckas? | `[[MÄTBARA UTFALL]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Vad ska uttryckligen inte byggas nu? | `[[ICKE-MÅL]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Vilken konkret första leverans beställs? | `[[FUNKTIONER/FLÖDEN/UNDERLAG]]` | `[[...]]` | `[[...]]` | [Produktkrav](product/PRODUCT_REQUIREMENTS.md) |
| Vilka acceptanskriterier måste vara uppfyllda för att den ska accepteras? | `[[OBSERVERBARA KRITERIER]]` | `[[...]]` | `[[...]]` | [Kravmatris](REQUIREMENTS_MATRIX.md) |

## 2. Användare, roller och flöden

| Fråga | Svar/beslut | Beslutsläge | Ägare | Bevis eller nästa steg |
|---|---|---|---|---|
| Vilka använder produkten och vilken behörighet behöver varje roll? | `[[ROLLER OCH ÅTKOMST]]` | `[[...]]` | `[[...]]` | [Användarflöden](product/USER_FLOWS.md) |
| Krävs konto, inloggning eller administration? | `[[JA/NEJ + VARFÖR]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Vilket är det viktigaste flödet från start till färdigt resultat? | `[[STEG OCH FELVÄGAR]]` | `[[...]]` | `[[...]]` | [Användarflöden](product/USER_FLOWS.md) |
| Vilka tillgänglighetskrav, språk eller enheter är viktiga? | `[[...]]` | `[[...]]` | `[[...]]` | [Tillgänglighetsgranskning](product/ACCESSIBILITY_REVIEW.md) |

## 3. Data, innehåll och integritet

| Fråga | Svar/beslut | Beslutsläge | Ägare | Bevis eller nästa steg |
|---|---|---|---|---|
| Vilken information måste finnas för att flödet ska fungera? | `[[DATATYPER OCH SYFTE]]` | `[[...]]` | `[[...]]` | [Datamodell](architecture/DATA_MODEL.md) |
| Var kommer varje uppgift ifrån: användare, intern källa, partner eller offentlig källa? | `[[KÄLLOR OCH RÄTTIGHETER]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Behövs lagring, sökning, historik, export eller radering? | `[[JA/NEJ + KRAV]]` | `[[...]]` | `[[...]]` | [Datamodell](architecture/DATA_MODEL.md) |
| Förekommer personuppgifter, känsliga uppgifter, betaluppgifter eller annan reglerad data? | `[[JA/NEJ + KLASSNING]]` | `[[...]]` | `[[...]]` | [EU-/GDPR-modul](security/EU_GDPR_MODULE.md) |
| Vilka får läsa, skapa, ändra och radera information? | `[[ÅTKOMSTREGLER]]` | `[[...]]` | `[[...]]` | [Säkerhetsbas](security/SECURITY_BASELINE.md) |
| Hur länge behövs informationen och hur ska den tas bort eller återställas? | `[[LAGRING/RADERING/BACKUP]]` | `[[...]]` | `[[...]]` | `[[...]]` |

## 4. Lösning: gränssnitt, backend och integrationer

| Fråga | Svar/beslut | Beslutsläge | Ägare | Bevis eller nästa steg |
|---|---|---|---|---|
| Behövs ett webbaserat gränssnitt, API, mobilapp eller en kombination? | `[[...]]` | `[[...]]` | `[[...]]` | [Blueprint](product/BLUEPRINT.md) |
| Behövs backend? Svara ja endast om serverlogik, privat data, behörighet, integration eller schemalagd behandling krävs. | `[[JA/NEJ + MOTIVERING]]` | `[[...]]` | `[[...]]` | [Arkitektur](architecture/ARCHITECTURE.md) |
| Behövs databas? Vilka krav motiverar den? | `[[JA/NEJ + MOTIVERING]]` | `[[...]]` | `[[...]]` | [Datamodell](architecture/DATA_MODEL.md) |
| Behövs externa tjänster, exempelvis betalning, e-post, AI, analys eller identitet? | `[[INGEN ELLER TJÄNSTER + ÄNDAMÅL]]` | `[[...]]` | `[[...]]` | [Integrationer](architecture/INTEGRATIONS.md) |
| Vilket är det enklaste säkra alternativet om en tjänst inte godkänns? | `[[ALTERNATIV]]` | `[[...]]` | `[[...]]` | [Teknikvalsbeslut](architecture/TECHNOLOGY_SELECTION.md) |
| Vilka fel måste användaren förstå och vilka fel ska endast loggas? | `[[FELVÄGAR OCH LARM]]` | `[[...]]` | `[[...]]` | [Hotbedömning](security/THREAT_ASSESSMENT.md) |

## 5. Säkerhet, drift och kostnad

| Fråga | Svar/beslut | Beslutsläge | Ägare | Bevis eller nästa steg |
|---|---|---|---|---|
| Vilka är de största riskerna för användare, data, leverans och kostnad? | `[[RISKER]]` | `[[...]]` | `[[...]]` | [Hotbedömning](security/THREAT_ASSESSMENT.md) |
| Vilka miljöer behövs: lokal, test, produktion? | `[[...]]` | `[[...]]` | `[[...]]` | [Setup-check](operations/SETUP_CHECK.md) |
| Vem ansvarar för åtkomst, hemligheter, backup, larm och återställning? | `[[ROLLER]]` | `[[...]]` | `[[...]]` | [Driftrunbook](operations/OPERATIONS_RUNBOOK.md) |
| Vilket månadstak, kostnadsstopp och vilken budgetägare gäller? | `[[BELOPP OCH GRÄNSER]]` | `[[...]]` | `[[...]]` | [Kostnadsbedömning](operations/COST_DECISION.md) |
| Vilka kostnader eller åtaganden kräver separat ägarbeslut före aktivering? | `[[...]]` | `[[...]]` | `[[...]]` | [Beslutslogg](DECISION_LOG.md) |

## 6. Leverans, test och godkännande

| Fråga | Svar/beslut | Beslutsläge | Ägare | Bevis eller nästa steg |
|---|---|---|---|---|
| När ska första leveransen vara möjlig att granska? | `[[DATUM/MILESTONE]]` | `[[...]]` | `[[...]]` | [Basplan](BASELINE_PLAN.md) |
| Hur ska funktion, säkerhet och tillgänglighet testas? | `[[TESTNIVÅER OCH ÄGARE]]` | `[[...]]` | `[[...]]` | [Teststrategi](operations/TEST_STRATEGY.md) |
| Vem godkänner respektive produkt-, teknik-, säkerhets- och kostnadsbeslut? | `[[NAMN/ROLL]]` | `[[...]]` | `[[...]]` | `[[...]]` |
| Vilket bevis krävs före release och hur återställs en misslyckad release? | `[[BEVIS OCH ROLLBACK]]` | `[[...]]` | `[[...]]` | [Releasechecklista](operations/RELEASE_CHECKLIST.md) |

## Startgrind före byggarbete

Byggarbete får börja när varje relevant rad är `Beslutad` eller `Ej aktuell`, och följande finns dokumenterat:

- tydlig första leverans, avgränsning och acceptanskriterier;
- utsedd produktägare och beslutsägare;
- datakällor, dataklassning och åtkomstregler;
- beslut om backend, datalagring och externa integrationer;
- kostnadstak, driftansvar och testmetod; samt
- öppna ägarfrågor i beslutsloggen, utan att de döljs som antaganden.

Om ett saknat beslut kan ändra omfattning, säkerhet, juridik, kostnad eller release ska arbetet vara blockerat i [projektstatus](PROJECT_STATE.md) tills beslutet finns.
