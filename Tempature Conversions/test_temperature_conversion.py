'''
CS5001
Fall 2023
Kayser Raei
Homework 2
'''

import temperature_conversion as tc

def test_points_fahrenheit (x1, x2, x3, x4):
    '''Converting 4 Fahrenheit temperatures to Celsius.'''

    # Converting Fahrenheit temperature to Celsius
    x1_celsius = tc.convert_fahrenheit_to_celsius(x1)
    x2_celsius = tc.convert_fahrenheit_to_celsius(x2)
    x3_celsius = tc.convert_fahrenheit_to_celsius(x3)
    x4_celsius = tc.convert_fahrenheit_to_celsius(x4)

    # Printing the converted temperatures with the expected result
    print(f'Converting {x1}F to Celsius --\n'
          f'result = {x1_celsius:.1f} expected = {x1_celsius:.1f}')
    print(f'Converting {x2}F to Celsius --\n'
          f'result = {x2_celsius:.1f} expected = {x2_celsius:.1f}')
    print(f'Converting {x3}F to Celsius --\n'
          f'result = {x3_celsius:.1f} expected = {x3_celsius:.1f}')
    print(f'Converting {x4}F to Celsius --\n'
          f'result = {x4_celsius:.1f} expected = {x4_celsius:.1f}')
    
 # Converting Celsius temperature to Fahrenheit
def test_points_celsius (y1, y2, y3):
    '''Converting 3 Celsius temperatures to Fahrenheit.'''

    y1_fahrenheit = tc.convert_celsius_to_fahrenheit(y1)
    y2_fahrenheit = tc.convert_celsius_to_fahrenheit(y2)
    y3_fahrenheit = tc.convert_celsius_to_fahrenheit(y3)

    # Printing the converted temperatures with the expected result
    print(f'Converting {y1}C to Fahrenheit --\n'
          f'result = {y1_fahrenheit:.1f} expected = {y1_fahrenheit:.1f}')
    print(f'Converting {y2}C to Fahrenheit --\n'
          f'result = {y2_fahrenheit:.1f} expected = {y2_fahrenheit:.1f}')
    print(f'Converting {y3}C to Fahrenheit --\n'
          f'result = {y3_fahrenheit:.1f} expected = {y3_fahrenheit:.1f}')

          
def main ():
  #fahrenheit testing points
    x1 = 32
    x2 = 100
    x3 = 212
    x4 = 85.1

    #celsius testing point 
    y1 = 0
    y2 = 37.8
    y3 = 100

    # Running the Fahrenheit & Celsius test points
    test_points_fahrenheit (x1, x2, x3, x4)
    test_points_celsius (y1, y2, y3) 
 

if __name__ == "__main__":
    main() 