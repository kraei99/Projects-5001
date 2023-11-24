'''
    CS 5001, 
    Fall 2023
    HW4 
    Kayser Raei
'''

# Import all the data sets from hw4data
from hw4data import DATA0, DATA1, DATA2, DATA3, DATA4, DATA5

# Define the decode function
def decode(data: list) -> list:
    # Create an empty list to store the decoded symbols
    decoded_list = []
    
    # Set starting point (i) to 0
    i = 0
    
    # Loop through the input data until we reach the end
    while i < len(data):
        # Get the current symbol (like 'P' or 'Y')
        symbol = data[i]
        
        # Get the number of times the symbol is repeated
        count = data[i + 1]
        
        # Add the symbol to our decoded_list 'count' times
        for _ in range(count):
            decoded_list.append(symbol)
        
        # Move to the next pair (symbol and its count) in the data list
        i = i + 2

    # Return the completed decoded list
    return decoded_list