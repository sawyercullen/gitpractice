
def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. View equipment and guides")
    print("4. Update equipment and guides")
    print("5. Revenue report")
    print("6. Run simulation")
    print("7. Save and exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            print("Coming Soon")
        else:
            print("Invalid choice. Please choose 1-7.")


# This starts the program.
main()
