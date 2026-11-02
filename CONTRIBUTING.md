# Bidra till mallen

Tack för att du vill förbättra mallen. Målet är att den ska vara tydlig, återanvändbar och säker för verkliga webb-/SaaS-projekt.

## Innan du föreslår en ändring

1. Läs [Börja här](docs/START_HERE.md), [kravmatrisen](docs/REQUIREMENTS_MATRIX.md) och relevant rollinstruktion i `agents/roles/`.
2. Beskriv behovet, vilka dokument som påverkas och hur förbättringen kan verifieras.
3. Håll ändringen liten och avgränsad. Förändra inte mallens godkända principer eller licens utan ett separat beslut.
4. Lägg aldrig in hemligheter, personuppgifter, kunddata eller otestade aktiva automationer.

## Kvalitetskrav för pull requests

- Uppdatera berörd dokumentation och kravmatris i samma ändring.
- Kör `python3.11 tools/verify_template.py`.
- Beskriv verifieringsnivå: statisk granskning, scenariogenomgång eller faktiskt kört integrationstest.
- Säkerhets-, åtkomst- och högriskförändringar ska oberoende granskas.

## Språk och stil

Mallen är i första hand svenskspråkig. Skriv konkret, teknikneutralt och källstyrt. Påstå inte att en integration, plugin eller automation fungerar utan ett verifierat bevis.
