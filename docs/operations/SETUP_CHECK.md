# Installationskontroll

Varje kontroll markeras `förberedd`, `verifierad` eller `blockerad`. En ansluten tjänst är inte verifierad förrän metoden nedan har godkänts.

| Område | Kontroll | Metod | Godkänt resultat | Status/bevis |
|---|---|---|---|---|
| Repository | Rätt ägare, synlighet och default branch | Läs repositoryinställningar | Matchar projektprofil | `[[...]]` |
| GitHub-behörighet | Issue, PR, Actions, Projects och branchregler | Testa minsta läsning per funktion | Endast nödvändig behörighet | `[[...]]` |
| Konton/kostnad | Abonnemang, budgetägare och gränser | Kontrollera leverantörens aktuella plan | Godkänd kostnadsbedömning | `[[...]]` |
| Miljöer | Lokal/test/produktion är separerade | Granska konfiguration och åtkomst | Ingen produktionshemlighet i test | `[[...]]` |
| Hemligheter | `.env.example` saknar riktiga värden | Sökning och manuell granskning | Endast namn och säkra platshållare | `[[...]]` |
| Agentinstruktioner | Läsordning och mandat finns | Kör lokal verifierare | Inga obligatoriska filer saknas | `[[...]]` |
| Plugins/MCP | Faktisk funktion och rättighet | Läs-/skrivtest med ofarlig åtgärd | Resultat dokumenterat | `[[...]]` |
| Tester/CI | Vald runtime och workflow är relevanta | Kör test i avsedd miljö | Grön, begriplig output | `[[...]]` |
| Dokumentation | Länkar och status stämmer | Lokal verifierare + granskning | Inga öppna dokumentationsfel | `[[...]]` |
| Återställning | Ägare och steg är testbara | Scenariogenomgång eller test | Tydlig trigger och återställning | `[[...]]` |

Automation får inte flyttas till `.github/workflows/` förrän relevanta rader är verifierade.
