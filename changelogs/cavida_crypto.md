# cavida_crypto

## 7.0.1

- Alle cryptogegevens worden als volledige snapshot opgeslagen in SQL: wallets, racks, hardware, warehouses, bestellingen en verplichtingen.
- Alleen-lezen export van de oude davidcrypto-KVP naar SQL, zonder de oorspronkelijke gegevens te wissen.
- Expliciet herstel met een SQL-backup van de vervangen dataset; conflicterende datasets worden niet blind samengevoegd.
- Geen stilzwijgende lege installatie; SQL-fouten of revisieconflicten blokkeren verdere mutaties.

Gecontroleerd met MariaDB en lokale Lua-contracten. Geen geslaagde live FiveM-test geclaimd.

## 7.0.0

- Cavida Crypto als native app op Cavida Desktop; externe laptopintegratie verwijderd.
- Uitsluitend Cavida-branding en migratiepad voor bestaande wallets, racks en warehouses bij hernoemen.
- Ontwikkeltools, tests en demomodus uit de actuele resourceboom verwijderd.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.
