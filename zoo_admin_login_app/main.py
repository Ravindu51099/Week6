"""Main program for the Zoo Admin Login System."""

# Import authentication functions from auth.py
from auth import login, logout

# Import zoo management functions from zoo_admin.py
from zoo_admin import view_animals, add_animal, remove_animal


# Function to display the admin menu options
def show_menu() -> None:
    """Display the admin menu options."""

    # Print menu title
    print("\nZoo Admin Menu")

    # Display available actions for the admin user
    print("1. View animals")
    print("2. Add animal")
    print("3. Remove animal")
    print("4. Logout")


# Main function that controls the application flow
def main() -> None:
    """Run the zoo admin login system."""

    # Welcome message displayed when the program starts
    print("Welcome to the Zoo Admin Login System")

    # Ask the admin user for login credentials
    username = input("Username: ")
    password = input("Password: ")

    # Attempt login using the provided credentials
    current_user = login(username, password)

    # Check whether login was successful
    if not current_user["is_logged_in"]:

        # Display error message if login fails
        print("Invalid login details. Program closed.")

        # Stop program execution
        return

    # Display successful login message
    print(f"Login successful. Welcome, {current_user['username']}!")

    # Continue running while the user is logged in
    while current_user["is_logged_in"]:

        # Show the menu options
        show_menu()

        # Ask the user to select a menu option
        choice = input("Choose an option: ")

        # Option 1 → View all animals
        if choice == "1":
            view_animals(current_user)

        # Option 2 → Add a new animal
        elif choice == "2":

            # Get animal details from the admin
            name = input("Animal name: ")
            species = input("Animal species: ")

            # Add the animal to the system
            add_animal(current_user, name, species)

        # Option 3 → Remove an animal
        elif choice == "3":
            try:
                # Ask for animal ID and convert input into integer
                animal_id = int(input("Animal ID to remove: "))

                # Remove the selected animal
                remove_animal(current_user, animal_id)

            # Handle invalid number input
            except ValueError:
                print("Please enter a valid number.")

        # Option 4 → Logout from the system
        elif choice == "4":
            logout(current_user)

        # Handle invalid menu choices
        else:
            print("Invalid option. Try again.")


# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()