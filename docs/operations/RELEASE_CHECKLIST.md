# Releasechecklista

## Före release

- [ ] Godkända krav och acceptanskriterier har bevis i kravmatrisen.
- [ ] Relevanta tester är körda i avsedd miljö och resultatet är länkat.
- [ ] Oberoende kod-/säkerhetsgranskning är genomförd där policy kräver den.
- [ ] Migrationer, feature flags och kompatibilitet är bedömda när relevanta.
- [ ] Rollbackplan, incidentägare och kommunikation är aktuella.
- [ ] Kostnads- och kapacitetsrisk är acceptabel eller uttryckligen godkänd.

## Under och efter release

- [ ] Verifiera vald release i test/staging före produktion när miljön finns.
- [ ] Kör relevanta smoke tests och kritiska användarflöden.
- [ ] Övervaka fördefinierade signaler under överenskommen period.
- [ ] Uppdatera releasebevis, ändringslogg och operativ status.

## Återställningssignaler

Sätt projektspecifika trösklar före release, exempelvis kritiskt flöde trasigt, otillåten åtkomst, korrupt data, tydlig felspik eller oacceptabel kostnadsökning.
