'''
CS5001
Fall 2023
Kayser Raei
Homework 2
'''

import temperature_conversion as tc

def calculate_windchill (temperature, speed):
    '''Function: calculate_windchill: Calculates windchill based on international formula (Metric)
    Parameters:
        temperature in Fahrenheit
        speed in miles per hour
    Returns: windchill index (floating point value) based on applied formula
    Require: temp/speed in metric units
    Ensure: metric -> imperial unit conversions prior to calculation
    >>> calculate_windchill (100,10)
    98.06480921360912
    >>> calculate_windchill (80, 30)
    85.39092850760173
    '''

    # Convert temperature from Fahrenheit to Celsius.
    temperature_celsius = tc.convert_fahrenheit_to_celsius(temperature)
    
    # Convert wind speed from MPH to KPH.
    speed_kph = 1.61 * speed

    # Calculating Windchill index (metric)
    wind_chill_index = 13.12 + (0.6215*temperature_celsius) - (11.37*speed_kph)**0.16 + (0.3965*temperature_celsius*speed_kph)**0.16

    # Convert wind chill index result to Fahrenheit
    wind_chill_index_fahrenheit = tc.convert_celsius_to_fahrenheit(wind_chill_index)

    # Returning the windchill index in Fahrenheit.
    return wind_chill_index_fahrenheit


def main():
    # Asking for temperature input from the user in Fahrenheit.
    temperature = float(input('Temperature in Fahrenheit?'))

    # Asking for wind speed in mph from user
    speed = float(input('Wind Speed in mph?'))

    # Calculating the windchill index.
    wind_chill_value = calculate_windchill(temperature, speed)
    
    # Printing the windchill index.
    print(f'Wind Chill Index: {wind_chill_value:.2f}')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()