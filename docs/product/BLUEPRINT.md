# Blueprint

## Syfte och gränser

Beskriv produktens huvudflöden, systemgränser och vilken information som passerar mellan dem. Hänvisa till produktkrav i stället för att duplicera dem.

```text
Användare → gränssnitt → applikationslogik → data/integration
                       ↘ observability och verifieringsbevis
```

| Del | Ansvar | Äger data? | In-/utdata | Beroenden | Felhantering |
|---|---|---|---|---|---|
| Gränssnitt | `[[ANSVAR]]` | Nej | `[[IN/UT]]` | `[[BEROENDE]]` | `[[BETEENDE]]` |

## Antaganden att pröva

| Antagande | Konsekvens om fel | Kontroll | Ägare | Status |
|---|---|---|---|---|
| `[[ANTAGANDE]]` | `[[PÅVERKAN]]` | `[[TEST/INTERVJU/ANALYS]]` | `[[ÄGARE]]` | Öppen |
