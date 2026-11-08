# cavida_fps 1.0.6

- Reject conflicting first-time preference saves instead of confirming another request’s data.

# cavida_fps 1.0.5

- Het prestatiescherm en de grafiek gebruiken het Cavida-blauwe kleurenpalet.

# cavida_fps 1.0.4

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.

# cavida_fps

## 1.0.3

- Spelersvoorkeuren staan per server-gecontroleerde characteridentiteit in SQL.
- Bestaande lokale voorkeuren worden alleen ingelezen bij de eerste SQL-migratie.
- De interface bevestigt opslaan pas na server- en databasebevestiging; fouten herstellen de vorige lokale waarden.

Gecontroleerd met MariaDB en lokale Lua-contracten. Geen geslaagde live FiveM-test geclaimd.

## 1.0.2

- Centrale registratie van FPS-beheerinstellingen.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.
