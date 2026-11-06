# cavida_postal 1.2.2

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.

# cavida_postal

## 1.2.1

- De blijvende voertuigvolgnummering staat in SQL en migreert uit de bestaande KVP.
- Een databaseconflict bij nummerreservering ontstaat vóór het aanmaken van een werkvoertuig.

Gecontroleerd met MariaDB en lokale Lua-contracten. Geen geslaagde live FiveM-test geclaimd.

## 1.2.0

- Cavida Post als native laptopapp; starten en uitvoeren van routes behoudt bestaande locatie- en jobcontroles.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.

## 1.1.0

- Twelve selectable route areas with 74 delivery addresses; surprise routes avoid repeating the previous area.
- Package and freight drivers must collect each box at the parked vehicle rear, with opening cargo doors, a pickup animation and a persistent carry prop.
- Boxes can be returned to the vehicle; delivery consumes one box and falling, death or leaving the job clears carried cargo.
- Vehicle damage creates persistent fines, shown in the HUD and deducted from delivery wages; cancelling, repairs or reconnecting do not erase recorded fines.
- Automatic profile migration adds damage debt and totals; manual SQL upgrade is included for installations without automatic schema updates.

## 1.0.2

- Use shared Cavida logging to keep repository URLs out of all console and error output.
- Require cavida_bridge 1.4.4 or newer for shared log filtering.

## 1.0.1

- Use Cavida branding throughout the portal, HUD, map labels and resource metadata.
- Remove development files, test fixtures and browser preview mode from the resource repository.
