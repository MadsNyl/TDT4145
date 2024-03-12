from pool import cursor, conn


# Her skal du kjøpe 9 voksenbilletter til forestillingen for Størst av alt er
# kjærligheten 3. februar, hvor det er 9 ledige billetter og hvor stolene er på
# samme rad. Stolene trenger ikke være ved siden av hverandre. Vi ønsker å få
# summert hva det koster å kjøpe disse billettene, men du trenger ikke ta
# hensyn til selve betalingen, den antar vi skjer på et annet system som dere
# ikke trenger å lage. Denne funksjonen skal implementeres i Python og SQL.

def get_available_seats():
    query = """
        SELECT Stol.Rad, Stol.StolNummer, Stol.Seksjon, Seksjon.Navn
        FROM
        (
            SELECT Stol.Rad, Stol.Seksjon, COUNT(Stol.Rad) AS stoler_per_rad, Seksjon.Navn, Sal.Navn, TeaterStykke.Navn
            FROM Stol
            INNER JOIN Seksjon ON Stol.Seksjon = Seksjon.SeksjonID
            INNER JOIN Sal ON Seksjon.Sal = Sal.SalID
            INNER JOIN TeaterStykke ON Sal.SalID = TeaterStykke.Sal
            WHERE TeaterStykke.Navn = 'Størst av alt er kjærligheten'
            GROUP BY Stol.Rad, Stol.Seksjon
            HAVING stoler_per_rad - (
                SELECT COUNT(*)
                FROM Billett
                INNER JOIN Forestilling ON Billett.Forestilling = Forestilling.ForestillingID
                WHERE Billett.Rad = Stol.Rad AND Billett.Seksjon = Stol.Seksjon AND Forestilling.Spilldato = '2024-02-03 18:30:00'
            ) >= 9
            ORDER BY Stol.Seksjon
            LIMIT 1
        ) AS Utvalg
        INNER JOIN Stol ON Utvalg.Rad = Stol.Rad AND Utvalg.Seksjon = Stol.Seksjon
        INNER JOIN Seksjon ON Stol.Seksjon = Seksjon.SeksjonID
        LEFT JOIN Billett ON Stol.Rad = Billett.Rad AND Stol.StolNummer = Billett.StolNummer AND Stol.Seksjon = Billett.Seksjon
        WHERE Billett.BillettID IS NULL
        LIMIT 9;
    """

    cursor.execute(query)
    tickets = cursor.fetchall()
    
    return tickets


def insert_tickets(tickets: list[tuple]):
    # Hent siste billettID og legg til 1
    ticketId = cursor.execute("SELECT MAX(BillettID) FROM Billett").fetchone()[0] + 1

    # Hent Pris for voksenbillett
    cursor.execute(
        """
            SELECT BillettPris.BilettPrisID, Kundegruppe.KundegruppeID
            FROM BillettPris
            INNER JOIN TeaterStykke ON BillettPris.TeaterStykke = TeaterStykke.StykkeID
            INNER JOIN Kundegruppe ON BillettPris.Kundegruppe = Kundegruppe.KundegruppeID
            WHERE TeaterStykke.Navn = 'Størst av alt er kjærligheten'
            AND Kundegruppe.Navn = 'Ordinær';
        """
    )

    ticket_info = cursor.fetchone()

    # Hent forestillingID
    cursor.execute(
        """
            SELECT ForestillingID
            FROM Forestilling
            INNER JOIN TeaterStykke ON Forestilling.TeaterStykke = TeaterStykke.StykkeID
            WHERE Spilldato = '2024-02-03 18:30:00'
            AND TeaterStykke.Navn = 'Størst av alt er kjærligheten';
        """
    )

    playId = cursor.fetchone()[0]

    for ticket in tickets:
        cursor.execute(
            """
                INSERT INTO Billett 
                (BillettID, Pris, Rad, StolNummer, Seksjon, Forestilling, Kundeprofil)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """,
            (
                ticketId,
                ticket_info[0],
                ticket[0],
                ticket[1],
                ticket[2],
                playId,
                ticket_info[1]
            )   
        )
        conn.commit()
        ticketId += 1


def calculate_total_tickets_price():
    query = """
        SELECT BillettPris.Pris * 9 AS TotalPris
        FROM Forestilling
        INNER JOIN TeaterStykke ON Forestilling.TeaterStykke = TeaterStykke.StykkeID
        INNER JOIN BillettPris ON TeaterStykke.StykkeID = BillettPris.TeaterStykke
        INNER JOIN Kundegruppe ON BillettPris.Kundegruppe = Kundegruppe.KundegruppeID
        WHERE Forestilling.Spilldato = '2024-02-03 18:30:00'
        AND Kundegruppe.Navn = 'Ordinær';
    """

    cursor.execute(query)
    total_price = cursor.fetchone()

    return total_price[0]


# Her skal du implementere et Pythonprogram (med bruk av SQL) som tar inn
# en dato og skriver ut hvilke forestillinger som finnes på denne datoen og lister
# opp hvor mange billetter (dvs. stoler) som er solgt. Ta også med forestillinger
# hvor det ikke er solgt noen billetter.

def get_show_and_tickets_purchased(date: str):
    query = """
        SELECT tstykke.Navn, COUNT(b.BillettID) AS AntallSolgteBilletter
        FROM Forestilling AS f
        INNER JOIN TeaterStykke AS tstykke ON f.TeaterStykke = tstykke.StykkeID
        LEFT JOIN Billett b ON f.ForestillingID = b.Forestilling
        WHERE DATE(f.Spilldato) = ?
        GROUP BY f.ForestillingID
        ORDER BY f.ForestillingID;
    """

    # Utfør spørringen
    cursor.execute(query, (date,))

    # Hent og skriv ut resultatene
    plays = cursor.fetchall()
    return plays


# Vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som
# opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke,
# navn på skuespiller og rolle.

def get_actors_and_roles():
    query = """
        SELECT DISTINCT TeaterStykke.Navn, Rolle.Navn, Ansatt.Navn
        FROM TeaterStykke
        INNER JOIN Akt ON TeaterStykke.StykkeID = Akt.TeaterStykke
        INNER JOIN HarRoller ON Akt.AktID = HarRoller.Akt
        INNER JOIN Rolle ON HarRoller.Rolle = Rolle.RolleID
        INNER JOIN SpillerSom ON Rolle.RolleID = SpillerSom.Rolle
        INNER JOIN Skuespiller ON SpillerSom.Skuespiller = Skuespiller.SkuespillerID
        INNER JOIN Ansatt ON Skuespiller.SkuespillerID = Ansatt.AnsattID
        ORDER BY TeaterStykke.Navn, Ansatt.Navn;
    """

    cursor.execute(query)
    actors_and_roles = cursor.fetchall()

    return actors_and_roles


# Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner
# hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og
# hvilket skuespill det skjedde.

def get_actors_played_together(actor: str):
    query = """
        SELECT DISTINCT A1.Navn, A2.Navn, TeaterStykke.Navn
        FROM SpillerSom
        INNER JOIN Skuespiller AS S1 ON SpillerSom.Skuespiller = S1.SkuespillerID
        INNER JOIN Ansatt A1 ON S1.SkuespillerID = A1.AnsattID
        INNER JOIN HarRoller AS HR1 ON SpillerSom.Rolle = HR1.Rolle
        INNER JOIN Akt ON HR1.Akt = Akt.AktID
        INNER JOIN HarRoller AS HR2 ON Akt.AktID = HR2.Akt
        INNER JOIN SpillerSom AS SS2 ON HR2.Rolle = SS2.Rolle
        INNER JOIN Skuespiller S2 ON SS2.Skuespiller = S2.SkuespillerID
        INNER JOIN Ansatt A2 ON S2.SkuespillerID = A2.AnsattID
        INNER JOIN TeaterStykke ON Akt.TeaterStykke = TeaterStykke.StykkeID
        WHERE A1.Navn != A2.Navn AND A1.Navn = ?
        ORDER BY A2.Navn;
    """

    cursor.execute(query, (actor, ))
    actors_played_together = cursor.fetchall()
    
    for actor in actors_played_together:
        print(actor)

    return actors_played_together

get_actors_played_together("Arturo Scotti")
def best_seller():
    query = '''
        SELECT tstykke.Navn as Forestillingsnavn, f.Spilldato, COUNT(b.BillettID) AS AntallSolgteBilletter
        FROM Forestilling AS f
        INNER JOIN TeaterStykke AS tstykke ON f.TeaterStykke = tstykke.StykkeID
        LEFT JOIN Billett AS b ON b.Forestilling = f.ForestillingID
        GROUP BY f.ForestillingID
        ORDER BY AntallSolgteBilletter DESC
        '''
    cursor.execute(query)
    plays = cursor.fetchall()
    return plays

best_seller()