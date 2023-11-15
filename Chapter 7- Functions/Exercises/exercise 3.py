def make_shirt(size, message):
    """Prints a sentence summarizing the size and message of a shirt."""
    print(f"Making a {size}-sized shirt with the message: '{message}'")

# Call the function using positional arguments
make_shirt("medium", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python is awesome!")
