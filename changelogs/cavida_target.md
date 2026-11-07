# cavida_target 1.2.5

- De ox_target-registratie-exports voor zones en modellen zijn beschikbaar vóór SQL-gereedmelding, zodat ox_inventory ze tijdens initialisatie kan gebruiken.
- De centrale instellingenservice ontvangt de Target-standaardwaarden. De interactie-interface wacht op gereedmelding.

# cavida_target 1.2.4

- Blauwe standaardaccenten voor het interactiemenu. Bestaande opgeslagen kleurkeuzes blijven behouden.

# cavida_target 1.2.3

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.

# cavida_target

## 1.2.2

- Centrale registratie van target- en interactieinstellingen.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.

## 1.2.1

- Execute the selected target action with E, alongside the existing left-click selection.
- Support E while the menu has mouse focus and prevent repeated keyboard activation.
- Suppress native pickup/context controls while targeting; preserve floating markers and wave animations.

## 1.2.0

- Add subtle Cavida wave animations to the active reticle and gently floating proximity markers.
- Position entity markers above model bounds and follow moving targeted objects, vehicles and peds.
- Preserve marker identities across updates and support animation settings and reduced motion.

## 1.1.0

- Replace the large interaction panel with compact floating action rows beside a small diamond reticle.
- Remove the title, counters, distance badge and persistent control banners from the target UI.
- Use subtle proximity dots and a configurable mint accent while retaining existing target exports and interaction behavior.

## 1.0.2

- Register ox_target, qb-target and qtarget compatibility exports before loading the interaction runtime.
- Prevent duplicate export handlers when runtime control exports are added.
- Correct installation order: start cavida_bridge and cavida_target before ox_inventory, the framework and target consumers.

## 1.0.1

- Filter invalid world-geometry and streaming entity handles before reading models.
- Catch model-native failures so they do not terminate the target loop.
- Reset raycast state when closing so repeated Alt activations start cleanly.

## 1.0.0

- New Cavida interface with proximity dots, compact action menu, scroll selection and optional mouse control.
- Compatibility providers and export aliases for ox_target, qb-target and qtarget.
- Zones, entities, models, bones, conditional actions, consumer cleanup and central version registration through cavida_bridge.
