# Automationsregister

Alla poster är **inaktiva** tills setup-check och respektive aktiveringsvillkor är godkända.

| ID | Syfte/utlösare | Förutsättningar och behörighet | Skydd | Resultat/notifiering | Test och reservrutin | Status |
|---|---|---|---|---|---|---|
| AUT-01 | Kvalitetsgrind vid PR eller manuell start | Verifierad runtime, minsta `contents: read`/`pull-requests: read` | Concurrency per PR, avbryt äldre köade körning | Check-resultat, inga externa ändringar | Test-PR; kör kontroller lokalt | Inaktiv |
| AUT-02 | Dokumentationskontroll vid PR eller manuell start | Python 3.11, repositoryinnehåll | Endast läsning, exitkod per avvikelse | Check-resultat med saknade dokument | Ändra testfil; kör verifierare lokalt | Inaktiv |
| AUT-03 | Beslutsärende vid mandatblockering | Verifierad issue- och assignee-behörighet | Stabil beslutsnyckel och sökning före skapande | Ett issue eller utkast, aldrig tyst godkännande | Testrepo; använd manuellt issueutkast | Inaktiv |
| AUT-04 | Projects-status efter verifierat issue-event | Verifierad Projects V2-behörighet och fält-ID | Event-ID/revisionslogg, serialisering per item | Statusuppdatering eller synligt fel | Testrepo; manuell Projects-uppdatering | Inaktiv |
| AUT-05 | Managerstyrd routing efter en uttryckligt godkänd trigger | Verifierad roll-/ärendeåtkomst, routingmodell och ägarkontakt | Stabil uppgiftsnyckel, idempotens, mänsklig paus och inga oberoende bakgrundskörningar | Arbetsorder/utkast till rätt roll eller synligt blockerarfel | Testrepo; manager skapar handoff manuellt | Inaktiv |

Varje faktisk implementation ska ha en egen ifylld [automationsspecifikation](AUTOMATION_SPEC_TEMPLATE.md). AI-baserade körningar följer dessutom [AI-policyn](AI_RUN_POLICY.md); ingen förutsätter en öppen chatt eller en osynlig bakgrundstjänst.
