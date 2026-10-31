# Projektstart: urval av skills, plugins och verktyg

> Fyll i i fas 3 av [projektgenomförandeplanen](PROJECT_EXECUTION_PLAYBOOK.md). En skill eller plugin används först när den är tillgänglig i den aktuella arbetsmiljön och dess instruktioner, behörighet och risk har granskats. Kopiera inte hemligheter, tokens eller hela externa instruktioner till detta dokument.

## Arbetsgång för urval

1. Inventera vilka skills, plugins, anslutningar och lokala verktyg som faktiskt är tillgängliga i den miljö där projektet ska utföras.
2. Läs hela instruktionen för varje kandidat som bedöms relevant. Notera namn, version/källa, uppgift och begränsningar.
3. Välj minsta nödvändiga uppsättning utifrån bekräftade krav — inte utifrån vad som råkar vara installerat.
4. Bedöm dataåtkomst, behörighet, kostnad, extern påverkan, fallback och test innan en plugin eller anslutning aktiveras.
5. Skriv endast de valda verktygen i respektive arbetsorder. Oanvända kandidater får inte aktiveras ”för säkerhets skull”.

## Inventering av tillgänglig miljö

| Typ | Namn/version eller källa | Kan användas för | Behörighet/dataåtkomst | Verifierad? | Kommentar |
|---|---|---|---|---|---|
| Skill | `[[NAMN + VERSION]]` | `[[UPPGIFT]]` | `[[LÄS/SKRIV/EXTERN]]` | `[[JA/NEJ]]` | `[[...]]` |
| Plugin/anslutning | `[[NAMN + VERSION]]` | `[[UPPGIFT]]` | `[[KONTO/SCOPES]]` | `[[JA/NEJ]]` | `[[...]]` |
| Lokalt verktyg | `[[NAMN + VERSION]]` | `[[UPPGIFT]]` | `[[LOKAL ÅTKOMST]]` | `[[JA/NEJ]]` | `[[...]]` |

## Val per behov

| Bekräftat behov | Kandidat | Varför passar den? | Risk/kostnad/behörighet | Val: använd/inte använd/blockerad | Fallback | Arbetsorder eller bevis |
|---|---|---|---|---|---|---|
| Produkt- eller kravarbete | `[[SKILL/VERKTYG]]` | `[[...]]` | `[[...]]` | `[[...]]` | Manuell kravgranskning | `[[LÄNK]]` |
| UX, tillgänglighet eller design | `[[SKILL/VERKTYG]]` | `[[...]]` | `[[...]]` | `[[...]]` | Manuell designgranskning | `[[LÄNK]]` |
| Arkitektur, data eller API | `[[SKILL/VERKTYG]]` | `[[...]]` | `[[...]]` | `[[...]]` | ADR + manuell granskning | `[[LÄNK]]` |
| Kod, kodgranskning eller säkerhet | `[[SKILL/VERKTYG]]` | `[[...]]` | `[[...]]` | `[[...]]` | Oberoende granskning/test | `[[LÄNK]]` |
| Test, release eller drift | `[[SKILL/VERKTYG]]` | `[[...]]` | `[[...]]` | `[[...]]` | Lokal/scenariobaserad kontroll | `[[LÄNK]]` |
| Extern integration eller automation | `[[SKILL/PLUGIN]]` | `[[...]]` | `[[DATA, KOSTNAD, SCOPES]]` | `[[...]]` | Manuell reservrutin | `[[LÄNK]]` |

## Obligatorisk kontroll för plugins och anslutningar

| Kontroll | Fråga | Resultat/bevis |
|---|---|---|
| Behov | Vilket godkänt krav kan inte lösas lika säkert utan detta? | `[[...]]` |
| Instruktion | Har hela instruktionen för skillen/pluginen lästs och förståtts? | `[[LÄNK/REFERENS]]` |
| Behörighet | Är minsta möjliga scope/konto tillräckligt? | `[[...]]` |
| Data | Vilken data lämnar miljön, vart och under vilken rättslig grund? | `[[...]]` |
| Kostnad | Finns pris, kostnadstak och budgetägare? | `[[...]]` |
| Säkerhet | Finns hotbedömning, loggning och hemlighetshantering? | `[[...]]` |
| Test | Kan funktionen bevisas med en ofarlig kontroll? | `[[...]]` |
| Reservrutin | Vad händer om tjänsten saknas, är felkonfigurerad eller fallerar? | `[[...]]` |
| Beslut | Vem godkänner aktivering? | `[[...]]` |

## Standardregel för vanliga behov

Använd [verktygsmatrisen](TOOL_MATRIX.md) som utgångspunkt, men välj alltid efter behov. Vanliga matchningar är dokumentationsskill för källdokument, arkitektur-/systemdesignskill för lösningsunderlag, test-/releasechecklisteskill för verifiering och säkerhetsgranskning för känslig data eller åtkomst. Den exakta listan varierar mellan arbetsmiljöer; ett namn i denna mall är inte ett krav och en installerad plugin är inte automatiskt godkänd.

## Slutligt urval

| Valda skills och verktyg | Ej valda kandidater | Blockerade val och ägarfråga | Nästa kontroll före användning |
|---|---|---|---|
| `[[...]]` | `[[...]]` | `[[...]]` | `[[...]]` |
