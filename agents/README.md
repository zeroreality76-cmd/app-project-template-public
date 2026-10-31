# Agentorganisation

Projektledaren väljer minsta nödvändiga roll för varje arbetsorder. En rollinstruktion är inte bevis på att en oberoende agent har använts.

| Situation | Obligatorisk separation |
|---|---|
| Säkerhetsgräns, hemligheter, åtkomst eller högriskdata | Builder och säkerhetsgranskare ska vara oberoende. |
| Kodändring med verksamhetskritisk effekt | Builder och kodgranskare ska vara oberoende. |
| Release | Builder/testare och driftansvarig ska bekräfta olika kontroller. |
| Gemensamt styrdokument | Endast utsedd dokumentationsansvarig ändrar filen. |
