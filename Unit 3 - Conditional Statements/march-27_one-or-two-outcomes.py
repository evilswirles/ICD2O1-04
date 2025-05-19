##QUESTION 1##
#number1 = int(input("Input your first number "))

#if (number1 > 50):
    #print("The number you gave is greater than 50")

#if (number1 != 50):
    #print("The number you gave is not 50")


##QUESTION 2##
#name = input("Please enter your name ")

#if (name == "Ryan Bower"):
    #print("You have the same name as Ryan Bower")

#else:
    #print("Your name is not the same as Ryan Bower")


##QUESTION 3##
#number1 = int(input("Please input your first number "))
#number2 = int(input("Please input your second number that is different from the first "))

#if (number1 > number2):
    #print("Number 1 is larger than number 2")

#else:
    #print("Number 2 is larger than number 1")


##QUESTION 4##
#number1 = int(input("Please input your first number "))
#number2 = int(input("Please input your second number that is different from the first number "))

#if (number1 < number2):
    #print("Number 1 is smaller than number 2")

#else:
    #print("Number 2 is smaller than number 1")


##QUESTION 5##
#question1 = int(input("What is 1+1? "))
#if (question1 == 2):
    #print("You are correct! The answer is 2")

#else:
    #print("Your answer is wrong!")


#question2 = int(input("What is 5+5? "))
#if (question2 == 10):
    #print("You are correct! The answer is 10")

#else:
    #print("Your answer is wrong!")


#question3 = int(input("What is 20+20? "))
#if (question3 == 40):
    #print("You are correct! The answer is 40")

#else:
    #print("Your answer is wrong!")


##QUESTION 6##
#age = int(input("What is your age? "))

#if (age >= 16):
    #print ("You are over or are the age of 16 to operate a vehicle in Ontario")

#else:
    #print("You are under the legal age to operate a vehicle in Ontario")


##CHALLENGE QUESTION##
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        largest, middle, smallest = num1, num2, num3
    else:
        largest, middle, smallest = num1, num3, num2
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        largest, middle, smallest = num2, num1, num3
    else:
        largest, middle, smallest = num2, num3, num1
else:
    if num1 >= num2:
        largest, middle, smallest = num3, num1, num2
    else:
        largest, middle, smallest = num3, num2, num1

#print the numbers in descending order
print("Numbers in descending order:", largest, middle, smallest)
