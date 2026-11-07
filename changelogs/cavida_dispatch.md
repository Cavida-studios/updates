# cavida_dispatch 1.0.3

- Telefoonadapters kunnen tijdens de opstart registreren. RoadPhone ontvangt ook vóór SQL-gereedmelding een geldig antwoord.
- CreateIncident en IngestRecording geven tijdens opstart een antwoord waarmee integraties later opnieuw kunnen proberen.

# cavida_dispatch 1.0.2

- Deuren van ondersteunde providers verschijnen automatisch volgens afzonderlijke kijk- en bedienrechten per job, rang en deuruitzondering in Cavida Beheer.
- Jobs met uitsluitend deurrechten krijgen geen toegang tot meldingen of MDT-personengegevens; bestaande expliciete deurbeperkingen blijven behouden.
- Native verzoeken en webantwoorden blijven geldige JSON geven tijdens opstart; lege antwoorden worden veilig afgehandeld zonder mutaties automatisch te herhalen.

# cavida_dispatch 1.0.1

- Server- en clientinitialisatie wachten op gereedmelding van Cavida Bridge, centrale instellingen en SQL.
- Eigen Cavida-afhankelijkheden en SQL-initialisatie worden gecontroleerd voordat de resource gereed wordt gemeld; bestaande gegevens blijven behouden.
- Meldkamerkaart behoudt geografische verhoudingen met zoomen, verschuiven en efficiënter laden; operationele oproepbediening aangescherpt.
- SmartFires-brandmeldingen worden met SQL-deduplicatie en bronstatus in de meldkamer verwerkt; uitgiftes blijven onder regie van de centralist.
- Deurenregie toont veilige, vrijgegeven deurposities en slotstatussen; admincatalogus, slotbediening en SQL-audit met actuele functie- en statuscontrole.
- Inkomende meldingen geven pas na succesvolle SQL-opslag een melding aan bevoegde online centralisten.

# cavida_dispatch 1.0.0

- Eigen React-meldkamer op Cavida Desktop en web met meldingen, eenheden, statusbeheer en portobediening.
- 112-intake met dienstkeuze en SQL-wachtrij, RoadPhone-nummerprovider en providerafhankelijke telefoonbediening.
- Optionele audiotranscriptie, centrale beheerinstellingen en server-side sessie- en dienstrechten.
- Optionele eigen privé-noodgesprekken via pma-voice: aannemen, wachten, hervatten en beëindigen; bestaande gesprekken worden niet overgenomen.
