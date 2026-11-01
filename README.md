# Cavida Studios — resource updates

Openbaar versieregister voor Cavida-resources. Deze repository bevat uitsluitend versienummers, changelogs en links; broncode en installatie-ZIPs staan in privé-repositories. Downloads vereisen repositorytoegang of worden via het Cavida-klantenportaal aangeboden.

## Resources

- [cavida_bridge](changelogs/cavida_bridge.md) — gedeelde frameworkbridge en updatechecker.
- [davidcrypto](changelogs/davidcrypto.md) — mining, hardware, warehouses en wallets voor Oosterberg roleplay.

## Voor serverbeheerders

Start cavida_bridge vóór de aangesloten resources. De bridge meldt beschikbare updates in de serverconsole, met de wijzigingen sinds je geïnstalleerde versie en een downloadlink. Controleer handmatig via cavida_updates of cavida_updates davidcrypto. Automatische controles vinden bij starten en iedere zes uur plaats. Er worden geen updates automatisch geïnstalleerd. Tokens zijn niet nodig op de gameserver.

## Nieuwe resource aansluiten

1. Geef fxmanifest.lua een stabiele versie zoals 1.0.0 en voeg cavida_bridge toe als dependency.
2. Roep server-side exports.cavida_bridge:RegisterResource(GetCurrentResourceName()) aan bij je eigen resource-start en na bridge-start.
3. Publiceer resources/<resourcenaam>.json en changelogs/<resourcenaam>.md. Gebruik de exacte resourcenaam, inclusief underscores.
4. Gebruik tools/release.py uit de privé-resource voor een consistente private release en openbare metadata. Lees daar RELEASING.md.

De JSON bevat resource, version, url (volledige changelog), download en releases: een lijst met version en changes (lijst van tekstregels), nieuwste eerst. Alleen stabiele versies met drie getallen. Plaats geen tokens, klantgegevens, licenties of broncode in deze repository.
