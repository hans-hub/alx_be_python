num1 = int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
operation = input("choose the operation(+,-,*,/)")
match operation:
    case _ if operation == "+":
        print ("The result is ",num1 + num2)
    case _ if operation == "-":
        print ("The result is ",num1 - num2)
    case _ if operation == "*":
        print ("The result is ",num1 * num2)
    case _ if operation == "/":
        if num2 == 0:
            print ("Cant divide a b=number by zero")
        else :
            print ("The result is ",num1 / num2)