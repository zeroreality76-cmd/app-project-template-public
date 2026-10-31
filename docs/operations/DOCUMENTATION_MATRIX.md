# Dokumentationsmatris

| Förändring | Uppdatera | Metod | Ansvarig | Kontroll |
|---|---|---|---|---|
| Mål, omfattning eller målgrupp | Projektprofil, produktkrav, kravmatris, basplan/prognos | Ändra källdokument och länka beslut | Produktägare/projektledare | Kravmatris + beslutslogg |
| Ny eller ändrad beställning, data-/backendval eller leveranskrav | Projektstart: beslutsunderlag, projektprofil, produktkrav, arkitektur och kravmatris | Fatta eller eskalera beslut innan byggarbete; länka beslutet | Produktägare/arkitekt | Startgrind + beslutslogg |
| Arkitektur, API eller data | Blueprint, arkitektur, ADR, data-/API-kontrakt, hotbedömning | Uppdatera före implementation | Arkitekt | Oberoende granskning |
| Kodändring | Kravmatris, testbevis, berörda kontrakt/runbooks | Samma PR/arbetsorder | Builder/dokumentationsansvarig | PR-checklista |
| Ny integration | Teknikval, integrationsregister, kostnad, säkerhet, drift | Beslut före aktivering | Arkitekt/säkerhetsgranskare | Setup-check |
| Drift- eller releaseändring | Release-, rollback- och incidentunderlag | Före release | Driftansvarig | Releasechecklista |
| Förändrad prognos | Aktuell prognos, status och beroendeärenden | Ändra prognos, aldrig basplan tyst | Projektledare | Milestonegranskning |

Saknad, motsägelsefull eller föråldrad obligatorisk dokumentation blockerar berörd färdigmarkering eller skapar ett dokumentationsärende.
