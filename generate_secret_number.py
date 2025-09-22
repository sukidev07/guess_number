def generate_secret_number():
    # 1. Get a starting number (seed) from the player.
    seed = int(input("To start, enter any number to generate the secret number: "))
    
    # 2. Perform a calculation to make the number less predictable.
    # These numbers (13, 7) are arbitrary; they just mix up the seed.
    mangled_number = (seed * 13) + 7
    
    # 3. Use the modulo operator to get the number into a range of 0-9.
    number_in_range = mangled_number % 10
    
    # 4. Add 1 to shift the range to 1-10.
    final_number = number_in_range + 1
    
    # 5. Send the final result back to wherever the function was called.
    return final_number