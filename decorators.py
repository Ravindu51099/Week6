from datetime import datetime


# Debugging note: this decorator is the central logging helper for the project.
# It receives another function, wraps it with extra logging, and returns the
# wrapped version so the original function can still be called normally.
def log_activity(func):
    """Log when a decorated activity function starts and finishes."""

    # Debugging note: @wraps keeps the original function name and metadata.
    # Without it, every decorated function would appear as "wrapper" during
    # inspection, which can make debugging confusing in larger projects.
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Run the original function with activity logs around it."""

        # Debugging note: these lines confirm which function is being executed
        # and when the activity begins.
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # Debugging note: this is the actual call to the decorated function.
        # *args and **kwargs allow the decorator to support functions with
        # different parameter lists, such as one username or username + assignment.
        result = func(*args, **kwargs)

        # Debugging note: reaching this point confirms the original function
        # completed successfully and returned control to the decorator.
        print("Activity completed.")
        print("===================================\n")

        # Debugging note: returning the original result preserves normal
        # function behavior if a decorated function later returns a value.
        return result

    return wrapper
