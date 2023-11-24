"""
CS5001
Kayser Raei
Homework 3
Fall 2023
"""

def black_or_white(row, column):

    if ord(column.capitalize()) % 2 == 0:
        if int(row) % 2 == 0:
            return 'BLACK'
        if int(row) % 2 == 1:
            return "WHITE"
    if ord(column.capitalize()) % 2 == 1:
        if int(row) % 2 == 1:
            return 'BLACK'
        if int(row) % 2 == 0:
            return "WHITE"