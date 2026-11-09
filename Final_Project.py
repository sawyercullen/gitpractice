
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
