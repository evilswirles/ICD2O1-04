###QUESTION 1###
#small = 5
#medium = 6
#large = 7

#pizza = input("What kind of pizza do you wish to order? Choices are: small, medium, large ")
#toppings = input("What kind of toppings do you want on your pizza? ")

#if (pizza == "small"):
    #small = 5
    #if (toppings == 1)


###QUESTION 2###
name = input("What is your name? ")
salary = float(input("What is your annual salary? "))

if (salary < 6000):
    print("Your name is", name, "and you have no tax")

elif (salary >= 6000) and (salary < 20000):
    salary * 0.25
    print("Your name is", name, "and you have 25% tax")
        
elif (salary >= 20000) and (salary < 50000):
    salary * 0.3
    print("Your name is", name, "and you have 30% tax")

elif (salary >= 50000):
    salary * 0.25
    print("Your name is", name, "and you have 35% tax")

else:
    print("Error. Please try again")
