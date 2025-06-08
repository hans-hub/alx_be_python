FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

# Main Program
temperature = float(input("Enter the temperature to convert: "))
option = input("Is this temperature Celsius or Fahrenheit? (C/F): ").strip().upper()

if option == "C":
    print(f"{temperature}℃ is {convert_to_fahrenheit(temperature):.2f}℉")
elif option == "F":
    print(f"{temperature}℉ is {convert_to_celsius(temperature):.2f}℃")
else:
    print("Please choose the correct option (C or F).")
