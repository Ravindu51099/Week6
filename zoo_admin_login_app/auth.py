"""Authentication logic for the Zoo Admin Login System."""

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "zoo123"


def login(username: str, password: str) -> dict:
    """Validate admin credentials and return a user session dictionary."""
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return {
            "username": username,
            "role": "admin",
            "is_logged_in": True,
        }

    return {
        "username": username,
        "role": "guest",
        "is_logged_in": False,
    }


def logout(current_user: dict) -> None:
    """End the current admin session."""
    current_user["is_logged_in"] = False
    print("You have been logged out.")
