#Learn to use Match Case statements for handling multiple 
# operations in a simple calculator program

#Prompt user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

def calcular(num1, num2, operation):
    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            else:
                result = num1 / num2
            
    print(f"The result is {result}.")

calcular(num1,num2,operation)