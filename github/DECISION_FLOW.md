# Flöde för ägarbeslut

1. Agenten fastställer att frågan ligger utanför mandatet.
2. Sök öppna ärenden efter samma stabila beslutsnyckel (`DEC-<ämne>-v<version>`).
3. Om en match finns, uppdatera den; annars skapa ett beslutissue från mallen.
4. Kontrollera att ägarkontot är verifierat innan tilldelning. Misslyckas det, skapa ett färdigt utkast och markera blockerat.
5. Ärendet ska innehålla sammanhang, alternativ, rekommendation, konsekvenser, blockerade arbeten, motiverad svarstid och källänkar.
6. Registrera det tydliga svaret med källänk i beslutsloggen.
7. Uppdatera berörda krav, ADR, prognos och Projects-status. Återuppta endast när alla beroenden är uppfyllda.

Otydligt svar kräver uppföljning. Ändrat svar skapar nytt beslut som länkar till det tidigare. Tystnad är aldrig godkännande.
