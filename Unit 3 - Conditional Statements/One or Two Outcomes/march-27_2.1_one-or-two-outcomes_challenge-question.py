###CHALLENGE QUESTION###
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
