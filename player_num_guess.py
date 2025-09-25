# player_num_guess.py

# Player number guess | created to meet with DRY logic and error handling
# Previous deployment was broken when you useed none INT value: float, string, etc.

def get_player_guess(MIN_RANGE, MAX_RANGE, prompt="Enter your guess: "):
    while True: # Start a loop that will run forever until we manually break it
        try:
            # Try to get input and convert it to an integer
            guess = int(input(prompt))
            # Validating the min_max range of the guess to add an extra layer of guessing logic that scales.
            if MIN_RANGE <= guess <= MAX_RANGE:
                return guess # If the conversion succeeds, return the number and exit the function
            else:
                # To return a failed message because the user cannot read instructions or fat-fingers
                print(f"What... I said guess the number between {MIN_RANGE} and {MAX_RANGE}?")
        except ValueError:
            # If a ValueError occurs, print a message and the loop will repeat
            print(f"You did not enter a number. Please enter a whole number within range {MIN_RANGE}-{MAX_RANGE}.")
            