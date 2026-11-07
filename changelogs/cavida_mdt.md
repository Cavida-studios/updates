# cavida_mdt 0.13.3

- CreateDispatchCall is vanaf het laden beschikbaar en meldt wanneer SQL nog niet gereed is.

# cavida_mdt 0.13.2

- Afgeschermde werkaccountprofielen voor jobs met uitsluitend deurrechten maken online deurenregie mogelijk zonder politie- of andere dienstrechten.
- Deurjobs krijgen een afzonderlijke accountscope en kunnen geen personen, registers of dossiers opvragen; bestaande dienstprofielen behouden voorrang.

# cavida_mdt 0.13.1

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.

# cavida_mdt 0.13.0

- Cavida Meldkamer integreert met bestaande MEOS-meldingen en gescheiden dienstendossiers; revisieconflicten bewaren handmatige wijzigingen.

# cavida_mdt

## 0.12.0

- Voertuigprofielen en mechanicwerkplaats tonen garage-/impoundstatus, bron, beschikbare livepositie, straatnaam, kaartpin en GPS-route.
- Afzonderlijke centraal beheerde rechten voor garage-inzage, live tracking en impound; mechanics zien standaard alleen live voertuigen binnen honderd meter.
- Impoundformulieren vanuit de laptop voor ondersteunde providers; SQL-audit registreert de aanvraag en claimt geen succesvolle inname bij een geannuleerd formulier.
- Rechtbank en Openbaar Ministerie krijgen een garagewerkruimte zonder automatische live tracking.

Gecontroleerd met echte lokale MariaDB, officiële API-/nativecontracten met mocks en telefoon-/laptopbrowser. Live FiveM-tests op verzoek overgeslagen.

## 0.11.0

- Automatische technische APK op laptop en telefoon: meetbare FiveM-schade en beschikbare JG-onderhoudsstatus bepalen de uitslag zonder handmatige checklist.
- Admins beheren automatische keuring, conditiegrenzen en verplichte JG-koppeling via Cavida Beheer.
- Meetwaarden, herkomst, voertuigidentiteit, meetmoment en gebruikte grenzen blijven in SQL bij de onveranderlijke keuring bewaard; handmatige beoordeling blijft apart beschikbaar.

Gecontroleerd met echte lokale MariaDB, native/API-mocks en telefoon/laptopbrowser; geen live FiveM-tests op verzoek.

## 0.10.1

- Politie krijgt een zichtbare tegel Huizen en woonadressen op het MEOS-startscherm.
- Woningen worden automatisch opgehaald bij het openen van een personenprofiel op laptop en telefoon, met server-side inzagerechten en zichtbare bronfouten.
- Bij wisselen van persoon worden oude woningresultaten verwijderd en achterhaalde antwoorden genegeerd.

Gecontroleerd in de echte politie-interface op telefoon en laptop, inclusief intrekking bij jobwissel. Geen live FiveM-tests.

## 0.10.0

- Woningregister op laptop en telefoon voor bevoegde diensten, inclusief rechtbank, met bronvermelding en geaudite inzage zonder politiedossierrechten.
- Eigen werkplaats met centraal instelbare APK-checklist, keuringsrechten en geldigheidsduur, onveranderlijke SQL-historie per werkplaats en atomische audit.
- Externe onderhoudsstatus, servicehistorie en kilometers via cavida_bridge; APK werkt ook zonder externe mechanicprovider.
- Character-, job-, rang- en baasstatus zijn aan sessies gebonden; jobwissels trekken oude schermen en antwoorden in op laptop, telefoon en web.

Gecontroleerd met lokale MariaDB, API-mocks en browser op telefoon/laptop. Live FiveM-tests op verzoek overgeslagen.

## 0.9.2

- Gedeelde dossiers in werkmail krijgen een opgemaakte dossierweergave met overdrachtskop, toelichting, hoofdstukken en leesbare Nederlandse datums.
- Nieuwe gedeelde mails worden atomisch aan hun opgeslagen dossierkopie gekoppeld; oudere gegenereerde mails worden alleen na controle van referentie, onderwerp, adressen, tijd en dienstrechten herkend.
- Oorspronkelijke mailtekst blijft bewaard en inklapbaar beschikbaar; gewone mails blijven tekstberichten zonder HTML-uitvoering.

Gecontroleerd met lokale MariaDB en de werkmailweergave op telefoon- en laptopformaat. Live FiveM-tests zoals afgesproken overgeslagen.

## 0.9.1

- Strafvoorstellen op telefoon als kaarten met volledige omschrijving en apart overzicht van aantal, RP-boete en celstraf.
- Desktop- en afdrukweergave behouden de tabel; geen wijziging aan dossiergegevens of strafbedragen.

Gecontroleerd met een lange artikelomschrijving op telefoon- en laptopformaat. Live FiveM-tests zoals afgesproken overgeslagen.

## 0.9.0

- 295 uitgewerkte FiveM-bepalingen toegevoegd: 151 RP-strafvoorstellen en 144 civiele, procedurele en disciplinaire bepalingen, met bronverwijzingen.
- Centrale admins beheren artikeltekst, categorie, afhandeling, beschikbaarheid, boete en celstraf op de laptop; SQL-opslag, revisies en audit bewaren bestaande dossiermomentopnamen.
- PV-workflow vernieuwd met duidelijke stappen, voortgang, controlekaarten, veldmeldingen en focus op het ontbrekende onderdeel.
- Straat- en gebiedsnamen bij de huidige locatie; verplaatsbare incidentpin en handmatig aanpasbaar adres worden samen in SQL bewaard.
- Opgemaakte leesweergave voor politie-, dienst-, ambulance- en gedeelde dossiers met hoofdstukken, medische gegevens, betrokkenen en strafvoorstellen.
- Dynamisch zoeken naar strafbare feiten op naam, code of categorie, met toetsenbordbediening en uitsluiting van al gekozen feiten.
- Leesbare Nederlandse datums voor epochwaarden in seconden of milliseconden; nieuwe PV-tijden zijn eenduidig UTC vastgelegd en worden in Europe/Amsterdam getoond.

Lokale MariaDB-, browser-, datum- en callbackcontractcontroles uitgevoerd. Live FiveM-tests op expliciet verzoek overgeslagen.

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
