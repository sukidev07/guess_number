# Player number guess | created to meet with DRY logic and error handling
# Previous deployment was broken when you useed none INT value: float, string, etc.

def get_player_guess(prompt="Enter your guess: "):
    while True: # Start a loop that will run forever until we manually break it
        try:
            # Try to get input and convert it to an integer
            guess = int(input(prompt))
            return guess # If the conversion succeeds, return the number and exit the function
        except ValueError:
            # If a ValueError occurs, print a message and the loop will repeat
            print("That's not a valid number. Please enter only whole numbers.")