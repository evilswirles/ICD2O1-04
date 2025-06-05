###QUESTION 4###
hours_worked = float(input("Enter the number of hours worked: "))

regular_hours = 40
regular_rate = 12.00
overtime_rate = 15.00

if (hours_worked <= regular_hours):
    salary = hours_worked * regular_rate
elif (hours_worked > regular_hours):
    overtime_hours = hours_worked - regular_hours
    salary = (regular_hours * regular_rate) + (overtime_hours * overtime_rate)
else:
    salary = 0  # Just a safeguard, but this case shouldn't happen

print(f"Total weekly salary: ${salary:.2f}")
