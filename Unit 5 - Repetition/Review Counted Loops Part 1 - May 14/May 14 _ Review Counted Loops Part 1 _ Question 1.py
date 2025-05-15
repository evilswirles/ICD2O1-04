###QUESTION 1###
x = int(input("Enter your first number (integer): "))
y = int(input("Enter your second number (integer): "))

if x <= y:
    for i in range(x, y + 1):
        print(i)
else:
    for i in range(x, y - 1, -1):
        print(i)
