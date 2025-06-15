
def divide(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 /num2

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = divide(num1, num2)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError as e:
    print(e)