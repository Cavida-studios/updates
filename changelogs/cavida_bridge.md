# cavida_bridge 1.10.1

- Het manifest vermeldt startup.lua en settings.lua expliciet als bestanden voor imports vanuit andere resources.

# cavida_bridge 1.10.0

- Centrale AwaitReady-/IsReady-contracten bewaken beide SQL-opslaglagen, instellingenaudit en geladen bridge-instellingen.
- SQL-gereedmelding wordt zonder vaste opstartdeadline afgewacht; initialisatiefouten worden opnieuw geprobeerd zonder lege fallback.
- Gedeelde native Lua-opstartwachtrij behoudt scriptvolgorde en Asset Escrow; clientcode wacht op servergereedmelding.
- SmartFires-broncontracten leveren gecontroleerde brandmeldingen aan Cavida Meldkamer met herkenning van bronuitval en providerherstarts.

# cavida_bridge 1.9.1

- SQL-opslag wacht langer op vertraagde oxmysql-gereedmelding; wachttijd telt geplande polls in plaats van tijd tijdens zware resource-opstart.
- Maximaal vijf idempotente initialisatiepogingen herstellen tijdelijke SQL-startfouten zonder bestaande opslag of instellingen te vervangen.
- Veilige diagnostiek onderscheidt ontbrekende database-gereedmelding, toegangsproblemen en ontbrekend SQL-schema zonder verbindingsgegevens te loggen.

# cavida_bridge 1.9.0

- Gedeelde tRadio-kanaalinzage en gecontroleerde portoverplaatsing voor Cavida Meldkamer, met actuele rol-, instance- en providerrechten.
- Optionele eigen privé-noodgesprekken via pma-voice: aannemen, wachten, hervatten en beëindigen; bestaande gesprekken worden niet overgenomen.

# cavida_bridge

## 1.8.0

- Gedeelde garageleescontracten voor JG, Codesign, VMS, okokGarage, Qbox Garages, QB Garages en ESX Garage, met veilige SQL-projectie en expliciete providerkeuze.
- Actuele OneSync-voertuigposities met instancecontrole en herkenning van dubbele kentekens; leveranciersgegevens worden niet gewijzigd.
- Afgeschermde overdracht naar officiële impoundformulieren van JG, Codesign en VMS met actuele rol-, voertuig-, afstands- en stilstandcontrole.

Gecontroleerd met echte lokale MariaDB, officiële API-/nativecontracten met mocks en telefoon-/laptopbrowser. Live FiveM-tests op verzoek overgeslagen.

## 1.7.0

- Frameworkonafhankelijke fysieke voertuigdiagnose met servermetingen voor motor, carrosserie en tank en clientmetingen voor banden, koplampen en rijdbaarheid.
- Afgeschermde scanexport met afstands-, stilstand-, instance-, kenteken-, model-, aanvraag- en actuele rolcontrole; fouten geven geen goedkeuring.
- JG-onderhoud levert een afzonderlijke momentopname voor automatische keuringsbewijzen.

Gecontroleerd met echte lokale MariaDB, native/API-mocks en telefoon/laptopbrowser; geen live FiveM-tests op verzoek.

## 1.6.0

- Centrale read-only woningregisters voor rcore_housing, VMS Housing en ATY Housing met uitsluiting van sleutelhouders en privégegevens.
- JG Mechanic-onderhoud en JG Vehicle Mileage via officiële serverexports; aanvullende providers melden een afgeschermde leesadapter aan.
- Alle registerinstellingen blijven server-side en worden beheerd in Cavida Beheer.

Gecontroleerd met lokale MariaDB, API-mocks en browser op telefoon/laptop. Live FiveM-tests op verzoek overgeslagen.

## 1.5.1

- Blijvende centrale instellingen en audithistorie staan in SQL; KVP wordt alleen gelezen voor eenmalige migratie.
- Gedeelde SQL-opslag met resource-eigendom, revisiecontrole en expliciete herstelbackups.
- SQL-uitval stopt instellingeninitialisatie zonder stille terugval naar lege standaardwaarden.

Gecontroleerd met MariaDB en lokale Lua-contracten. Geen geslaagde live FiveM-test geclaimd.

## 1.5.0

- Centrale beheerrechten voor QBCore, Qbox, ESX en standalone; Cavida Desktop is de primaire apphost.
- Gedeelde instellingenservice met scheiding tussen servergeheimen en publieke clientwaarden.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.

## 1.4.7 — testrelease

- PlayerData levert de server-side character-voornaam, achternaam en echte baasstatus voor afgeschermde werkmail.

## 1.4.6 — testrelease

- Testrelease voor in-game validatie.
- Centrale checker herkent ontwikkelmetadata en gepubliceerde testreleases.
- Bestaande stabiele updates blijven in hun eigen kanaal.



## 1.4.5

- Prefer cavida_target during automatic target provider detection.
- Use the existing compatible target exports for interaction registration and cleanup.

## 1.4.4

- Update notices direct users to the Cfx.re Portal (Purchased Assets) without printing repository, API, raw, download or changelog URLs.
- Shared Cavida logging redacts repository URLs in diagnostic messages, external errors and update changelog text.

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
