# main.py

# This is our first Python program!
# Adding imports to the tool box.
# Moved function to its own location
# Created to import generated_servret_number.py
import ran_num_mod, player_num_guess, num_lvl_select

# Game should actually start here:
# We need a level select, which sets the min,max range and guess count
MIN_RANGE, MAX_RANGE, GUESS_COUNT = num_lvl_select.level_select()

# Moved variables higher in the stack to validate the print statements
# We create a variable to store our secret number.
# Adding min-MAX_RANGE to be addeed in to validate these values for the secret guess and updating ran_num_mod
secret_number = ran_num_mod.ran_num_mod(MIN_RANGE, MAX_RANGE)
print("")
print(f"I'm thinking of a number between {MIN_RANGE} and {MAX_RANGE}.")
print(f"You have {GUESS_COUNT} to guess the number.")

# Breaking out into a new DRY method we need a method to get a response outside the while loop
# Get the users first guess
# need to pass through the MIN_RANGE and MAX_RANGE values to the player guess else it fails
user_guess = player_num_guess.get_player_guess(MIN_RANGE, MAX_RANGE) 
GUESS_COUNT -= 1 # Still need to redact a single guess the count down begins

# Refactor the while loop - interesting my original thought now comes into play.
# We now loop until based on two conditions being TRUE
while user_guess != secret_number and GUESS_COUNT != 0:
    if user_guess < secret_number:
        print("Too low! Try guessing a little higher.")
    else:
        print("Too high! Try guessing a little lower.")

    print(f"{GUESS_COUNT} guesses left")

    user_guess = player_num_guess.get_player_guess(MIN_RANGE, MAX_RANGE)
    GUESS_COUNT -= 1
if user_guess == secret_number:
    print(f"Congratulations! You guessed the number in {GUESS_COUNT + 1}/3 guesses. The secret number was {secret_number}!")
else:
     print(f"Sorry, you have {GUESS_COUNT} guesses left. The number was {secret_number}.")   