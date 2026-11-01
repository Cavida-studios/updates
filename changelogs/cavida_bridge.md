# cavida_bridge

## 1.3.0

- Gedeelde laptop-/appbridge met automatische optionele AV Laptop-integratie.
- RegisterLaptopApp, GetLaptopState, GetLaptopAccess, OpenLaptopApp en LaptopMessage beschikbaar.
- Provider-interface voor een toekomstige Cavida-laptop; standalone apparaat en configureerbare directe netwerkverbinding.
- AV-wifi gekoppeld aan de huidige server-serial en een korte geldigheidsduur.
- RegisterUsableItem voor Qbox/QBCore/ESX en UseInventoryItem voor optionele ox-use validatie.
- AK47-bankmutaties krijgen voorrang wanneer beschikbaar; native frameworkbank als alternatief, nooit een tweede mutatie na een mislukte betaling.
- PlayerData.loaded voor veilig personagebeheer; framework- en laptopregressies toegevoegd.

## 1.2.0

- Gedeelde updatechecker voor alle Cavida-resources via RegisterResource(resourcenaam).
- Versie wordt uit het eigen fxmanifest gelezen; console toont nieuwe versies, wijzigingen en downloadlink.
- Controle bij registratie en iedere zes uur; consolecommand cavida_updates [resource].
- Zelfregistratie van de bridge, timeoutafhandeling en opruimen van gestopte resources.
- GetVersion leest voortaan de daadwerkelijke manifestversie.
