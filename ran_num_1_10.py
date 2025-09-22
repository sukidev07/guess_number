# Module - creation of the first module to be used
# Module is a way to break the code apart, usually with functions so they can be reused in the future
# This example we can reuse a generate random whole number 1-10 whenver we like.
# We can also change up the file name to be more accurate
# We used this to refactor the code into something more managable for scaleable approach

# Import time as the seed location
import time

# Creating a function inside the code first and testing.
# Function is defined to validate an incoming seed value the player inputs and has the range between 1-10
# Issue with fucntion is this is a repeatable seed amount
def ran_num_1_10():
    # 1. Get a starting number (seed) from the player.
    seed = time.time()
    
    # 2. Perform a calculation to make the number less predictable.
    # These numbers (13, 7) are arbitrary; they just mix up the seed.
    mangled_number = (seed * 13) + 7
    
    # 3. Use the modulo operator to get the number into a range of 0-9.
    number_in_range = mangled_number % 10
    
    # 4. Add 1 to shift the range to 1-10.
    # 4. Fixed bug changed to int() to make sure it was not a float
    final_number = int(number_in_range + 1)
    
    # 5. Send the final result back to wherever the function was called.
    return final_number