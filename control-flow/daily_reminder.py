#Use conditional statements, Match Case, and loops to remind
#user about a single, priority task for the day based on time sensitivity

#Prompt for a single task
task_variable = input("Enter your task: ") #Enter task description
priority_variable = input("Priority (high/medium/low): ") #Task's priority
time_bound = input("Is it time-bound? (yes/no): ")

#Define a function that defines reminder message based on user inputs
def reminder(priority,time_bound):
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task_variable}' is a {priority} priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"Note: '{task_variable}' is a {priority} priority task. Consider completing it when you have free time.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task_variable}' is a {priority} priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"Note: '{task_variable}' is a {priority} priority task. Consider completing it when you have free time.")
reminder(priority_variable,time_bound)