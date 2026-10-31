# Projektgenomförande: ordning från start till release

> Detta är den styrande arbetsgången när ett nytt projekt skapas från mallen. Följ faserna i ordning. Hoppa inte till implementation för att en lösning eller plugin råkar vara tillgänglig. Om ett startvillkor saknas: skapa en ägarfråga och markera arbetet blockerat.

## Första regeln

Det första arbetet är alltid att förstå och planera uppdraget — inte att välja teknik, installera något eller skriva kod. Projektledaren skapar inga arbetsorder för byggarbete förrän faserna 0–3 är klara för den första leveransen.

## Faser och grindar

| Ordning | Fas | Gör detta | Leverans | Startvillkor | Klar när |
|---|---|---|---|---|---|
| 0 | Mottagning och inventering | Bekräfta uppdrag, ägare, tid, budgetram och tillgängliga underlag. Be om saknade fakta utan att gissa. | Ifylld [projektprofil](PROJECT_PROFILE.md) och lista över saknade indata | Nytt projekt eller nytt uppdrag | Beslutsägare och första mål är identifierade |
| 1 | Beställning och beslut | Fyll i [beslutsunderlaget](PROJECT_DECISION_WORKBOOK.md): vad som ska byggas, för vem, vilken data som behövs och vad första leveransen ska bevisa. | Beslut, avgränsning, icke-mål och öppna ägarfrågor | Fas 0 klar | Varje relevant beslut är `Beslutad`, `Ej aktuell` eller eskalerat |
| 2 | Plan och krav | Gör behov till produktkrav, kravmatris, basplan och realistisk prognos. Identifiera beroenden och risker. | Första plan, prioriterad kravlista och beslut om första milestone | Fas 1 klar | Första leveransen har ägare, acceptanskriterier och verifiering |
| 3 | Skill-/plugin- och verktygsval | Inventera den aktuella miljön och välj minsta uppsättning relevanta skills, verktyg och eventuella plugins enligt [urvalsbladet](PROJECT_TOOL_SELECTION.md). | Ifyllt urvalsblad och beslutad reservrutin | Fas 2 klar | Varje valt verktyg har behov, behörighet, kostnad, säkerhet och fallback dokumenterad |
| 4 | Lösningsdesign | Skapa användarflöden, blueprint, arkitektur, datamodell, API-kontrakt, ADR:er och hotbedömning i den omfattning kraven kräver. | Byggbart och granskat lösningsunderlag | Fas 3 klar | Teknik- och databeslut är spårbara och ingen högriskfråga är dold |
| 5 | Setup och arbetsorder | Genomför relevanta delar av setup-checken, dela upp arbetet och skapa en avgränsad [arbetsorder](WORK_ORDER_TEMPLATE.md) per ändringsyta. | Verifierad eller blockerad setup, arbetsorder och ansvar | Fas 4 klar | Varje arbetsorder har tillåtna ändringar, test och eskalering |
| 6 | Bygg och dokumentera | Utför en arbetsorder i taget. Uppdatera krav, kontrakt, bevis och prognos i samma flöde. | Testbar förändring med dokumentation | Fas 5 klar | Acceptanskriterier är uppfyllda med bevis |
| 7 | Oberoende granskning och test | Låt rätt oberoende roll granska kod, säkerhet eller test enligt risknivå. Rätta eller öppna tydliga avvikelser. | Gransknings- och testbevis | Fas 6 klar | Definitionen av klart är uppfylld, inte enbart en mergad PR |
| 8 | Release och uppföljning | Använd releasechecklistan, säkra rollbackbevis och uppdatera drift-/incidentunderlag. | Godkänd eller blockerad release | Fas 7 klar | Release- och återställningsbevis är dokumenterade |

## Indata som ska begäras i fas 0

Fråga bara efter sådant som behövs för att kunna gå vidare. Markera frånvaron synligt i stället för att fylla i påhittade svar.

| Område | Minsta underlag | Om det saknas |
|---|---|---|
| Ägarskap | Produktägare, beslutsägare och kontaktväg | Skapa ägarfråga; starta inte irreversibla eller kostnadsdrivande val |
| Beställning | Problem, målgrupp, önskat resultat och första leverans | Använd beslutsunderlagets avsnitt 1 |
| Innehåll | Funktioner, texter, varumärkesmaterial, data eller källor som beställaren äger rättigheterna till | Dokumentera källa och rättighet; använd inte skyddat eller personligt material utan beslut |
| Data | Vilken data som behövs, källa, klassning och åtkomst | Blockera data-/backendbeslut som saknar klassning |
| Ekonomi | Budgetägare, kostnadstak och godkännande för betalda tjänster | Använd endast kostnadsfria, lokala underlag tills beslut finns |
| Tid och kapacitet | Önskad första granskningspunkt, beroenden och tillgängliga personer | Sätt osäker prognos, inte ett påhittat leveransdatum |
| Konton och åtkomst | Vilka system som redan finns och vilken minsta åtkomst som kan testas | Notera som förberett/blockerat; dela aldrig hemligheter i projektfiler |

## Hur ChatGPT/Codex startar ett nytt projekt

1. Läs [Börja här](START_HERE.md), projektprofil, projektstatus, kravmatris och denna genomförandeplan.
2. Sammanfatta bara bekräftade fakta, saknade indata och beslut som krävs från ägaren.
3. Fyll inte i teknik, kostnad, data eller tid på antagande. Använd `[[BESLUT KRÄVS]]` och beslutsloggen.
4. Gör faserna 0–3 till konkreta punkter i basplanen och uppdatera status med nästa minsta steg.
5. Skapa först därefter arbetsorder för design, arkitektur, implementation eller test.
6. När ett beroende försenas: ändra [aktuell prognos](CURRENT_FORECAST.md), inte godkänd omfattning eller basplan i tysthet.

## Regler för parallellt arbete

- En ägare per kodyta eller dokumentyta.
- Projektprofil, kravmatris, basplan, prognos och beslutslogg ändras aldrig parallellt av flera roller.
- Oberoende granskning krävs för säkerhetsgränser, hemligheter, åtkomst, högriskdata, verksamhetskritisk kod och release.
- En ny skill, plugin eller extern tjänst är aldrig en genväg runt en obesvarad produkt-, data-, budget- eller säkerhetsfråga.

## Startgrind för första arbetsorder

Innan fas 5 får börja ska följande vara bevisat eller synligt blockerat:

- första leveransen, dess icke-mål och acceptanskriterier;
- relevant data, klassning, åtkomst och källrättighet;
- beslut om backend, datalagring och integrationer;
- skill-/plugin-urval med minsta behörighet och reservrutin;
- budgetgräns, ägare och prognos; samt
- en arbetsorder med tillåtna ändringar, verifiering och eskalering.

Se [definitionen av klart](DEFINITION_OF_DONE.md) för vad som krävs före färdigmarkering eller release.
