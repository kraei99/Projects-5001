'''
    CS 5001, 
    Fall 2023
    HW4 
    Kayser Raei
'''

def is_valid_upc(list_of_integers: list) -> bool:
    # Check if there's less than 2 numbers
    if len(list_of_integers) < 2:
        return False

    # Count zeros in the list
    zero_count = 0
    for num in list_of_integers:
        if num == 0:
            zero_count += 1
    # If all numbers are zeros, return False
    if zero_count == len(list_of_integers):
        return False

    # Make a copy to not mess with the original list
    temp_list = list_of_integers.copy()

    # Start a sum for our calculations
    total_sum = 0
    # This will help check even or odd places
    position = 0
    
    # Loop until list is empty
    while temp_list:
        # Get the last number
        digit = temp_list.pop()

        # Add number or its triple based on position
        if position % 2 == 0:
            total_sum += digit
        else:
            total_sum += digit * 3
        
        # Go to next position
        position += 1

    # See if sum is divisible by 10
    if total_sum % 10 == 0:
        return True
    else:
        return False