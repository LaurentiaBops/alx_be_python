#Receive user input and calculate user's age in
#future year

#Ask user to input their current age
current_age = int(input("How old are you? "))

#Calculate the user's age in the year 2050
#Assume the current year is 2023
future_year = 2050
current_year = 2023
future_age = current_age + (future_year - current_year)
print("In 2050, you will be", str(future_age), "years old")
