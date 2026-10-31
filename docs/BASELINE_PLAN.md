# Basplan

Basplanen fastställs av beslutsägaren och ändras endast genom ett dokumenterat beslut.

Använd [projektgenomförandeplanen](PROJECT_EXECUTION_PLAYBOOK.md) för fasernas faktiska ordning och grindar. Raderna nedan blir den godkända tids- och ansvarsversionen för det specifika projektet.

| Fas/milestone | Mål | Leverans | Beroenden | Ansvar | Arbetsinsats | Basdatum | Startvillkor | Slutvillkor |
|---|---|---|---|---|---|---|---|---|
| 0. Initiering | Godkänd riktning | Profil, beslutsunderlag, verktygsurval, krav och riskbild | – | Projektledare | `[[ESTIMAT]]` | `[[DATUM]]` | Profil ifylld | Startgrind för första arbetsorder passerad |
| 1. Blueprint | Byggbar lösning | UX, ADR:er, kontrakt | Fas 0 | Arkitekt/designer | `[[ESTIMAT]]` | `[[DATUM]]` | Mål låsta | Beslut dokumenterade |
| 2. Leverans | Testbar produkt | Kod, tester, dokumentation | Fas 1 | Builder | `[[ESTIMAT]]` | `[[DATUM]]` | Arbetsorder redo | Acceptans bevisad |
| 3. Release | Säker leverans | Release- och rollbackbevis | Fas 2 | Drift/test | `[[ESTIMAT]]` | `[[DATUM]]` | Checklista klar | Produktionskontroll klar |
