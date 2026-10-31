# Rollbackplan

| Område | Trigger | Återställning | Ägare | Verifiering | Kommunikation |
|---|---|---|---|---|---|
| Applikationsrelease | `[[TRIGGER]]` | `[[VERSION/FLAGG/STEG]]` | `[[ROLL]]` | `[[SMOKE TEST]]` | `[[MOTTAGARE]]` |
| Datamigrering | `[[TRIGGER]]` | `[[BACKUP/COMPENSERANDE MIGRERING]]` | `[[ROLL]]` | `[[INTEGRITETSKONTROLL]]` | `[[MOTTAGARE]]` |
| Integration | `[[TRIGGER]]` | `[[PAUSA/ÅTERGÅ/MANUELL RUTIN]]` | `[[ROLL]]` | `[[KONTROLL]]` | `[[MOTTAGARE]]` |

Ingen återställningsrutin får antas fungera utan scenariogenomgång eller faktiskt test, beroende på risk.
