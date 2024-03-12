from pool import cursor, conn
from utils import get_date


def run_main_scene():
    section = None
    row = 18
    balcony_row = 4
    seatNumber = 1
    playId = None
    ticketId = 1

    with open("hovedscenen.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            date = get_date(line)
            if date:
                date = f"{date} 19:00:00"
                # hent riktig forestilling med dato og tidspunkt
                # TeaterStykke = 2 for "Kongsemnene"
                cursor.execute(
                    """
                    SELECT ForestillingID
                    FROM Forestilling
                    WHERE Spilldato = ?
                    AND TeaterStykke = 2
                    """,
                    (date,)
                )
                playId = cursor.fetchone()[0]
                continue

            if line == "Galleri":
                # lag seksjon med tittel "Galleri"
                # Starter på id 1
                cursor.execute(
                    """
                    INSERT INTO Seksjon 
                    (SeksjonID, Navn, Sal) 
                    VALUES (?, ?, ?)  
                    """,
                    (
                        1,
                        "Galleri",
                        1
                    )
                )
                conn.commit()
                section = "Galleri"
                continue

            if line == "Parkett":
                # lag seksjon med tittel "Parkett"
                # Fortsetter med id 2 
                # Sal = 1 for "Hovedscenen"
                cursor.execute(
                    """
                    INSERT INTO Seksjon 
                    (SeksjonID, Navn, Sal) 
                    VALUES (?, ?, ?)  
                    """,
                    (
                        2,
                        "Parkett",
                        1
                    )
                )
                conn.commit()
                section = "Parkett"
                continue

            for seat in line if section else []:
                if seat == "x" or not section:
                    continue
                
                # Lag sete med nummer og rad
                cursor.execute(
                    """
                    INSERT INTO Stol
                    (Rad, StolNummer, Seksjon)
                    VALUES (?, ?, ?)
                    """,
                    (
                        row if section == "Parkett" else balcony_row,
                        seatNumber,
                        1 if section == "Galleri" else 2
                    )
                )    
                conn.commit()

                if seat == "1":
                    # lag  billett
                    cursor.execute(
                        """
                        INSERT INTO Billett
                        (BillettID, Pris, Rad, StolNummer, Seksjon, Forestilling, Kundeprofil)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            ticketId,
                            1,
                            row if section == "Parkett" else balcony_row,
                            seatNumber,
                            1 if section == "Galleri" else 2,
                            playId,
                            1
                        )
                    )
                    conn.commit()
                    ticketId += 1
                    seatNumber += 1
                    continue

                seatNumber += 1

            if section == "Galleri":
                balcony_row -= 1
            elif section == "Parkett":
                row -= 1



                
