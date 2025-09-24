# ran_num_mod.py

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
def ran_num_mod(MIN_RANGE, MAX_RANGE):
    # Changed it up to time seed + some manglement
    seed = time.time()
    mangled_number = int((seed * 13) + 7) # keepint it int deny the floats
    # adding in new min-MAX_RANGE value so we can dynamically change the total value range.
    range_size = MAX_RANGE - MIN_RANGE + 1
    number_in_range = mangled_number % range_size
    # This is alright not the best, but we get min range + the funky number.
    final_number = number_in_range + MIN_RANGE
    
    # 5. Send the final result back to wherever the function was called.
    return final_number