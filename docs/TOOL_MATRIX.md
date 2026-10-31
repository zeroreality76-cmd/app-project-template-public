# Verktygsmatris

Statusen beskriver denna arbetsmiljö vid paketbyggandet. “Tillgänglig” betyder inte att målprojektets konto eller behörighet har verifierats.

| Behov | Roll | Skill/verktyg | Behörighet | Kostnad | Alternativ | Status |
|---|---|---|---|---|---|---|
| System- och arkitekturdesign | Arkitekt | Engineering: System Design, Architecture | Lokal läsning/skrivning | Ingår i arbetsmiljön | Manuell ADR | Verifierad metod |
| Dokumentation och handoff | Dokumentationsansvarig | Engineering: Documentation, lokal Markdown | Lokal filåtkomst | Gratis | Manuell dokumentgranskning | Verifierad |
| Teststrategi/release | Testare/drift | Engineering: Testing Strategy, Deploy Checklist | Lokal filåtkomst | Gratis | Projektets egna tester | Verifierad metod |
| Lokal kontroll | Testare | Python 3.11, `tools/verify_template.py` | Lokal körning | Gratis | Manuell checklista | Verifierad |
| GitHub repository/issue/PR | Projektledare | GitHub-anslutning | Kontoberoende | Planberoende | GitHub UI/CLI | Konto upptäckt; projektbehörighet ej verifierad |
| GitHub Projects V2 | Projektledare | GraphQL/CLI enligt underlag | Separat Projects-behörighet | Planberoende | Manuell Projects-konfiguration | Ej verifierad |
| CI/workflows | Builder/testare | GitHub Actions-mallar | Repository-/Actions-behörighet | Plan-/användningsberoende | Lokal testkörning | Inaktiv, ej verifierad |
| Valfri webbdrift | Arkitekt/drift | Leverantörsmodul efter ADR | Kontoberoende | Beslutas per projekt | Annan leverantör | Inte vald |
| Valfri databas/backend | Arkitekt/builder | Leverantörsmodul efter ADR | Kontoberoende | Beslutas per projekt | Annan leverantör | Inte vald |

Använd bara en rad när behovet finns. Uppdatera status med konkret testresultat i projektets setup-check.
