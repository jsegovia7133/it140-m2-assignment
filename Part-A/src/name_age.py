"""Get the user's name and age to calculate their birth year, and display a greeting.

Input:
    user name - string from user input
    user age - integer from user input
    current year - integer from system date

Process:
    calculate birth year by subtracting the user's age from the current year

Output:
    personalized greeting with the user's name and birth year - string displayed in the console

Typical usage example:
    What is your name? Judy
    How old are you? 33
    Hello Judy! You were born in 1993.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))
    
    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with the user's name and birth year.
    print(f"Hello {user_name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

