from pool import cursor, conn


# Her skal du kjøpe 9 voksenbilletter til forestillingen for Størst av alt er
# kjærligheten 3. februar, hvor det er 9 ledige billetter og hvor stolene er på
# samme rad. Stolene trenger ikke være ved siden av hverandre. Vi ønsker å få
# summert hva det koster å kjøpe disse billettene, men du trenger ikke ta
# hensyn til selve betalingen, den antar vi skjer på et annet system som dere
# ikke trenger å lage. Denne funksjonen skal implementeres i Python og SQL.

def get_available_seats():
    query = """
        SELECT Stol.Rad, Stol.StolNummer, Seksjon.Navn
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



# Her skal du implementere et Pythonprogram (med bruk av SQL) som tar inn
# en dato og skriver ut hvilke forestillinger som finnes på denne datoen og lister
# opp hvor mange billetter (dvs. stoler) som er solgt. Ta også med forestillinger
# hvor det ikke er solgt noen billetter.


