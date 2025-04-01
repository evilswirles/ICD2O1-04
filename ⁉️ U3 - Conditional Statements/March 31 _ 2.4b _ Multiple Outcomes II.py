##QUESTION 1##
#number = int(input("What is your number? ")) #asks for a number

#if(number >= 0):
    #print("Your number is positive")

#elif(number <= -1):
    #print("Your number is negative")

#else:
    #print("Your number is neither")


##QUESTION 2##
#age = int(input("What is your age? ")) #asks for your age

#if(age <= 12):
    #print("You are a child")

#elif(age > 12):
    #print("You are a teen")

#elif(age >= 20):
    #print("You are an adult")

#elif(age > 65):
    #print("You are a senior citizen")

#else:
    #print("Invalid age")


##QUESTION 3##
#weight = float(input("Enter your weight in kg: "))

#if weight > 80:
    #print("You are classified as Heavy Weight.")
#elif 60 <= weight <= 80:
    #print("You are classified as Medium Weight.")
#else:
    #print("You are classified as Light Weight.")


##QUESTION 4##
hours_worked = float(input("Enter the number of hours worked: "))

regular_hours = 40
regular_rate = 12.00
overtime_rate = 15.00

if hours_worked <= regular_hours:
    salary = hours_worked * regular_rate
elif hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    salary = (regular_hours * regular_rate) + (overtime_hours * overtime_rate)
else:
    salary = 0  # Just a safeguard, but this case shouldn't happen

print(f"Total weekly salary: ${salary:.2f}")

