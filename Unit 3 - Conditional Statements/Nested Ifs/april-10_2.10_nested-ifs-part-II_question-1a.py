###QUESTION 1A###
print("Please input the three numbers in integer form:\n")
number1 = int(input("Enter the first number: ")) #get the three inputted numbers (ints) from the user
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

#finding the smallest number
if (number1 < number2):
    if (number1 < number3):
        smallest = number1
    else:
        smallest = number3
else:
    if (number2 < number3):
        smallest = number2
    else:
        smallest = number3

print("The smallest number of the three is:", smallest)
