# This is our first Python program!
# Adding imports to the tool box.
# Moved function to its own location
# Created to import generated_servret_number.py
import ran_num_1_10


# Moved variables higher in the stack to validate the print statements
# We create a variable to store our secret number.
secret_number = ran_num_1_10.ran_num_1_10()


# guess_count defines the total number of guesses allowed
guess_count = 3

# The print() function displays text on the screen.
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {guess_count} to guess the number.")

# create a number guessing loop
# guess if not equal to value will loop until max numbers tried or correct guess
while guess_count != 0:
    
    # Guess moved to validate guess attempts
    user_guess = int(input("Enter your guess: "))
    # Adding the guess reduction count at the top of the code to keep it DRY
    guess_count -= 1

    if user_guess == secret_number:
        # This block runs if the guess is correct.
        # We moved the correct statement inside and moved the failed message outside
        # Added break to clean clear out of the loop onces reached
        print(f"Congratulations! You guessed the number {secret_number}!")
        print(f"total guesses reamining {guess_count + 1}/3")
        break  # Exit the loop if the guess is correct 
    elif user_guess < secret_number:
        # This block runs if the guess is too low.
        print("Too low! Try guessing a little higher.")
        print(f"{guess_count} guesses left")
    else:
        # This block runs if the guess is too high.
        print("Too high! Try guessing a little lower.")
        print(f"{guess_count} guesses left")
    
# adding the failed outside while statement to have the counter catch if 
if user_guess != secret_number:
    print(f"Sorry, you have {guess_count} guesses left. The number was {secret_number}.")
