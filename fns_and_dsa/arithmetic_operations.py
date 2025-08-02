#Function that performs basic arithmetic operations

def perform_operation (num1, num2, operation):

    if operation == "add":
        return num1 + num2

    if operation == "subtract":
        return num1 - num2
    
    if operation == "multiply":
        return num1 * num2

    if operation == "divide":
        if num2 == 0:
            print("Undefined. Number cannot be divided by zero")

        else :
            return num1 / num2

