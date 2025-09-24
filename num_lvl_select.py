# num_level_select.py

# helper function for 4 custom game mode

def get_custom_range():
    while True: # Loop forever until we get a valid range
        try:
            # Try to get input and convert it to integers for min max and guess count
            MIN_RANGE = int(input("Enter the minimum number for the range: "))
            MAX_RANGE = int(input("Enter the maximum number for the range: "))
            GUESS_COUNT = int(input("Enter the number of guesses allowed: "))   
            
            # Validates MAX is not smaller than Min because that would break stuff
            # Validates GUESS_COUNT is also greater than 0 because that is also strange and would screw up logic
            if MAX_RANGE > MIN_RANGE and GUESS_COUNT > 0:
                # If the range is logical, return the values and exit the function
                return MIN_RANGE, MAX_RANGE, GUESS_COUNT
            else:
                # If not, print an error and the loop will repeat
                print("Error: The maximum number must be greater than the minimum.")
                print("       The number of guesses must be greater than 0.")
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
        choice = input("Choose an option (1-4): ").lower() # get the choice input then compare (string value)
        # return MIN_RANGE,MAX_RANGE,GUESS_COUNT values if you get confused
        if choice == "1" or choice == "easy":
            return 1, 10, 3
        elif choice == "2" or choice == "medium" or choice == "med":
            return 1, 20, 3
        elif choice == "3" or choice == "hard":
            return 1, 100, 4
        # This one is fun as it loops to the above function to get your own values (forced and validated)
        elif choice == "4" or choice == "custom":
            MIN_RANGE, MAX_RANGE, GUESS_COUNT = get_custom_range()
            return MIN_RANGE, MAX_RANGE, GUESS_COUNT
        # Check on the 'error' and just loops back if you can't type correctly
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")