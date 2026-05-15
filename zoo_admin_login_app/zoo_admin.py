"""Admin-only zoo management actions."""

# Import custom decorators used for authentication and logging
from decorators import admin_required, activity_logger


# List that stores animal records in the zoo system
# Each animal is represented as a dictionary
ANIMALS = [
    {"id": 1, "name": "Leo", "species": "Lion"},
    {"id": 2, "name": "Milo", "species": "Monkey"},
    {"id": 3, "name": "Ella", "species": "Elephant"},
]


# Apply logging decorator first
# Then apply admin access control decorator
@activity_logger
@admin_required
def view_animals(current_user: dict) -> None:
    """Display all animals currently registered in the zoo."""

    # Display section title
    print("\nZoo Animal List")
    print("---------------")

    # Loop through all animals in the list
    for animal in ANIMALS:

        # Display animal details
        print(f"{animal['id']}. {animal['name']} - {animal['species']}")


# Decorators used to log activity and protect admin access
@activity_logger
@admin_required
def add_animal(current_user: dict, name: str, species: str) -> None:
    """Add a new animal record to the zoo list."""

    # Generate a new ID based on current list size
    new_id = len(ANIMALS) + 1

    # Add the new animal dictionary into the ANIMALS list
    ANIMALS.append({"id": new_id, "name": name, "species": species})

    # Display success message
    print(f"Animal added successfully: {name} the {species}")


# Decorators used for logging and admin authorization
@activity_logger
@admin_required
def remove_animal(current_user: dict, animal_id: int) -> None:
    """Remove an animal by ID if it exists."""

    # Search through all animals in the list
    for animal in ANIMALS:

        # Check whether the current animal ID matches the requested ID
        if animal["id"] == animal_id:

            # Remove the matching animal from the list
            ANIMALS.remove(animal)

            # Display success message
            print(f"Animal removed successfully: {animal['name']}")

            # Exit function after successful removal
            return

    # Display message if no matching animal is found
    print("Animal not found.")