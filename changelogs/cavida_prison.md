# cavida_prison

## 2.5.0

- Gevangenispaneel als native laptopapp met bestaande panelrechten, deuren en camerafuncties.
- Ontwikkeltools en tests uit de actuele resourceboom verwijderd.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.

## 2.4.0

- Register cavida_prison with the shared bridge update checker at startup and after bridge restarts.
- Require cavida_bridge 1.3.2+ and reject unloaded framework players for panel/door management and canteen actions.
- Keep framework, inventory, banking and doorlock integrations centralized in cavida_bridge.
- Add a private source repository, reproducible runtime release packaging and public version metadata.
