from pool import cursor, conn


# Her skal du kjøpe 9 voksenbilletter til forestillingen for Størst av alt er
# kjærligheten 3. februar, hvor det er 9 ledige billetter og hvor stolene er på
# samme rad. Stolene trenger ikke være ved siden av hverandre. Vi ønsker å få
# summert hva det koster å kjøpe disse billettene, men du trenger ikke ta
# hensyn til selve betalingen, den antar vi skjer på et annet system som dere
# ikke trenger å lage. Denne funksjonen skal implementeres i Python og SQL.

def get_available_seats():
    query = """
        SELECT Utvalg.*, Stol.Rad, Stol.StolNummer, Stol.Seksjon
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
        LEFT JOIN Billett ON Stol.Rad = Billett.Rad AND Stol.StolNummer = Billett.StolNummer AND Stol.Seksjon = Billett.Seksjon
        WHERE Billett.BillettID IS NULL
        LIMIT 9;
    """

    cursor.execute(query)
    tickets = cursor.fetchall()
    
    for ticket in tickets:
        print(ticket)


get_available_seats()


