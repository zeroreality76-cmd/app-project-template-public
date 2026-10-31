# Policy för AI-körningar

## Tillåtna initieringar

En AI-körning startas endast genom en tydlig manuell begäran, en godkänd arbetsorder eller en senare verifierad eventintegration. Ingen öppen chatt, tidsstyrning eller bakgrundstjänst antas vara en självgående agent.

## Obligatorisk kontext

Körningen får: projektprofil, aktuell status, relevant arbetsorder, berörda krav/ADR:er, mandat, filer inom tillåten ändringsyta och verifieringskrav. Den får inte ges hemligheter eller bredare åtkomst än uppgiften behöver.

## Mandat och stopp

AI får analysera, föreslå, skapa lokala underlag och köra godkända ofarliga kontroller. Den stoppar och skapar en beslutspost vid ändrad omfattning, budget, extern publicering, produktion, ny betaltjänst, åtkomständring, person-/känslig data eller oåterkallelig åtgärd.

## Kostnad och granskning

Varje framtida AI-automation ska ha modell, maximal körfrekvens, token-/kostnadstak, timeout, loggning och mänsklig granskningspunkt i sin automationsspecifikation. Resultat får inte ensamt ändra externa system utan den uttryckligen godkända behörighet som specen beskriver.

## Managerstyrd routing

En manageragent får inom en manuellt startad körning läsa aktuell status och routingmodell, välja nästa roll, skapa lokala arbetsorder och sammanställa ett ägarbeslutsutkast. Den får inte självständigt börja en bakgrundskörning, tilldela externa konton, skapa externa ärenden eller kringgå en blockerad ägarfråga. Sådan extern routing är en framtida, inaktiv automation och kräver AUT-05:s villkor.
