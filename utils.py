from datetime import datetime
from pool import cursor, conn


# Hent dato fra linje
def get_date(line: str) -> str | None:
    if "Dato" in line:
            words = line.split()
            for word in words:
                if len(word) == 10 and word[4] == "-" and word[7] == "-":
                    return word
    return None

# Kjør SQL-script
def run_sql_script(script_path: str) -> None:
    with open(script_path, 'r', encoding="utf-8") as script_file:
        sql_script = script_file.read()
        cursor.executescript(sql_script)
        conn.commit()

# Hent alle rader om billetter og omgjør til liste
def convert_tickets_to_string(tickets: list[tuple]) -> str:
    return_string = ""
    for ticket in tickets:
        return_string += f"Rad: {ticket[0]}, Stol: {ticket[1]}, Seksjon: {ticket[3]}\n"
    return return_string

# Hent alle rader om skuespillere og omgjør til liste
def convert_actors_and_roles_to_string(actors: list[tuple]) -> str:
    return_string = ""
    for actor in actors:
        return_string += f"Teaterstykke: {actor[0]}, Skuespiller: {actor[2]}, Rolle: {actor[1]}\n"
    return return_string

# Hent alle rader om teaterstykker og omgjør til liste
def convert_plays_to_string(plays: list[tuple]) -> str:
    return_string = ""
    for play in plays:
        return_string += f"Forestilling: {play[0]}, Antall Biletter Solgt: {play[1]}\n"
    return return_string

# Hent alle rader om skuespillere som har spilt sammen og omgjør til liste
def convert_actors_played_together_to_string(actorteams: list[tuple]) -> str:
    return_string = ""
    for actor in actorteams:
        return_string += f"Teaterstykke: {actor[2]}, Valgt Skuespiller: {actor[0]}, Spiller mot: {actor[1]}\n"
    return return_string

# Hent alle rader om mest solgte teaterstykker og omgjør til liste
def convert_most_sold_plays_to_string(plays: list[tuple]) -> str:
    return_string = ""
    standings = 1
    for play in plays:
        return_string += f"{standings}. Teaterstykke: {play[0]}, Dato: {play[1]}, Antall Biletter Solgt: {play[2]}\n"
        standings += 1
    return return_string


# Sjekk om dato er gyldig
def validate_date(date: str) -> bool:
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False