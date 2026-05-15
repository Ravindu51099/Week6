"""Custom decorators used by the Zoo Admin Login System."""

# Import wraps to preserve the original function metadata
# such as function name and docstring
from functools import wraps

# Import datetime module to record timestamps for logging
from datetime import datetime


# Decorator to check whether the current user is an admin
def admin_required(func):
    """
    Allow a protected function to run only when the current user is logged in
    and has the admin role.
    """

    # wraps() keeps the original function information intact
    @wraps(func)
    def wrapper(current_user, *args, **kwargs):

        # Check if the user is logged in
        if not current_user.get("is_logged_in"):

            # Display access denied message
            print("Access denied: please log in first.")

            # Stop function execution
            return None

        # Check whether the user has admin privileges
        if current_user.get("role") != "admin":

            # Display access denied message
            print("Access denied: admin privileges required.")

            # Stop function execution
            return None

        # Print successful access message
        print(f"[ACCESS GRANTED] {current_user.get('username')} opened {func.__name__}")

        # Execute the original protected function
        return func(current_user, *args, **kwargs)

    # Return the wrapper function
    return wrapper


# Decorator to log when a function starts and finishes
def activity_logger(func):
    """Log when an admin action starts and finishes."""

    # Preserve original function metadata
    @wraps(func)
    def wrapper(*args, **kwargs):

        # Record the current date and time before function execution
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Print start log message
        print(f"[LOG {start_time}] Starting: {func.__name__}")

        try:
            # Run the original function
            return func(*args, **kwargs)

        finally:
            # Record the completion time after function execution
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Print completion log message
            print(f"[LOG {end_time}] Finished: {func.__name__}")

    # Return the wrapper function
    return wrapper