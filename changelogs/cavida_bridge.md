# cavida_bridge

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
