# Database-prosjekt Del 2
**Mats Nylund & Christian Stensøe**

## Kjøring av programmet

For å kjøre programmet, følg disse stegene:

1. **Naviger til TDT4145-mappen** hvor programmet ligger.

    ```bash
    cd path/to/project-folder
    ```

2. **Start programmet** ved å kjøre følgende kommando i terminalen. Dette vil slette eksisterende data i databasen og opprette den på nytt med forhåndsbestemte data som kreves for prosjektet:

    ```bash
    python3 main.py
    ```
    - **Sletter eksisterende data:** `drop.sql` sletter eksisterende tabeller. 

    - **Oppretter databasen på nytt:** `create.sql` Tabeller i databasen opprettes på nytt.

    - **Populerer databasen:** `insert.sql`Databasen blir fylt med forhåndsbestemte data som er nødvendige for at programmet skal kunne kjøre som forventet.

    - **Populerer databasen med billetter:** `scan_seats_gamlescene.py` og `scan_seat_hovedscenen.py` leser hver sin tekstfil og lager seksjoner, stoler og billetter. 

    - **Klar for bruk:** Nå er systemet klart til å ta imot input fra brukeren for å kjøre forskjellige brukerhistorier.


3. **Velg brukerhistorie** du ønsker å kjøre ved å taste inn et tall mellom `1` og `6`. Velger du `6`, avsluttes programmet. For noen av brukerhistoriene vil du bli bedt om å oppgi ytterligere informasjon som programmet trenger.

## Brukerhistorier

### 1. Finn og kjøp 9 ledige seter på samme rad, og kalkuler totalpris
**Forklaring:** Dette alternativet lar deg finne og kjøpe 9 sammenhengende seter på samme rad for en bestemt forestilling. Programmet vil deretter kalkulere totalprisen for disse billettene. Her vil du ikke bli promptet med noe ekstra input-data. Programmet kjører og spørringen returnerer første rad den finner med 9 seter tilgjenglig. For å bekrefte at setene faktisk er blitt "kjøpt" kan du kjøre **brukerhistoire 4** og se at antall solgte billetter på den aktuelle forestillingen øker med ni for hver gang programmet kjører denne spørringen. 

**Eksempeldata:** None

### 2. Hent forestillinger for en gitt dato, for å få informasjon om antall billetter solgt per forestilling.
**Forklaring:** Velg dette alternativet for å få en oversikt over alle forestillinger på en spesifikk dato, samt hvor mange billetter som er solgt til hver av dem.

**Eksempeldata:** Ved å spørre etter forestillinger den "2024-02-03", vil programmet liste opp alle tilgjengelige forestillinge den dagen med antall solgte billetter.

To forestillinger med billetter solg:
```bash
2024-02-03 
```
En forestillinger uten noen solgte billetter. 
```bash
2024-02-05 
```
To forestillinger uten noen solgte billetter. 
```bash
2024-02-06
```

### 3. Hent alle skuespillere og deres roller for teaterstykkene.
**Forklaring:** Dette valget gir en oversikt over alle skuespillere og hvilke roller de har i forskjellige teaterstykker.

**Eksempeldata:** None

### 4. Hent sortert liste over mestselgende forestillinger.
**Forklaring:** Se hvilke forestillinger som har solgt flest billetter. Listen er sortert fra høyest til lavest.

**Eksempeldata:** None

### 5. Hent informasjon om skuespillere en gitt skuespiller har spilt sammen med.
**Forklaring:** Finn ut hvilke skuespillere en bestemt skuespiller har delt scene med i forskjellige teaterstykker.

**Eksempeldata:** Ved å oppgi skuespillernavnet "Thomas Jensen Takyi", vil programmet vise en liste over alle skuespillere Thomas Jensen Takyi har spilt sammen med. Obs! Skriv inn navn med store forbokstaver. Eller så vil dere få en tilbakemelding om at det ikke finnes noen som spiller med valgt skuespiller.
Skuespiller fra "Kongsemnene". 
```bash
Thomas Jensen Takyi
```
Skuespiller fra "Størst av alt er kjærligheten". 
```bash
Tor Ivar Hagen
```

### 6. Avslutter programmet.
**Forklaring:** Velger du dette alternativet, vil programmet avslutte.
