# App Project Template

En återanvändbar, teknikneutral mall för att starta och styra webb-/SaaS-projekt. Den innehåller styrning, produktunderlag, agentroller, GitHub-underlag, inaktiva automationer och verifieringsrutiner.

## Start

1. Läs [Börja här](docs/START_HERE.md).
2. Fyll i [projektprofilen](docs/PROJECT_PROFILE.md).
3. Sätt statusen i [kravmatrisen](docs/REQUIREMENTS_MATRIX.md) för varje relevant rad.
4. Använd [installationskontrollen](docs/operations/SETUP_CHECK.md) innan någon integration eller automation aktiveras.

Mallen är publicerad som det privata GitHub-template-repositoryt [`zeroreality76-cmd/app-project-template`](https://github.com/zeroreality76-cmd/app-project-template). Den innehåller inga hemligheter och inga aktiva GitHub Actions-workflows.

## Principer

- Dokument är sanningskälla för mål, krav, beslut, arkitektur och bevis; GitHub är sanningskälla för operativt arbete när det är anslutet.
- Basplan och aktuell prognos hålls åtskilda.
- Teknik och tjänster väljs först efter ett dokumenterat beslut.
- Automationer är inaktiva tills behörighet, kostnad, dubblettskydd och reservrutin har verifierats.
- Status får endast vara `förberedd`, `verifierad` eller `blockerad`; planerat får aldrig beskrivas som genomfört.

Se [mallversionen](TEMPLATE_VERSION.md) och [ändringsloggen](CHANGELOG.md) för paketets livscykel.
