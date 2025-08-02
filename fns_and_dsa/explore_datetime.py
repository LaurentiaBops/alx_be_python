# Performs specified operations with dates and times

import datetime
from datetime import datetime, timedelta

#Determine the current date and time
def display_current_datetime ():
   now = datetime.now()
   print("Current Date and Time:",now.strftime("%Y-%m-%d %H:%M:%S")) 

display_current_datetime()

#Calculate a future day
def calculate_future_date ():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    now = datetime.now()              
    future_date = now.date() + timedelta(days = number_of_days)
    print("Future date: ",future_date.strftime("%Y-%m-%d"))

calculate_future_date()

#if __name__ == "__main__":
#    main()
