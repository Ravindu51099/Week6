"""Authentication logic for the Zoo Admin Login System."""

# Default admin username used for login validation
ADMIN_USERNAME = "admin"

# Default admin password used for login validation
ADMIN_PASSWORD = "zoo123"


# Function to validate user login credentials
def login(username: str, password: str) -> dict:
    """Validate admin credentials and return a user session dictionary."""

    # Check whether the entered username and password match admin credentials
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

        # Return a dictionary representing a successful admin session
        return {
            "username": username,      # Store the username
            "role": "admin",           # Assign admin role
            "is_logged_in": True,      # Mark user as logged in
        }

    # Return guest session details if login fails
    return {
        "username": username,          # Store attempted username
        "role": "guest",               # Assign guest role
        "is_logged_in": False,         # Mark login as failed
    }


# Function to log out the current user
def logout(current_user: dict) -> None:
    """End the current admin session."""

    # Update login status to False
    current_user["is_logged_in"] = False

    # Display logout confirmation message
    print("You have been logged out.")