from decorators import log_activity


# Debugging note: @log_activity replaces student_login with the wrapper returned
# by log_activity. Calling student_login(...) now prints log messages before and
# after the login message below.
@log_activity
def student_login(username):
    """Simulate a student logging into the system."""
    print(f"{username} logged into the system.")


# Debugging note: this function has two parameters, which verifies that the
# decorator's *args/**kwargs forwarding works for different function signatures.
@log_activity
def submit_assignment(username, assignment):
    """Simulate a student submitting an assignment."""
    print(f"{username} submitted {assignment}.")


# Debugging note: this function confirms that the same decorator can be reused
# for multiple independent student actions without duplicating logging code.
@log_activity
def view_grades(username):
    """Simulate a student viewing grades."""
    print(f"{username} is viewing grades.")
