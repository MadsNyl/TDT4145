from pool import cursor, conn

#
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
            WHERE TeaterStykke.Navn = 'StÃ¸rst av alt er kjÃ¦rligheten'
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
            WHERE TeaterStykke.Navn = 'StÃ¸rst av alt er kjÃ¦rligheten'
            AND Kundegruppe.Navn = 'OrdinÃ¦r';
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
            AND TeaterStykke.Navn = 'StÃ¸rst av alt er kjÃ¦rligheten';
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
        AND Kundegruppe.Navn = 'OrdinÃ¦r';
    """

    cursor.execute(query)
    total_price = cursor.fetchone()

    return total_price[0]

get_available_seats()

# Her skal du implementere et Pythonprogram (med bruk av SQL) som tar inn
# en dato og skriver ut hvilke forestillinger som finnes på denne datoen og lister
# opp hvor mange billetter (dvs. stoler) som er solgt. Ta også med forestillinger
# hvor det ikke er solgt noen billetter.

def get_show_and_tickets_purchased(dato):
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
    cursor.execute(query, (dato,))

    # Hent og skriv ut resultatene
    forestillinger = cursor.fetchall()
    if forestillinger:
        print("ForestillingID, Navn på TeaterStykke, Antall Solgte Billetter")
        for forestilling in forestillinger:
            print(forestilling)
    else:
        print("Ingen forestillinger funnet på denne datoen.")



def format_1(forestillinger: tuple) -> str:
    return_string = ""
    for value in forestillinger:
        return_string += f"Forestilling:\t\t    Antall Biletter Solgt: {value[1]} \n"
    return return_string

dato = '2024-02-06'
get_show_and_tickets_purchased(dato)

