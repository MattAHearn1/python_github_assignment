#Program introduction
print("Welcome to my python project!")
hours = input("Enter hours worked:")

#Completes calculations
hours = float(hours)
daily_hours = hours / 7

#Final output
print("You studied " + daily_hours + "hours a day")

#Error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
    


