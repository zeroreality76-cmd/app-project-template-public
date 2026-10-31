# Automationsspecifikation: [[ID OCH NAMN]]

## Syfte och utlösare

- **Syfte:** `[[VILKET RESULTAT UTAN ONÖDIG AUTOMATION]]`
- **Utlösare:** `[[EVENT/MANUELL/SCHEMALAGD]]`
- **Indata och källa:** `[[EVENTFÄLT/DOKUMENT/API]]`
- **Förutsättningar:** `[[SETUP, FEATURE FLAGG, TESTDATA]]`

## Utförande och kontroll

| Fält | Värde |
|---|---|
| Åtgärd och resultat | `[[VAD SKER OCH VILKET ARTEFAKT SKAPAS]]` |
| Ansvarig | `[[ROLL]]` |
| Minsta behörighet | `[[RÄTTIGHET]]` |
| Hemlighetshantering | `[[ENDAST NAMN, KÄLLA OCH ROTATION]]` |
| Dubblettskydd/idempotens | `[[NYCKEL, FÖRSÖK FÖRST LÄSA]]` |
| Samtidighet | `[[GRUPP, KÖ/AVBRYT-REGEL]]` |
| Återförsök och timeout | `[[GRÄNS OCH BACKOFF]]` |
| Loopskydd | `[[HÄNDELSEFILTER/ORIGIN]]` |
| Loggning och revisionsspår | `[[VAD, VAR, LAGRINGSTID]]` |
| Notifiering | `[[VEM, VAD SOM ÄR MENINGSFULLT]]` |
| Pausfunktion | `[[HUR AVAKTIVERA]]` |
| Manuell reservrutin | `[[STEG OCH ÄGARE]]` |
| Test | `[[TESTMILJÖ, FALL, FÖRVÄNTAT RESULTAT]]` |
| Kostnadsgräns | `[[TAK/LARM/ÄGARE]]` |

**Status:** Förberedd | Verifierad | Blockerad
