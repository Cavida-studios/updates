# cavida_mdt

## 0.8.0

- Begeleid PV-stappenplan op telefoon en laptop, met SQL-concepten per character en server-side automatische invulling.
- Admins beheren stappen, vragen, antwoordtypen en verplichte velden via Cavida Beheer; concepten bewaren hun eigen vragenlijst.
- Eenmalige SQL-import van 9.789 officiële Nederlandse wetsartikelen uit 32 regelingen en 64 afzonderlijke RP-strafregels; bestaande gegevens blijven behouden.
- Doorzoekbaar juridisch naslagwerk met paginering, volledige teksten, bronversies en wetsverwijzingen in processen-verbaal.
- KMar-jobrollen en dienstnaam centraal instelbaar; militair strafrecht, tuchtrecht, ambtsinstructie en grenswetgeving opgenomen.
- Revisiecontrole, eigenaarschap, databasefouten en idempotente definitieve PV-opslag gecontroleerd op lokale MariaDB.

Lokale controles uitgevoerd met MariaDB en browser op telefoon- en laptopformaat. Live FiveM-tests op expliciet verzoek overgeslagen.

## 0.7.0

- MDT-instellingen migreren naar centraal beheer; bestaande dossiers en mail blijven behouden.
- Instellingen registreren automatisch in Cavida Beheer op Cavida Desktop.
- Centrale persistente instellingen met serverautorisatie, revisiecontrole en migratie van bestaande waarden.
- Geen handmatig te bewerken configbestanden meer; wijzigingen gelden na resourceherstart.

Lokale controles uitgevoerd. Live FiveM-tests zijn voor deze release op expliciet verzoek overgeslagen.

## 0.6.1 — testrelease

- Telefoonkop respecteert de statusbalk, camera-uitsparing en SDK-schermmarges.
- Compactere menurijen zonder dubbele pictogrammen; alle zes politieopties passen op een smal telefoonscherm.
- Zichtbare scrollbars en overbodige telefoonfooter verwijderd; scrollen blijft werken.


## 0.6.0 — testrelease

- Hoofdletterongevoelig zoeken, e-mail en jobcontrole.
- Ambulancewerkplek met patiëntendossiers, behandelingen, voorgeschiedenis en versiehistorie.
- Gedocumenteerde OSP-momentopnamen met bron, tijdstip, nabijheid en dienstcontrole.
- Dossiers delen als vaste kopie met volledige dienstmail in het info-postvak.
- Cavida-telefooninterface voor RoadPhone Pro, LB Phone en SD via LB-compatibiliteit.


## 0.5.0 — testrelease

- Globale zoekbalk met categorieën, Ctrl+K en rechtstreeks openen van personen, voertuigen en bevoegde dossiers.
- Personen, voertuigen en dossiers opzoeken en koppelen binnen rapporten, met herkenbare resultaten en bescherming tegen dubbele koppelingen.
- Vernieuwde Cavida-vormgeving met twee dossierkolommen, consistente navigatie, rustige panelen en aangepaste mobiele indeling.
- Defensie en army hebben dezelfde politiemogelijkheden, met eigen instelbare jobs, afdelingsnaam en defensie.com-werkmail.
- Globaal zoeken en dezelfde personenzoeker zijn ook beschikbaar voor dienstregistraties, met behoud van dienst- en ranggrenzen.


## 0.4.1 — testrelease

- Zoekacties en andere leesverzoeken wachten niet meer op achtergrondverkeer of schrijfverzoeken; dubbele lopende leesverzoeken worden samengevoegd.
- Grote API-antwoorden worden via kleine, sessiegebonden delen opgehaald om vastlopende antwoorden op de native gamepoort te voorkomen.
- Online charactercontrole gebruikt een gecontroleerde bronkoppeling en blijft bij ieder verzoek de actuele frameworkrol controleren.
- Zoekscherm toont voortgang en legt het minimum van twee zoektekens uit; achtergrondvernieuwing stapelt niet op.


## 0.4.0 — testrelease

- Automatische characteradressen zoals j.devries@police.com; medewerkers kiezen uitsluitend hun eigen wachtwoord.
- Werkmail en laptopmail gebruiken dezelfde interne berichten; iedere job krijgt info en echte bazen krijgen management.
- Oude adressen en berichten blijven binnen de bijbehorende dienst behouden; managment werkt als management-alias.
- De externe website bevat geen livemap of kaartdownloads meer; de in-game kaart en portobediening blijven beschikbaar.

## 0.3.2 — testrelease

- Herstel van browserverbindingen die na het eerste antwoord vastlopen op de gamepoort.
- HTTP-antwoorden sluiten de verbinding expliciet; gecomprimeerde assets en versiecache blijven actief.

## 0.3.1 — testrelease

- Herstel van vastlopende grote websitebestanden via gecomprimeerde, begrensde overdrachten op de gamepoort.
- Versiegebonden browsercache voor openbare code, stijlen en kaarttegels; servercache voorkomt herhaald bestand lezen.
- Kleine assetverzoeken worden gespreid om de native HTTP-requestlimiet te respecteren.
- Inloggen, dossiers en andere persoonlijke API-antwoorden blijven buiten de publieke assetcache.

## 0.3.0 — testrelease

- Cavida Overheid met afzonderlijke werkruimtes voor ambulance, brandweer, rechtbank, Openbaar Ministerie, advocatuur en gemeente.
- Dienst- en ranggebonden dossiers, wijzigingshistorie, werkmail, livekaart en optionele tRadio-bediening.
- Openbare startpagina met vacatures en wetboek, sollicitaties en persoonsgerichte rechtbankberichten.
- Discord-codeflow met dezelfde store-applicatie, servergeverifieerde characterkoppelingen en afgeschermde burgersessies.
- Diensten, toegangsrollen, dossiertypen, frequenties en publicaties zijn in-game te beheren.

## 0.2.1 — testrelease

- Herstel van de iframe-handshake en de sleepbediening van de livekaart.
- Zakelijke Cavida-overheidsstijl met dienstentegels en leesbare formulieren.
- Externe inlogpagina blijft bereikbaar tijdens database-opstart en toont de portaalstatus.
- Kaarttegels laden buiten de game gespreid om de FXServer-requestlimiet te respecteren.

## 0.2.0 — testrelease

- Testrelease voor in-game en tRadio-validatie.
- Tegelinterface met meldkamer, OneSync-livemap en tRadio-bediening.
- Persoonsgebonden werkmail en uitsluitend eigen in-game wachtwoordbeheer.
- Extern portaal op de serverpoort met actuele politierolcontrole per verzoek.




## 0.1.2 — in ontwikkeling

Nog geen gepubliceerde release. Deze metadata bevestigt uitsluitend de registratie bij de centrale Cavida-versiecontrole.

- Gerichte registratiemeldingen en vereiste laptopversie met FiveM-functiereferenties.

- MEOS-icoon blijft zichtbaar met uitleg bij ontbrekend internet of rechten.
