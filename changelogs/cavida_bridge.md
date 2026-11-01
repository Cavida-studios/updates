# cavida_bridge

## 1.4.3

- Keep the GitHub repository limited to the installable Cavida resource and installation/release documentation.
- Remove local-only tests, CI workflows and release tooling from the resource repository; runtime behavior remains unchanged.

## 1.4.2

- Read public version metadata through the unauthenticated GitHub Contents API using its raw JSON media type, avoiding stale branch snapshots served by the GitHub Raw CDN.
- Retain cache-control headers, per-request URLs, manual source/path/version diagnostics and protected HTTP error handling.
- HTTP errors and API rate limits report an unavailable check, never a false up-to-date result.

## 1.4.1

- Each update request now uses a unique cache-busting URL and no-cache headers to avoid reusing stale version metadata.
- Manual checks print the installed version, exact metadata URL, actual resource directory and received published version for diagnosis.
- Regression coverage reproduces an installed 1.3.2 receiving stale metadata and then correctly detecting a fresh 1.4.1 response.

## 1.4.0

- Central vehicle key integration for fourteen providers, including ak47_vehiclekeys and ak47_qb_vehiclekeys.
- Added trusted GiveVehicleKeys, RemoveVehicleKeys, HasVehicleKeys and provider diagnostics with validation, deduplication and protected calls.
- AK47 supports virtual and physical keys through a bounded, allowlisted client relay; other integrations use native server APIs or documented events.
- Added key-provider regression tests and GitHub Actions; in-game provider acceptance remains pending.

## 1.3.2

- All update-checker status messages, warnings and registration errors are now in English.
- Public changelog history for the bridge and davidcrypto is now available in English.

## 1.3.1

- Each registered resource prints UP-TO-DATE with its installed version after the first successful check.
- Periodic checks do not repeat an unchanged status; cavida_updates always prints the current status.
- Local versions newer than the public release receive a separate status message.

## 1.3.0

- Shared laptop and app bridge with optional automatic AV Laptop integration.
- Added RegisterLaptopApp, GetLaptopState, GetLaptopAccess, OpenLaptopApp and LaptopMessage.
- Provider interface for a future Cavida laptop, standalone device access and a configurable direct connection.
- AV WiFi reports are bound to the current server-validated device serial and expire after a short interval.
- Added RegisterUsableItem for Qbox/QBCore/ESX and UseInventoryItem for optional ox validation.
- AK47 bank mutations take priority when available, with native framework banking as an alternative; failed mutations never retry through another backend.
- Added PlayerData.loaded and regression coverage for framework and laptop integration.

## 1.2.0

- Shared update checker for Cavida resources through RegisterResource(resourceName).
- Reads installed versions from each resource manifest and prints available versions, changes and download links.
- Checks after registration and every six hours; console command: cavida_updates [resource].
- Automatic bridge registration, timeout handling and cleanup of stopped resources.
- GetVersion now reads the actual manifest version.
