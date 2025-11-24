print("Welcome to my python project!")
hours = input("Enter hours worked:")
hours = float(hours)
daily_hours = hours / 7
print("You studied " + daily_hours + "hours a day")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
    


