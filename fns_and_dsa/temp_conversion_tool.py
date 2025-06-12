global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(fahrenheit,"°F is ",temp,"°C" )
    


def convert_to_fahrenheit(celsius):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(celsius,"°C is ",temp,"°F" )
    

while True:
    temp_value = (input("Enter the temperature to convert: "))
    try:
        temp = float(temp_value)
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

choice = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

if choice == "C":
    convert_to_fahrenheit(temp)
elif choice == "F":
    convert_to_celsius(temp)
else:
    "Input a valid option"