
reservations = {
    "Sawyer Cullen": {
        "date": "2026-07-10",
        "people": 4,
        "trip": "Blackfoot"
    },
    "Teddy Higgins": {
        "date": "2026-07-11",
        "people": 6,
        "trip": "Clark Fork"
    },
    "Harry Higgins": {
        "date": "2026-07-12",
        "people": 3,
        "trip": "Blackfoot"
    }
}

def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. View equipment and guides")
    print("4. Update equipment and guides")
    print("5. Revenue report")
    print("6. Run simulation")
    print("7. Save and exit")


def view_reservations():
    print("\nRafting Reservations")

    for name, details in reservations.items():
        print("Customer:", name)
        print("Date:", details["date"])
        print("People:", details["people"])
        print("Trip:", details["trip"])
        print()

def add_reservation():
    name = input("Enter customer name: ").strip()

    if name == "":
        print("Customer name cannot be empty.")
        return

    if name in reservations:
        print("Updating existing reservation.")
    else:
        print("Adding new reservation.")

    date = input("Enter trip date (YYYY-MM-DD): ")
    
    while True:
        try:
            people = int(input("Enter number of people: "))

            if people > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    trip = input("Enter river (Blackfoot or Clark Fork): ")

    reservations[name] = {
        "date": date,
        "people": people,
        "trip": trip
    }
1

print("Reservation saved!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_reservations()
        elif choice == "2":
            add_reservation()
        elif choice == "7":
            print("Goodbye!")
            break
        elif choice in ["3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid choice. Please choose 1-7.")

main()


import csv

# This dictionary stores all customer reservations.
reservations = {}


# This function loads reservations from the CSV file.
def load_reservations():
    global reservations

    try:
        with open("reservations.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                reservations[row["name"]] = {
                    "river": row["river"],
                    "date": row["date"],
                    "people": int(row["people"])
                }

    except FileNotFoundError:
        reservations = {
            "John Smith": {
                "river": "Blackfoot River",
                "date": "2026-07-10",
                "people": 4
            },
            "Sarah Jones": {
                "river": "Clark Fork River",
                "date": "2026-07-11",
                "people": 6
            },
            "Mike Wilson": {
                "river": "Blackfoot River",
                "date": "2026-07-12",
                "people": 3
            }
        }

        save_reservations()


# This function saves all reservations to the CSV file.
def save_reservations():
    with open("reservations.csv", "w", newline="") as file:
        headings = ["name", "river", "date", "people"]
        writer = csv.DictWriter(file, fieldnames=headings)

        writer.writeheader()

        for name, details in reservations.items():
            writer.writerow({
                "name": name,
                "river": details["river"],
                "date": details["date"],
                "people": details["people"]
            })


# This function displays the menu options.
def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. Record a rafting trip - Coming soon")
    print("4. View trip history - Coming soon")
    print("5. Save and exit")


# This function displays all customer reservations.
def view_reservations():
    print("\nCurrent Reservations")

    if len(reservations) == 0:
        print("No reservations found.")

    for name, details in reservations.items():
        print("\nCustomer:", name)
        print("River:", details["river"])
        print("Date:", details["date"])
        print("People:", details["people"])


# This function gets a valid number of people.
def get_people():
    while True:
        try:
            people = int(input("Enter number of people: "))

            if people > 0:
                return people
            else:
                print("Enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


# This function adds a new reservation or updates an existing one.
def add_reservation():
    name = input("Enter customer name: ").strip()

    if name == "":
        print("Customer name cannot be empty.")
        return

    if name in reservations:
        print("Updating existing reservation.")
    else:
        print("Adding new reservation.")

    river = input("Enter river: ").strip()
    date = input("Enter trip date (YYYY-MM-DD): ").strip()
    people = get_people()

    if river == "" or date == "":
        print("River and date cannot be empty.")
        return

    reservations[name] = {
        "river": river,
        "date": date,
        "people": people
    }

    print("Reservation saved!")


def main():
    load_reservations()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_reservations()

        elif choice == "2":
            add_reservation()

        elif choice == "3" or choice == "4":
            print("Coming soon")

        elif choice == "5":
            save_reservations()
            print("Reservations saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")


main()

