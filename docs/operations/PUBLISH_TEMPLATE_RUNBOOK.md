# Runbook: publicera GitHub-template

Detta är en generell runbook för en senare publicering eller ny utgåva.

1. Begär uttryckligt mandat för extern publicering, inklusive rätt GitHub-ägare, repositorynamn och synlighet.
2. Kontrollera att repositoryt inte redan finns och att ägaren har administratörsbehörighet.
3. Kör lokal verifierare och granska att inga hemligheter, kunddata eller oavsiktliga aktiva workflows ingår.
4. Skapa repositoryt med beslutad synlighet, publicera paketet och verifiera filerna via GitHubs UI eller API.
5. Markera repositoryt som template med administratörsbehörighet och kontrollera att template-statusen visas.
6. Skapa ett separat testrepository från templaten och kör setup-check samt lokal verifierare där.
7. Dokumentera testresultat och eventuella avvikelser; radera inget testrepository utan separat beslut.

GitHubs template-markering och Projects-/workflowbehörigheter ska verifieras mot aktuell dokumentation och det verkliga kontot vid genomförandet.
