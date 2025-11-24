#Program introduction
print("Welcome to my python project!")
hours = input("Enter hours worked:")

#Completes calculations
hours = float(hours)
daily_hours = hours / 5

#Final output
print(f"You worked {daily_hours} hours a day")

#Error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
    


