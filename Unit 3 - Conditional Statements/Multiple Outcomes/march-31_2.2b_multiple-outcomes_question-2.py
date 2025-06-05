###QUESTION 2###
age = int(input("What is your age? ")) #asks for your age

if (age <= 12):
    print("You are a child")
elif (age > 12):
    print("You are a teen")
elif (age >= 20):
    print("You are an adult")
elif (age > 65):
    print("You are a senior citizen")
else:
    print("Invalid age")
