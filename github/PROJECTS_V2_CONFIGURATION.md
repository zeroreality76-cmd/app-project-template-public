# Projects V2-konfiguration

## Ägare och förutsättningar

- **Ägare:** `[[VERIFIERAD GITHUB-ANVÄNDARE ELLER ORGANISATION]]`
- **Projekt:** `[[NAMN OCH ID EFTER SKAPANDE]]`
- **Behörighet:** verifiera separat för Projects V2, fält, views och automationer.
- **Abonnemangsgränser:** verifiera auto-add-kvot före aktivering.

## Fält

| Fält | Typ | Värden/syfte | Källa |
|---|---|---|---|
| Status | Single select | Planerat, Redo, Pågående, Blockerat, Granskning, Klart | Operativ status |
| Prioritet | Single select | P0, P1, P2, P3 | Issue |
| Milestone | Milestone | Leveransmål | GitHub milestone |
| Beroenden | Text | Länkade issue-ID:n | Plan/issue |
| Prognosdatum | Date | Aktuell prognos, aldrig basdatum | Prognos |
| Beslut krävs | Single select | Ja/Nej | Beslutslogg |
| Tidsrisk | Single select | Låg/Medel/Hög | Prognos |

## Vyer

| Vy | Filter/gruppering | Syfte |
|---|---|---|
| Operativ tavla | Gruppera Status | Planerat till klart |
| Ägarbeslut | `type:owner-decision` eller Beslut krävs=Ja | Synliga blockerare |
| Aktuell milestone | Filtrera aktiv milestone | Nästa leverans |
| Tidsrisk | Filtrera risk Medel/Hög | Prognosuppföljning |
| Granskning | Status=Granskning | Kvalitetskö |

## Konfigurationsregel

Bygg om idempotent: läs befintligt projekt och fält först, skapa saknade objekt, uppdatera endast avvikande värden och skriv resultat till ett revisionsspår. Projects V2 kan konfigureras via GitHubs GraphQL API, men det här paketet exekverar inte den åtgärden.
