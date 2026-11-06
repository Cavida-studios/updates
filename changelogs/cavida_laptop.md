# cavida_laptop 0.7.3

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.

# cavida_laptop

## 0.7.2

- Centraal beheerde PV-vragen ondersteunen het antwoordtype Locatie met kaart voor MEOS 0.9.0.
- Bestaande vragenlijsten en instellingen blijven behouden; een bestaande tekstvraag met code location krijgt eveneens de locatiekiezer.

Lokale MariaDB-, browser-, datum- en callbackcontractcontroles uitgevoerd. Live FiveM-tests op expliciet verzoek overgeslagen.

## 0.7.1

- Visuele PV-editor in Cavida Beheer voor MEOS: stappen en vragen toevoegen, verplaatsen en verwijderen, antwoordtypen, keuzelijsten en automatische invulling.
- Bestaande invoer blijft zichtbaar wanneer het opslaan van centrale instellingen mislukt.
- De bestaande centrale serverautorisatie, SQL-opslag, revisiecontrole en herstarttoepassing blijven leidend.

Lokale controles uitgevoerd met MariaDB en browser op telefoon- en laptopformaat. Live FiveM-tests op expliciet verzoek overgeslagen.

## 0.7.0

- Automatische Cavida Beheer-app voor bevoegde beheerders, zonder wijziging van de bestaande desktopvormgeving.
- Native appberichttransport en standalone characteridentiteit via de centrale bridge.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.

## 0.6.1 — testrelease

- Hoofdletterongevoelige interne e-mail en e-mailaanmaak.
- Korte mailboxvoorvertoning en volledige berichten na actuele postvakcontrole.
- Gedeelde Cavida-dossiers volledig lezen in laptopmail.


## 0.6.0 — testrelease

- Centrale interne mail koppelt laptopaccounts aan werkmail en gedeelde jobpostvakken.
- Gedeelde afzenders en postvakken worden bij ieder verzoek gecontroleerd; berichten en leesstatus zijn consistent.
- Bestaande laptopmail wordt zonder dubbele berichten overgenomen en de brondata blijft behouden.
- DUI-wereldschermen met lokale laptopprop, afstandsbeheer, opruimen en in-game afstelling per computermodel.

## 0.5.3 — testrelease

- Iframe-apps wachten op gecontroleerde gereedmelding voordat de sessietoken wordt verstuurd.
- Bestaande appvensters behouden hun sessie bij opnieuw openen.

## 0.5.2 — testrelease

- Testrelease voor in-game validatie.
- Cavida React-desktop met unieke laptop-, USB- en 4G-dockmetadata.
- Internetabonnementen, modeminstallatie, blijvende wifi en databundels.
- Externe app-export met FiveM-functiereferenties en zichtbare MEOS-launcher.
