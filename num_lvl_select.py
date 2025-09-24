

def level_select(min_range, max_range, guess_count, choice=() ):
    
        choice = input("Select:").lower()
    # Define the levels:
        if choice == int(1) or 'easy':
            min_range = 1
            max_range = 10
            guess_count = 3
        elif choice == int(2) or 'medium' or 'med':
            min_range = 1
            max_range = 20
            guess_count = 3
        elif choice == int(3) or 'hard':
            min_range = 1
            max_range = 100
            guess_count = 4
        #elif choice == int(4) or 'custom':
        #    min_range = user_min
        #    max_range = user_max
        #    guess_count = user_count
        else:
            print("Invalid selection. Defaulting to easy mode.")
            min_range = 1
            max_range = 10
            guess_count = 3