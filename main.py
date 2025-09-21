# This is our first Python program!
# The print() function displays text on the screen.
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# We create a variable to store our secret number.
secret_number = 5

# Get the user's guess and convert it to an integer.
user_guess = int(input("Enter your guess: "))

# For now, let's just print the guess back to see if it worked.
print(f"You guessed: {user_guess}")

