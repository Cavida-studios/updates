# Cavida Studios â€” resource updates

Openbaar versieregister voor Cavida-resources. Deze repository bevat uitsluitend versienummers, changelogs en verwijzingen. De daadwerkelijke resources staan in afzonderlijke privÃ©repositories. Uitgebrachte assets worden aan gebruikers geleverd via het Cfx.re-portaal, onder Purchased Assets.

## Centrale controle

Start `cavida_bridge` vÃ³Ã³r de aangesloten resources. De bridge registreert resources en controleert hun openbare metadata. Handmatig controleren kan met `cavida_updates` of `cavida_updates <resourcenaam>`. Servers hebben hiervoor geen GitHub-token nodig. Er worden geen updates automatisch geÃ¯nstalleerd of uitgevoerd.

Iedere resource gebruikt een versie met drie getallen en registreert server-side via `exports.cavida_bridge:RegisterResource(GetCurrentResourceName())`, bij de eigen start en opnieuw na een bridge-herstart. Resources implementeren geen afzonderlijke HTTP-updatechecker. Consolemeldingen verwijzen voor levering uitsluitend naar het Cfx.re-portaal.

## Metadata

Elke resource heeft `resources/<resourcenaam>.json` en `changelogs/<resourcenaam>.md`, met exact dezelfde resourcenaam als de installatiemap. Houd manifest, releaseadministratie, Git-tag, privÃ©release en openbare metadata consistent. Publiceer alleen werkelijk gepushte en geteste releases.

Een ontwikkelrecord bevat `status: development`, `developmentVersion` en een lege lijst `releases`. Dit adverteert geen stabiele update. Een stabiel record bevat `resource`, `version` en `releases` met per versie de wijzigingen. Plaats hier nooit broncode, resource-ZIPs, tokens, klantgegevens of ontwikkelhulpmiddelen.
