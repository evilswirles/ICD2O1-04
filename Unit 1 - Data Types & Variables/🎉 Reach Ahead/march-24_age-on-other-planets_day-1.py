#input information
year = int(input("What is your age in years? "))
month = int(input("What is your age in months? "))
day = int(input("What is your age in days? "))


#calculations
ageinYears = (year * 365) #calculate for years
ageinMonths = (month * 30) #calculate for months
ageinDays = (day * 1) #calculate for days

print("\n")
print("Age in years is: ")
print("Age is months is: ")
print("Age in days is: ")
print("\n")

#total
print("Total = ", ageinYears + ageinMonths + ageinDays)
