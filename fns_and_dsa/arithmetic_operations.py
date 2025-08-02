#Function that performs basic arithmetic operations

def perform_operation (num1: float, num2: float, operation: str):

    if operation == "add":
        return num1 + num2

    if operation == "subtract":
        return num1 - num2
    
    if operation == "multiply":
        return num1 * num2

    if operation == "divide":
        if num2 == 0:
            print("Undefined. Number cannot be divided by zero")

        elif ():
            return num1 / num2

