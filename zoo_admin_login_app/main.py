"""Main program for the Zoo Admin Login System."""

from auth import login, logout
from zoo_admin import view_animals, add_animal, remove_animal


def show_menu() -> None:
    """Display the admin menu options."""
    print("\nZoo Admin Menu")
    print("1. View animals")
    print("2. Add animal")
    print("3. Remove animal")
    print("4. Logout")


def main() -> None:
    """Run the zoo admin login system."""
    print("Welcome to the Zoo Admin Login System")

    username = input("Username: ")
    password = input("Password: ")
    current_user = login(username, password)

    if not current_user["is_logged_in"]:
        print("Invalid login details. Program closed.")
        return

    print(f"Login successful. Welcome, {current_user['username']}!")

    while current_user["is_logged_in"]:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_animals(current_user)
        elif choice == "2":
            name = input("Animal name: ")
            species = input("Animal species: ")
            add_animal(current_user, name, species)
        elif choice == "3":
            try:
                animal_id = int(input("Animal ID to remove: "))
                remove_animal(current_user, animal_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            logout(current_user)
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
