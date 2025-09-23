# This is our first Python program!
# Adding imports to the tool box.
# Moved function to its own location
# Created to import generated_servret_number.py
import ran_num_mod, player_num_guess

# Changing up the game require use input before playing.
# We want to see what skill level, 1-10:(3) 1-20:(4) 1-100(5)
print("# # # # # # # # # # # # # # # # # # # # #")
print("# ------------------------------------- #")
print("# Welcome to the Guess the Number Game! #")
print("# ------------------------------------- #")
print("#                                       #")
print("#        Select your skill level        #")
print("#                                       #")
print("#     Level       Range       Guess     #")
print("#     + + + + + + + + + + + + + + +     #")
print("#     |1. |Easy:   1-10        3  |     #")
print("#     |2. |Medium: 1-20        3  |     #") 
print("#     |3. |Hard:   1-100       4  |     #") 
print("#     |4. |Custom: x-y         z  |     #")
print("#     + + + + + + + + + + + + + + +     #")
print("#                                       #")
print("# # # # # # # # # # # # # # # # # # # # #")
print("")
choice = input("Select:").lower

## I need to add error handling somewhere around these parts might need to break out choice into a new mod

# Define the levels:
if choice == 1 or 'easy':
    min_range = 1
    max_range = 10
    guess_count = 3
elif choice == 2 or 'medium' or 'med':
    min_range = 1
    max_range = 20
    guess_count = 3
elif choice == 3 or 'hard':
    min_range = 1
    max_range = 100
    guess_count = 4
#elif choice == 4 or 'custom':
#    min_range = user_min
#    max_range = user_max
#    guess_count = user_count
else:
    print("Invalid selection. Defaulting to easy mode.")
    min_range = 1
    max_range = 10
    guess_count = 3
    
# Game should actually start here:

# Moved variables higher in the stack to validate the print statements
# We create a variable to store our secret number.
# Adding min-max_range to be addeed in to validate these values for the secret guess and updating ran_num_mod
secret_number = ran_num_mod.ran_num_mod(min_range, max_range)
print(f"I'm thinking of a number between {min_range} and {max_range}.")
print(f"You have {guess_count} to guess the number.")

# Breaking out into a new DRY method we need a method to get a response outside the while loop
# Get the users first guess
# need to pass through the min_range and max_range values to the player guess else it fails
user_guess = player_num_guess.get_player_guess(min_range, max_range) 
guess_count -= 1 # Still need to redact a single guess the count down begins

# Refactor the while loop - interesting my original thought now comes into play.
# We now loop until based on two conditions being TRUE
while user_guess != secret_number and guess_count != 0:
    if user_guess < secret_number:
        print("Too low! Try guessing a little higher.")
    else:
        print("Too high! Try guessing a little lower.")

    print(f"{guess_count} guesses left")

    user_guess = player_num_guess.get_player_guess(min_range, max_range)
    guess_count -= 1
if user_guess == secret_number:
    print(f"Congratulations! You guessed the number in {guess_count + 1}/3 guesses. The secret number was {secret_number}!")
else:
     print(f"Sorry, you have {guess_count} guesses left. The number was {secret_number}.")   