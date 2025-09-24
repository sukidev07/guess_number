# main.py

# This is our first Python program!
# During the build we split out actual functions into their own modules
# Used local imports to perform jobs, this was to train the skills and improve logical flow for myself
import ran_num_mod, player_num_guess, num_lvl_select

# Added a game loop so we can keep playing with a single run
while True:

    # Game should actually start here:
    # Level Selector: Forces the import of the major game variables
    MIN_RANGE, MAX_RANGE, GUESS_COUNT = num_lvl_select.level_select()

    # Module to randomly generate the number based on the min and max range provided
    # Needs to pass the ran_num_mod(MIN_RANGE, MAX_RANGE) to the function: Else it don't work 
    secret_number = ran_num_mod.ran_num_mod(MIN_RANGE, MAX_RANGE) 

    # Lets open the game up with the computer asking you to do a thing: GUESS A NUMBER!
    print("")
    print(f"I'm thinking of a number between {MIN_RANGE} and {MAX_RANGE}.")
    print(f"You have {GUESS_COUNT} to guess the number.")

    # Player guess need to be gotten so we ask but created the function that lives in another file, much like the princess in another castle
    # Needs to pass the get_player_guess(MIN_RANGE, MAX_RANGE) to the function: Else it don't work 
    user_guess = player_num_guess.get_player_guess(MIN_RANGE, MAX_RANGE) 
    GUESS_COUNT -= 1 # Still need to redact a single guess the count down begins (pretty sure its require daniel)

    # Refactor the while loop - interesting my original thought now comes into play.
    # We now loop until based on two conditions being TRUE
    while user_guess != secret_number and GUESS_COUNT != 0:
        if user_guess < secret_number:
            print("Too low! Try guessing a little higher.")
        else:
            print("Too high! Try guessing a little lower.")

        print(f"{GUESS_COUNT} guesses left")

        # loops back to get value but reduction of the min/max_range
        # Needs to pass the get_player_guess(MIN_RANGE, MAX_RANGE) to the function: Else it don't work 
        user_guess = player_num_guess.get_player_guess(MIN_RANGE, MAX_RANGE)
        GUESS_COUNT -= 1
    
    # Based win or lose conditions 
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the correct number: {secret_number}!")
        print(f"Total guesses remaining: {GUESS_COUNT + 1}")
    else:
        # cleaning up some of the game play words 
        print(f"Sorry, you have {GUESS_COUNT} guesses left.")
        print(f"Game over. The number was {secret_number}.")
    
    # part of the replay logic; yes or y lets you continue else all other break
    print("Do you want to play again?")
    play_again = input("Enter: Yes to play again: ").lower()
    if play_again != "yes" and play_again != "y": # continue the game or break to end
        break


