FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Function to convert from Fahrenheit to celsius

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return CELSIUS_TO_FAHRENHEIT_FACTOR * (celsius + 32)
 

temprature = float(input("Enter the temprature to convert: "))
option = input("Is this temperature Celsius or Fahrenheit? (C/F): ")
if option == "C":
    print(f"{temprature}℃ is {convert_to_fahrenheit(temprature)}℉")
elif option == "F":
    print(f"{temprature}℉ is {convert_to_celsius(temprature)}℃")
else:
    print("choose the right option")
