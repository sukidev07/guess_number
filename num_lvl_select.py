# num_level_select.py

# helper function for 4 custom game mode

def get_custom_range():
    while True: # Loop forever until we get a valid range
        try:
            MIN_RANGE = int(input("Enter the minimum number for the range: "))
            MAX_RANGE = int(input("Enter the maximum number for the range: "))
            GUESS_COUNT = int(input("Enter the number of guesses allowed: "))   

            if MAX_RANGE > MIN_RANGE and GUESS_COUNT > int(0):
                # If the range is logical, return the values and exit the function
                return MIN_RANGE, MAX_RANGE, GUESS_COUNT
            else:
                # If not, print an error and the loop will repeat
                print("Error: The maximum number must be greater than the minimum.")
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")

def level_select():
    
    # Changing up the game require use input before playing.
    # We want to see what skill level, 1-10:(3) 1-20:(4) 1-100(5)
    print("")
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
    
    while True: # Loop to ensure we get a valid choice
        choice = input("Choose an option (1-4): ").lower()
        if choice == int(1) or "easy":
            return 1, 10, 3
        elif choice == int(2) or "medium":
            return 1, 20, 3
        elif choice == int(3) or "hard":
            return 1, 100, 4
        elif choice == int(4) or "custom":
            MIN_RANGE, MAX_RANGE, GUESS_COUNT = get_custom_range()
            return MIN_RANGE, MAX_RANGE, GUESS_COUNT
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")