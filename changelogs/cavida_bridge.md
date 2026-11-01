# cavida_bridge

## 1.2.0

- Gedeelde updatechecker voor alle Cavida-resources via RegisterResource(resourcenaam).
- Versie wordt uit het eigen fxmanifest gelezen; console toont nieuwe versies, wijzigingen en downloadlink.
- Controle bij registratie en iedere zes uur; consolecommand cavida_updates [resource].
- Zelfregistratie van de bridge, timeoutafhandeling en opruimen van gestopte resources.
- GetVersion leest voortaan de daadwerkelijke manifestversie.
