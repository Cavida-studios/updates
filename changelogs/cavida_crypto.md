# cavida_crypto 7.0.5

- Lichte MDT-stijl voor de warehousecatalogus en blauwe accenten in het technische Crypto-dashboard.
- Zichtbare branding in het Crypto-scherm gebruikt Cavida Studios.

# cavida_crypto 7.0.4

- Hardware- en app-exports blijven beschikbaar tijdens uitgestelde initialisatie en weigeren gebruik totdat bridge, server en client gereed zijn.
- Crypto-hardware wordt tijdens het wachten niet verbruikt; bestaande SQL-eigendom en spelersgegevens blijven behouden.

# cavida_crypto 7.0.3

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.

# cavida_crypto

## 7.0.2

- Robuuste opstart initialiseert de gebundelde SQL-opslagmodule voordat CryptoStore wordt gebruikt.
- Ontbrekende, beschadigde of onvolledig geïnstalleerde bestanden stoppen de resource met een duidelijke melding, zonder lege spelersgegevens aan te maken.
- Bestaande SQL- en migratiegegevens en reeds geladen opslagrevisies blijven ongewijzigd.

Opstart gecontroleerd met ontbrekende, beschadigde en reeds geladen modules. Geen geslaagde FiveM-test geclaimd.

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
