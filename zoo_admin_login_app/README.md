# Zoo Admin Login System

A simple Python command-line application that demonstrates an admin login system for a zoo management project. The project uses decorators to protect admin-only functions and log admin activity.

## Project Structure

```text
zoo_admin_login_app/
├── auth.py          # Handles admin login and logout
├── decorators.py    # Contains custom decorators
├── zoo_admin.py     # Contains admin-only zoo management functions
├── main.py          # Runs the command-line application
└── README.md        # Project explanation
```

## Functionality

The admin user can:

- Log in with a username and password
- View the zoo animal list
- Add a new animal
- Remove an animal by ID
- Log out of the system

Default admin credentials:

```text
Username: admin
Password: zoo123
```

## How the Decorator Is Implemented

The project uses two decorators in `decorators.py`.

### `admin_required`

This decorator checks whether the current user is logged in and has the `admin` role before allowing access to protected functions.

It is used in `zoo_admin.py` like this:

```python
@admin_required
def view_animals(current_user):
    ...
```

If the user is not logged in or is not an admin, the function will not run.

### `activity_logger`

This decorator logs when an admin action starts and finishes. It helps with debugging and tracking admin activity.

Example usage:

```python
@activity_logger
@admin_required
def add_animal(current_user, name, species):
    ...
```

The decorators are stacked so that every protected admin action is checked and logged.

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

Then log in using the default admin credentials.

## Example Output

```text
Welcome to the Zoo Admin Login System
Username: admin
Password: zoo123
Login successful. Welcome, admin!

Zoo Admin Menu
1. View animals
2. Add animal
3. Remove animal
4. Logout
```

## GitHub Upload Steps

```bash
git init
git add .
git commit -m "Create zoo admin login system"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/zoo-admin-login-system.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.
