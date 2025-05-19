###QUESTION 5###
# 1. Print a message if the user enters an 'A', regardless of case
char = input("Enter a character: ")
if char.upper() == 'A':  
    print("You entered an A!")

# 2. Determine if a given integer is divisible by either 3 or 5
num = int(input("Enter an integer: "))
if num % 3 == 0 or num % 5 == 0:
    print(f"{num} is divisible by 3 or 5.")
else:
    print(f"{num} is not divisible by 3 or 5.")

# 3. Determine if a given integer is divisible by both 3 and 5
num = int(input("Enter another integer: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")

# 4. Determine if a given integer is not divisible by 4 or 7
num = int(input("Enter another integer: "))
if not (num % 4 == 0 or num % 7 == 0):
    print(f"{num} is not divisible by 4 or 7.")
else:
    print(f"{num} is divisible by 4 or 7.")

# 5. Determine if two given integers are both positive, both negative, or one positive and one negative
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

if x > 0 and y > 0:
    print("Both numbers are positive.")
elif x < 0 and y < 0:
    print("Both numbers are negative.")
else:
    print("One number is positive and the other is negative.")
