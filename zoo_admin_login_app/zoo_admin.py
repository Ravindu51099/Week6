"""Admin-only zoo management actions."""

from decorators import admin_required, activity_logger


ANIMALS = [
    {"id": 1, "name": "Leo", "species": "Lion"},
    {"id": 2, "name": "Milo", "species": "Monkey"},
    {"id": 3, "name": "Ella", "species": "Elephant"},
]


@activity_logger
@admin_required
def view_animals(current_user: dict) -> None:
    """Display all animals currently registered in the zoo."""
    print("\nZoo Animal List")
    print("---------------")
    for animal in ANIMALS:
        print(f"{animal['id']}. {animal['name']} - {animal['species']}")


@activity_logger
@admin_required
def add_animal(current_user: dict, name: str, species: str) -> None:
    """Add a new animal record to the zoo list."""
    new_id = len(ANIMALS) + 1
    ANIMALS.append({"id": new_id, "name": name, "species": species})
    print(f"Animal added successfully: {name} the {species}")


@activity_logger
@admin_required
def remove_animal(current_user: dict, animal_id: int) -> None:
    """Remove an animal by ID if it exists."""
    for animal in ANIMALS:
        if animal["id"] == animal_id:
            ANIMALS.remove(animal)
            print(f"Animal removed successfully: {animal['name']}")
            return

    print("Animal not found.")
