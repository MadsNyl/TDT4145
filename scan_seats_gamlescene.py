from pool import cursor, conn
from utils import get_date


def run_old_scene():
    section = None
    gallery_row = 3
    balcony_row = 4
    standard_row = 10
    seatNumber = 1
    playId = None
    # Henter siste billettID fra scriptet som lager billetter for hovedscenen og legger til 1
    ticketId = cursor.execute("SELECT MAX(BillettID) FROM Billett").fetchone()[0] + 1

    with open("gamle-scene.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            date = get_date(line)
            if date:
                date = f"{date} 18:30:00"
                # hent riktig forestilling med dato og tidspunkt
                # TeaterStykke = 1 for "Størst av alt er kjærligheten"
                cursor.execute(
                    """
                    SELECT ForestillingID
                    FROM Forestilling
                    WHERE Spilldato = ?
                    AND TeaterStykke = 1
                    """,
                    (date,)
                )
                playId = cursor.fetchone()[0]
                continue

            if line == "Galleri":
                # lag seksjon med tittel "Galleri"
                # Starter på id 3
                # Sal = 2 for "Gamle Scene"
                cursor.execute(
                    """
                    INSERT INTO Seksjon 
                    (SeksjonID, Navn, Sal) 
                    VALUES (?, ?, ?)  
                    """,
                    (
                        3,
                        "Galleri",
                        2
                    )
                )
                conn.commit()
                section = "Galleri"
                continue
            
            if line == "Balkong":
                # lag seksjon med tittel "Balkong"
                # Fortsetter med id 4
                # Sal = 2 for "Gamle Scene"
                cursor.execute(
                    """
                    INSERT INTO Seksjon 
                    (SeksjonID, Navn, Sal) 
                    VALUES (?, ?, ?)  
                    """,
                    (
                        4,
                        "Balkong",
                        2
                    )
                )
                conn.commit()
                section = "Balkong"
                continue

            if line == "Parkett":
                # lag seksjon med tittel "Parkett"
                # Fortsetter med id 5
                # Sal = 2 for "Gamle Scene"
                cursor.execute(
                    """
                    INSERT INTO Seksjon 
                    (SeksjonID, Navn, Sal) 
                    VALUES (?, ?, ?)  
                    """,
                    (
                        5,
                        "Parkett",
                        2
                    )
                )
                conn.commit()
                section = "Parkett"
                continue


            for seat in line if section else []:
                if seat == "x":
                    continue
                
                # Lag sete med nummer og rad
                # Finner riktig radnummer å bruke
                if section == "Galleri":
                    row = gallery_row
                    sectionID = 3
                elif section == "Balkong":
                    row = balcony_row
                    sectionID = 4
                else:
                    row = standard_row
                    sectionID = 5

                cursor.execute(
                    """
                    INSERT INTO Stol
                    (Rad, StolNummer, Seksjon)
                    VALUES (?, ?, ?)
                    """,
                    (
                        row,
                        seatNumber,
                        sectionID
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
                            row,
                            seatNumber,
                            sectionID,
                            playId,
                            1
                        )
                    )
                    conn.commit()
                    ticketId += 1
                    seatNumber += 1
                    continue

                seatNumber += 1
                
            seatNumber = 1

            if section == "Galleri":
                gallery_row -= 1
            elif section == "Balkong":
                balcony_row -= 1
            else:
                standard_row -= 1