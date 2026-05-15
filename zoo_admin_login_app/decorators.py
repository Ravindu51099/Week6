"""Custom decorators used by the Zoo Admin Login System."""

from functools import wraps
from datetime import datetime


def admin_required(func):
    """
    Allow a protected function to run only when the current user is logged in
    and has the admin role.
    """
    @wraps(func)
    def wrapper(current_user, *args, **kwargs):
        if not current_user.get("is_logged_in"):
            print("Access denied: please log in first.")
            return None

        if current_user.get("role") != "admin":
            print("Access denied: admin privileges required.")
            return None

        print(f"[ACCESS GRANTED] {current_user.get('username')} opened {func.__name__}")
        return func(current_user, *args, **kwargs)

    return wrapper


def activity_logger(func):
    """Log when an admin action starts and finishes."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG {start_time}] Starting: {func.__name__}")

        try:
            return func(*args, **kwargs)
        finally:
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[LOG {end_time}] Finished: {func.__name__}")

    return wrapper
