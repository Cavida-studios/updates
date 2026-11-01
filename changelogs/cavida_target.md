# cavida_target

## 1.0.1

- Filter invalid world-geometry and streaming entity handles before reading models.
- Catch model-native failures so they do not terminate the target loop.
- Reset raycast state when closing so repeated Alt activations start cleanly.

## 1.0.0

- New Cavida interface with proximity dots, compact action menu, scroll selection and optional mouse control.
- Compatibility providers and export aliases for ox_target, qb-target and qtarget.
- Zones, entities, models, bones, conditional actions, consumer cleanup and central version registration through cavida_bridge.
