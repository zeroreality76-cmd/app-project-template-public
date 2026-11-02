# App Project Template

En öppen, svensk och teknikneutral mall för att starta och styra webb-/SaaS-projekt med tydliga beslut, arbetsordrar och verifiering. Den passar när du vill bygga en app metodiskt — ensam, i ett team eller tillsammans med AI-agenter — utan att låsa projektet till en viss databas, molnleverantör eller plugin.

> **Offentlig beta.** Mallen är avsiktligt omfattande för att fungera i riktiga projekt. Börja med snabbvägen nedan; aktivera de fördjupande modulerna först när ditt projekt behöver dem.

## Vem är den för?

- Webbappar och SaaS-projekt som behöver tydligt syfte, data- och teknikbeslut, test och driftansvar.
- Projekt där AI-agenter kan hjälpa till, men där pengar, åtkomst, personuppgifter och produktion fortfarande kräver ett tydligt ägarbeslut.
- Team som vill skilja en godkänd plan från aktuell prognos och från faktiskt verifierad leverans.

Den är mindre lämplig för en engångssida utan data, arbetsflöden eller fortsatt förvaltning. Använd då bara projektprofilen, produktkraven och en enkel arbetsorder.

## Skapa ett nytt projekt

1. Klicka **Use this template** högst upp på GitHub och välj **Create a new repository**.
2. Välj namn, ägare och synlighet för ditt nya projekt. Det nya repositoryt blir självständigt.
3. Läs [Börja här](docs/START_HERE.md) och utse en produktägare, en projektledare/manager och en arkitekt när tekniska vägval behövs.
4. Fyll i [projektprofilen](docs/PROJECT_PROFILE.md) och [projektstartens beslutsunderlag](docs/PROJECT_DECISION_WORKBOOK.md).
5. Följ [projektgenomförandeplanen](docs/PROJECT_EXECUTION_PLAYBOOK.md): skapa först plan och arbetsorder, bygg därefter.
6. Använd [installationskontrollen](docs/operations/SETUP_CHECK.md) innan någon extern integration, hemlighet eller automation aktiveras.

En skapad projektkopia får inte automatiskt GitHub-behörigheter, hemligheter, branchregler, labels eller Projects. Sätt upp dessa per projekt med minsta nödvändiga behörighet.

## De viktigaste dokumenten

- [Projektagent: manager, arkitekt och routing](docs/AGENT_ORCHESTRATION.md) — vem gör vad och när ägaren måste besluta.
- [Projektgenomförandeplan](docs/PROJECT_EXECUTION_PLAYBOOK.md) — faserna från uppdrag till release.
- [Projektstart: beslutsunderlag](docs/PROJECT_DECISION_WORKBOOK.md) — syfte, målgrupp, data, backend, kostnad och godkännande.
- [Urval av skills, plugins och verktyg](docs/PROJECT_TOOL_SELECTION.md) — välj bara verktyg som behov, behörighet och risk motiverar.
- [Kravmatris](docs/REQUIREMENTS_MATRIX.md) — behov → leverans → verifiering → status → bevis.

## Principer

- Dokument är sanningskälla för mål, krav, beslut, arkitektur och bevis; GitHub är sanningskälla för operativt arbete när det är anslutet.
- Basplan och aktuell prognos hålls åtskilda.
- Teknik och tjänster väljs först efter ett dokumenterat beslut.
- Automationer är inaktiva tills behörighet, kostnad, dubblettskydd och reservrutin har verifierats.
- Status får endast vara `förberedd`, `verifierad` eller `blockerad`; planerat får aldrig beskrivas som genomfört.

## Bidra och säkerhet

Läs [CONTRIBUTING.md](CONTRIBUTING.md) innan du föreslår en ändring. Rapportera inte hemligheter eller sårbarhetsdetaljer i ett öppet issue; se [SECURITY.md](SECURITY.md).

## Licens

Mallen är licensierad under [MIT-licensen](LICENSE). Den används på egen risk och utan garanti.

Se [mallversionen](TEMPLATE_VERSION.md) och [ändringsloggen](CHANGELOG.md) för paketets livscykel.
