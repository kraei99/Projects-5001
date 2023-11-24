'''
    CS 5001, 
    Fall 2023
    HW1 
    Kayser Raei
'''
'''
Test case #1:
Input: $300
Output: 6 fifties, 0 twenties, 0 tens, 1 fives, 0 ones

Test case #2:
Input: $450
Output: 9 fifties, 1 twenties, 0 tens, 0 fives, 2 ones

Test case #3:
Input: $40
Output: 0 fifties, 2 twenties, 0 tens, 0 fives, 0 ones

'''


def main (): 
    
    # Ask the user for the amount they want to withdraw.
    original_withdrawal = (int(input("Amount to withdraw? $:")))
    user_withdrawal = original_withdrawal

    # Start by determining how many $50 bills can be given.
    fifties = user_withdrawal // 50
    user_withdrawal = user_withdrawal % 50 

    # Next, determine how many $20 bills can be given.
    twenties = user_withdrawal // 20
    user_withdrawal = user_withdrawal % 20

    # Continue with $10 bills.
    tens = user_withdrawal // 10
    user_withdrawal = user_withdrawal % 10

    # Then $5 bills.
    fives = user_withdrawal //  5
    user_withdrawal = user_withdrawal % 5

    # Finally, whatever is left are $1 bills.
    ones = user_withdrawal


    
    print(f"Welcome to PDQ Bank! Amount to withdraw? $: \n"
          f"Cha-ching! You asked for {original_withdrawal} \n"
          f"That breaks down to: \n")
     
    # Print out how many of each bill the user will receive.
    print(f"{fifties} fifties")
    print(f"{twenties} twenties")
    print(f"{tens} tens")
    print(f"{fives} fives")
    print(f"{ones} ones")


if __name__ == "__main__":
    main()