Calculate user's birth year and display a personalized greeting.

Input:
    user name - string from user input
    user age - integer from user input
    current year - integer from system date
    
Process:
    calculate birth year by subtracting user age from current year

Output:
    personalized greeting with the user's name and birth year - string display in the console

Typical usage example:
    What is your name? Jordan
    How old are you? 25
    Hello Jordan! You were born in 2001.
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
    user_age = int(input("How old are you? ")
    
    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===


