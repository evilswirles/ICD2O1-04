###QUESTION 5A###
name = input("What is your name? ")
day = int(input("Enter the day you were born (day 1-30): "))
month = int(input("Enter the month you were born (month 1-12): "))
year = int(input("Enter the year you were born: "))
print("\n")

currentDay = int(input("Enter today's day (day 1-30): "))
currentMonth = int(input("Enter today's month (month 1-12): "))
currentYear = int(input("Enter today's year (eg. 2009): "))
print("\n")

#calculations
birthTotalDays = year * 365 + (month - 1) * 30 + day
currentTotalDays = currentYear * 365 + (currentMonth - 1) * 30 + currentDay

#calculate the difference
daysOld = currentTotalDays - birthTotalDays

#output the results
print(f"Hello, {name}. You are ⏳{daysOld} days old.")
