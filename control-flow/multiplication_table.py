#Use a for loop to generate and print the multiplication 
#table for a given number.

#Prompt User for number
number = int(input("Enter a number to see its multiplication table: "))


#Generate the multiplication table
for x in range(1,11):
    product = x * number
    print(f"{number} * {x} = {product}")
