"""
CS5001
Kayser Raei
Homework 3
Fall 2023
"""

def check_valid_row(row):
    try:
        # Convert row to integer if it's a string or already an integer
        row = int(row)
        
        # Check if the given row is an integer between 1 and 8 inclusive
        return 1 <= row <= 8
    except ValueError:  # If conversion to int fails
        return False

def check_valid_column(column):
    if ord(column.upper()) >= 65 and ord(column.upper()) <= 72:
        return True 
    else:
        return False