# App Project Template

En återanvändbar, teknikneutral mall för att starta och styra webb-/SaaS-projekt. Den innehåller styrning, produktunderlag, agentroller, GitHub-underlag, inaktiva automationer och verifieringsrutiner.

## Start

1. Läs [projektgenomförandeplanen](docs/PROJECT_EXECUTION_PLAYBOOK.md) och [Börja här](docs/START_HERE.md).
2. Fyll i [projektprofilen](docs/PROJECT_PROFILE.md) och samla saknade beställningsunderlag.
3. Fatta eller eskalera avgörande val i [projektstartens beslutsunderlag](docs/PROJECT_DECISION_WORKBOOK.md).
4. Inventera och välj relevanta [skills, plugins och verktyg](docs/PROJECT_TOOL_SELECTION.md) för just projektet.
5. Sätt statusen i [kravmatrisen](docs/REQUIREMENTS_MATRIX.md) för varje relevant rad.
6. Använd [installationskontrollen](docs/operations/SETUP_CHECK.md) innan någon integration eller automation aktiveras.

Mallen är publicerad som det privata GitHub-template-repositoryt [`zeroreality76-cmd/app-project-template`](https://github.com/zeroreality76-cmd/app-project-template). Den innehåller inga hemligheter och inga aktiva GitHub Actions-workflows.

## Principer

- Dokument är sanningskälla för mål, krav, beslut, arkitektur och bevis; GitHub är sanningskälla för operativt arbete när det är anslutet.
- Basplan och aktuell prognos hålls åtskilda.
- Teknik och tjänster väljs först efter ett dokumenterat beslut.
- Automationer är inaktiva tills behörighet, kostnad, dubblettskydd och reservrutin har verifierats.
- Status får endast vara `förberedd`, `verifierad` eller `blockerad`; planerat får aldrig beskrivas som genomfört.

Se [mallversionen](TEMPLATE_VERSION.md) och [ändringsloggen](CHANGELOG.md) för paketets livscykel.
