# This is our first Python program!
# The print() function displays text on the screen.
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# We create a variable to store our secret number.
secret_number = 5

# Get the user's guess and convert it to an integer.
user_guess = int(input("Enter your guess: "))

# Creating a loop for number of guesses to get correct
while user_guess != secret_number:
    # restructure of the code for an lower or hire stance
    # we changed from an if elif elif to a if else in a while loop
    if user_guess < secret_number:
        # This block runs if the guess is too low.
        print("Too low! Try guessing a little higher.")
    else:
        # This block runs if the guess is too high.
        print("Too high! Try guessing a little lower.")
    
    # This is fitting inline with the if else with the prints for too high too low are indented
    # Create the repeat value to update the user_guess value
    user_guess = int(input("Try again: "))

# This block runs ONLY if the guess is correct.
# This print is outside the loop and enacts if the value is correct (ie: user_guess == secret_number)
print("You got it! Congratulations!")