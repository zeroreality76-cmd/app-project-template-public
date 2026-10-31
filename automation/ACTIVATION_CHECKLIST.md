# Aktiveringschecklista för automation

1. Bekräfta att projektprofil, teknikvalsbeslut och setup-check är verifierade.
2. Granska workflow för minsta `permissions`, inga exponerade hemligheter och inga oavsiktliga skrivoperationer.
3. Sätt concurrency-grupp, idempotensnyckel, loopskydd, timeout och manuell paus-/reservrutin.
4. Testa i ett godkänt testrepository med icke-känsliga testdata.
5. Dokumentera körning, kostnad, ansvarig och rollback i automationsregistret.
6. Aktivera genom en granskad PR som flyttar en enda mall till `.github/workflows/`.
7. Övervaka första körningen och återställ genom att ta bort workflow från den aktiva sökvägen om utfallet avviker.
