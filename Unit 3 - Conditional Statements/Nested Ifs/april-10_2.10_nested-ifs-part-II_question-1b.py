###QUESTION 1B###
print("Please input the three numbers in integer form:\n")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#finding the largest number
if (num1 > num2):
    if (num1 > num3):
        largest = num1
    else:
        largest = num3
else:
    if (num2 > num3):
        largest = num2
    else:
        largest = num3

print("The largest number of the three is:", largest)
