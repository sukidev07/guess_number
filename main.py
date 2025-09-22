# This is our first Python program!
# Adding imports to the tool box.
# Moved function to its own location
# Created to import generated_servret_number.py
import ran_num_1_10, player_num_guess

# Moved variables higher in the stack to validate the print statements
# We create a variable to store our secret number.
secret_number = ran_num_1_10.ran_num_1_10()

# guess_count defines the total number of guesses allowed
guess_count = 3

# The print() function displays text on the screen.
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {guess_count} to guess the number.")

# Breaking out into a new DRY method we need a method to get a response outside the while loop
# Get the users first guess
user_guess = player_num_guess.get_player_guess()
guess_count -= 1 # Still need to redact a single guess the count down begins

# Refactor the while loop - interesting my original thought now comes into play.
# We now loop until based on two conditions being TRUE
while user_guess != secret_number and guess_count != 0:
    if user_guess < secret_number:
        print("Too low! Try guessing a little higher.")
    else:
        print("Too high! Try guessing a little lower.")

    print(f"{guess_count} guesses left")

    user_guess = player_num_guess.get_player_guess()
    guess_count -= 1
if user_guess == secret_number:
    print(f"Congratulations! You guessed the number in {guess_count + 1}/3 guesses. The secret number was {secret_number}!")
else:
     print(f"Sorry, you have {guess_count} guesses left. The number was {secret_number}.")   