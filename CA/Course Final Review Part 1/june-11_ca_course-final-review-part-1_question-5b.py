###QUESTION 5B###
#user input
hours = float(input("Hours worked this week: "))
rate = float(input("Regular hourly rate: $"))

#calculate overtime
if hours > 40:
    overtime_hours = hours - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours

#calculate pay
overtime_rate = rate * 1.5
regular_pay = regular_hours * rate
overtime_pay = overtime_hours * overtime_rate
total_pay = regular_pay + overtime_pay

#display results
print(f"\nOvertime hours: {overtime_hours}")
print(f"Overtime rate: ${overtime_rate:.2f}")
print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Total pay: ${total_pay:.2f}")
