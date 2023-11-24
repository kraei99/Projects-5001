"""
CS5001
Kayser Raei
Homework 3
Fall 2023
"""

import chessboard as cb

# test cases for columns
"""
test columns
test_column = 'A'
test_column_2 = 'F'
test_column_3 = 'D'
test_column_4 = 'h'
"""
# test cases for rows
"""
test rows
test_row_1 = 2
test_row_2 = 5
test_row_3 = 3
test_row_4 = 7
"""

# tests if the  row is valid by comparing it against the expected result
def test_check_valid_row(row, expected):
    result = cb.check_valid_row(row)
    print(f"Row: {row}, Expected: {expected}, Actual: {result}")

def test_check_valid_column(column, expected):
    result = cb.check_valid_column(column)
    print(f"Column: {column}, Expected: {expected}, Actual: {result}")

def test_squares():
    # Invalid columns
    test_check_valid_column('I', False)
    test_check_valid_column('Z', False)
    
    # Validating the given columns values.
    test_check_valid_column('A', True)
    test_check_valid_column('F', True)
    test_check_valid_column('D', True)
    test_check_valid_column('H', True)

    # Invalid rows
    test_check_valid_row(0, False)
    test_check_valid_row(9, False)
    test_check_valid_row("10", False)
    test_check_valid_row("abcd", False)

    # Validating the given row values.
    test_check_valid_row(2, True)
    test_check_valid_row(5, True)
    test_check_valid_row(3, True)
    test_check_valid_row(7, True)

def main():
    test_squares()

if __name__ == "__main__":
    main()
