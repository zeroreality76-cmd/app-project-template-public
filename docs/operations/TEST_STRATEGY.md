# Teststrategi

## Princip

Testa främst affärskritiska flöden, felvägar, behörighetsgränser, dataintegritet och återställning. Anpassa testnivå till faktisk teknik och risk.

| Område | Testnivå | Exempel | Bevis |
|---|---|---|---|
| Affärslogik | Unit | Regler, validering, beräkning | Testresultat |
| API/integration | Integration/kontrakt | Behörighet, schema, timeout, återförsök | Körlogg utan hemligheter |
| Gränssnitt | Komponent/E2E | Kritiska användarflöden, fel, tangentbord | Rapport/skärmbild |
| Säkerhet | Negativa tester/granskning | Otillåten åtkomst, indata, läckage | Hotbedömning |
| Drift | Smoke/rollback | Hälsa, deploy, återställning | Releasebevis |

Sätt endast täckningsmål när kodbas, risk och testverktyg är valda. Ett grönt test ersätter inte produktacceptans.
