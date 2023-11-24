'''
    CS 5001, 
    Fall 2023
    HW1 
    Kayser Raei
'''

def main ():
     # Constants to be used throughout the code
     CONVERSION_VALUE_SQUARE_METERS = 0.092903
     COST_PER_SQUARE_METER = 21.10
     

    # User input to gather the dimensions of the office
     office_length = (float(input("Enter the length of the office (in feet)")))
     office_width = (float(input("Enter the width of the office (in feet)")))

    # Calculations based on user input and constants
     office_area = office_length * office_width
     office_area_in_square_meters = office_area * 0.092903
     monthly_payment = 21.10 * office_area_in_square_meters

     # Display the results to the user
     print(f"The area of the office is {office_area:.2f} square feet \n"
           f"...which is {office_area_in_square_meters:.2f} square meters \n"
           f"......and you will pay €{monthly_payment:.2f} per month")
     
if __name__ == "__main__":
     main()


