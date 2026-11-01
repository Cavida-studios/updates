# cavida_target

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
