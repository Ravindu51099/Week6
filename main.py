from users import (
    student_login,
    submit_assignment,
    view_grades
)


# Debugging note: main() is the test driver for the project. It calls each
# decorated function once so we can confirm the decorator logs every activity.
def main():
    """Run sample student activity actions."""

    # Debugging note: expected output includes decorator logs plus the login text.
    student_login("Mohammad")

    # Debugging note: this call checks that the decorator handles multiple
    # arguments correctly and still executes the assignment submission function.
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    # Debugging note: this call verifies the decorator works for another user
    # action and does not depend on a specific username.
    view_grades("Alex")


# Debugging note: this guard prevents main() from running when the module is
# imported elsewhere, but runs the test flow when executing python main.py.
if __name__ == "__main__":
    main()
