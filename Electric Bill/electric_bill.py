'''
    CS 5001, 
    Fall 2023
    HW1 
    Kayser Raei
'''

def main():
    supply_charge = float(input("What is the supplier fee per kWh?"))
    power_delivery_charge = float(input("What is the power fee per kWh?"))
    kilowatt_hours_used = float(input("How many kWh were used this month?"))

    # Compute the eletricity bill
    total = kilowatt_hours_used * (supply_charge + power_delivery_charge)
    
    # Display the result
    print(f"Your electricity bill is: ${total:.2f}")

if __name__ == "__main__":
    main()