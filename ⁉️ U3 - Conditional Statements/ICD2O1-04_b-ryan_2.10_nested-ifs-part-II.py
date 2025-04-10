###QUESTION 1###
## question 1a ##
#print("Please input the three numbers in integer form:\n")
#number1 = int(input("Enter the first number: ")) #get the three inputted numbers (ints) from the user
#number2 = int(input("Enter the second number: "))
#number3 = int(input("Enter the third number: "))

#finding the smallest number
#if number1 < number2:
    #if number1 < number3:
        #smallest = number1
    #else:
        #smallest = number3
#else:
    #if number2 < number3:
        #smallest = number2
    #else:
        #smallest = number3

#print("The smallest number of the three is:", smallest)


## question 1b ##
#print("Please input the three numbers in integer form:\n")
#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#num3 = int(input("Enter the third number: "))

#finding the largest number
#if num1 > num2:
    #if num1 > num3:
        #largest = num1
    #else:
        #largest = num3
#else:
    #if num2 > num3:
        #largest = num2
    #else:
        #largest = num3

#print("The largest number of the three is:", largest)


###QUESTION 2###
def calculate_discount(tv_type, size):
    if tv_type == "plasma":
        discount = 5  # 5% for plasma
    elif tv_type == "LCD":
        if size == 30:
            discount = 8  # 8% for 30" LCD
        elif size == 42:
            discount = 10  # 10% for 42" LCD
        else:
            discount = 0  # No discount for other sizes of LCD
    else:
        discount = 0  # No discount for other TV types

    return discount

tv_type = input("Enter the TV type (plasma/LCD): ").lower()
size = int(input("Enter the TV size (in inches): "))

discount = calculate_discount(tv_type, size)
if discount == 0:
    print("No discount.")
else:
    print(f"Discount is {discount}% of the selling price.")
