# This is our first Python program!
# The print() function displays text on the screen.
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# We create a variable to store our secret number.
secret_number = 5

# Get the user's guess and convert it to an integer.
user_guess = int(input("Enter your guess: "))

# Compare the guess to the secret number using an if/else statement.
if user_guess == secret_number:
    # This block runs ONLY if the guess is correct.
    print("You got it! Congratulations!")
elif user_guess < secret_number:
    # This block runs if the guess is too low.
    print("Too low! Try guessing a little higher.")
elif user_guess > secret_number:
    # This block runs if the guess is too high.
    print("Too high! Try guessing a little lower.")
else:
    # This block runs ONLY if the guess is incorrect.
    print("Sorry, that's not the correct number.")