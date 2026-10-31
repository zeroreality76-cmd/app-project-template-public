# Neutralt B2B-webb/SaaS-scenario

Scenario: ett litet team bygger en portal där kundorganisationer administrerar serviceärenden. Konton, ärenden och en valfri extern notifieringsintegration ingår endast som testunderlag, inte som mallkrav.

| Nr | Händelse | Förväntat mallbeteende | Verifieringsnivå |
|---|---|---|---|
| 1 | Nytt projekt startar | Profil, läsordning, basplan, kravmatris och GitHub-underlag fylls i rätt ordning | Scenariogenomgång |
| 2 | Ägaren måste välja notifieringsleverantör | Dubblettskyddat beslutissue eller färdigt utkast, blockerad status och källänkar | Scenariogenomgång |
| 3 | Beroende försenas | Aktuell prognos och beroenden ändras, basplanen bevaras | Scenariogenomgång |
| 4 | Kodändring för ärendeflöde | Arbetsorder, relevanta tester, oberoende granskning och dokumentuppdatering krävs | Scenariogenomgång |
| 5 | Automationsfel uppstår | Fel syns, kan återförsökas utan dubblett och har manuell reservrutin | Scenariogenomgång |
| 6 | Ny person ansluter | Startguide leder till mål, beslut, status och nästa steg utan chatthistorik | Statisk granskning |
| 7 | Release föreslås | Releasechecklista, testbevis och rollbackplan måste vara klara | Scenariogenomgång |
| 8 | Mallversion uppdateras | Projektets egna beslut bevaras och konflikt granskas | Scenariogenomgång |

Ett framtida privat testrepository kan höja relevanta rader till faktiskt kört integrationstest efter uttryckligt mandat.
