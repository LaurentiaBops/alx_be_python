#Calculate simple interest on a given principal 
#amount, rate of interest, and time

#Define variables
principal = 1_000 #$,dollars
rate = 0.05 #annual interest rate
time = 3 #years

interest = principal * rate * time
print("The simple interest is: ", str(interest))