#Calculate and provide feedback on a user's monthly
#savings and potential future savings without applying
#conditional statements


#Prompt usesrs to input their financial details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

#Project Annual Savings 
a = 0.05 #assume a 5% annual interest rate
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * a))

#Output Results
print("Your monthly savings are $"+str(monthly_savings)+".")
print("Projected savings after one year, with interest, is: $"+str(projected_savings)+".")
