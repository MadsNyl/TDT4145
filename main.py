from utils import (
    run_sql_script,
    convert_tickets_to_string,
    convert_actors_and_roles_to_string,
    convert_plays_to_string,
    convert_actors_played_together_to_string,
    convert_most_sold_plays_to_string,
    validate_date
)

from scan_seats_hovedscenen import run_main_scene
from scan_seats_gamlescene import run_old_scene

from queries import (
    get_available_seats,
    calculate_total_tickets_price,
    insert_tickets,
    get_actors_and_roles,
    get_show_and_tickets_purchased,
    get_actors_played_together,
    best_seller
)

def delete_database():
    # Dropper og lager databasen på nytt
    run_sql_script("drop.sql")

def setup_database():
    print("Setter opp databasen...")
    run_sql_script("create.sql")
    # Popullerer databasen med data
    print("Popullerer databasen med data...")
    run_sql_script("insert.sql")

    # Skanner setene for hovedscenen og gamle scene og lager seksjoner, stoler og billetter
    print("Skanner setene for Hovedscenen og lager seksjoner, stoler og billetter...")
    run_main_scene()
    print("Skanner setene for Gamle scene og lager seksjoner, stoler og billetter...")
    run_old_scene()

def display_menu():
    print("\n\n\n1. Finn og kjøp 9 ledige seter på samme rad, og kalkuler totalpris.")
    print("2. Hent forestillinger for en gitt dato, for å få informasjon om antall billetter solgt per forestilling.")
    print("3. Hent alle skuespillere og deres roller for teaterstykkene.")
    print("4. Hent sortert liste over mestselgende forestillinger")
    print("5. Hent informasjon om skuespillere en gitt skuespiller har spilt sammen med.")
    print("6. Avslutt")

if __name__ == "__main__":

    delete_database()
    setup_database()

    # Kjører programmet
    while True:

        display_menu()
        choice = input("\nVennligst velg et alternativ (1 - 6): \n")

        if choice == "6":
            print("Avslutter programmet...")
            break

        elif choice == "1":
            try:
                tickets = get_available_seats()
                insert_tickets(tickets)
                tickets = convert_tickets_to_string(tickets)
                if not len(tickets):
                    print("Fant ingen ledige seter")
                    continue
                print("Dine billetter:")
                print(tickets)
                total_price = calculate_total_tickets_price()
                print(f"Totalpris for 9 voksenbilletter: {total_price} kr")
            except:
                print("Det skjedde en feil. Prøv igjen.")
                continue
        
        elif choice == "2":
            try:
                date = input("Vennligst skriv inn en dato (YYYY-MM-DD): \n")
                if not validate_date(date):
                    print("\nUgyldig dato. Prøv igjen.")
                    continue
                plays = get_show_and_tickets_purchased(date)
                plays = convert_plays_to_string(plays)
                print(f"Forestillinger og antall billetter solgt for {date}: ")
                print(plays)
            except:
                print("Det skjedde en feil. Prøv igjen.")
                continue

        elif choice == "3":
            try:
                actors = get_actors_and_roles()
                actors = convert_actors_and_roles_to_string(actors)
                print("Skuespillere og roller for hvert teaterstykke: ")
                print(actors)
            except:
                print("Det skjedde en feil. Prøv igjen.")
                continue
        
        elif choice == "4":
            try:
                plays = best_seller()
                plays = convert_most_sold_plays_to_string(plays)
                print("Mestselgende forestillinger: ")
                print(plays)
            except:
                print("Det skjedde en feil. Prøv igjen.")
                continue
        
        elif choice == "5":
            try:
                actor = input("Vennligst skriv inn et skuespillernavn: \n")
                actorteams = get_actors_played_together(actor)
                if not len(actorteams):
                    print(f"{actor} har ikke spilt sammen med noen.")
                    continue
                actorteams = convert_actors_played_together_to_string(actorteams)
                print("Skuespillere som har spilt sammen: ")
                print(actorteams)
            except Exception as e:
                print("Det skjedde en feil. Prøv igjen.")
                continue
