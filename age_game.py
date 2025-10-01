#! /usr/bin/env python3
""" This programme was written to determine
whether the user is a young blood or old head
"""

__version__ = "1.0"
__maintainer__ = "Sir Max"
__contact__ = "sir.max@example.com"

# This programme is intended for educational purposes only
# This programme will calculate what you should be referred to

print("Hello and welcome to the calculator that will determine if you are a young blood or an old head.")
print()
print("Let's begin, shall we")

def the_age_game():
    run_again = True
    while run_again:
        year_of_birth = int(input("Please enter your year of birth: "))
        current_year = 2025
        age_1 = current_year - year_of_birth

        if age_1 < 15:
            print("You are a Young Blood. Please stay in school")

        elif 16 <= age_1 <= 25:
            print("You are a Young Ninja. You have a bright future ahead.")

        elif 26 <= age_1 <= 35:
            print("You are now a Big Bro. Embrace the journey ahead.")

        elif 36 <= age_1 <= 45:
            print("You are a now an Unc. Keep shining bright.")

        elif age_1 > 46:
            print("You are an old head. Please leave the club and join the seniors.")

        run_again = input("Would you like to check another age? (yes/no): ")
        if run_again.lower() != "yes":
            print("Thank you for using the age game!")
            run_again = False

the_age_game()
