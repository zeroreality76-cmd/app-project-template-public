# Global säkerhetsbas

- Använd minst privilegium, separata roller och verifierad auktorisation på varje skyddad operation.
- Validera och normalisera indata på servergränsen; använd säkra standardvärden och generiska fel mot klienten.
- Lagra inga hemligheter i repository, loggar eller klientkod. Dokumentera endast variabelnamn i `.env.example`.
- Skydda data under överföring och i lagring enligt vald plattform och dataklassning.
- Definiera beroendeuppdatering, säkerhetstest, loggåtkomst, backup, återställning och incidentägare innan drift.
- Hotmodellera ändringar som påverkar identitet, behörighet, betalning, personuppgifter, externa webhooks eller administrativ åtkomst.

Detta är en global bas. Aktivera [EU-/GDPR-modulen](EU_GDPR_MODULE.md) när marknad eller behandling kräver den.
