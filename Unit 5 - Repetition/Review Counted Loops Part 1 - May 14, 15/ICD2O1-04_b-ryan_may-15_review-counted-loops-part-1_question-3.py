#set up constants
minValueToCollect = 1
maxValueToCollect = 10

#wait for the user to input a valid number
n = 0
valid = False
while valid == False:
    #user input value
    message = "Enter an integer between " + str(minValueToCollect) + " and " + str(maxValueToCollect) + " (inclusive): "
    n = int(input(message))

    #check if the value is in range
    if (n < minValueToCollect) or (n > maxValueToCollect):
        print("You entered a value outside of the range.")
    else:
        valid = True

#display an n x n grid representing the multiplication table up to n
for a in range(1, n + 1):
    for b in range(1, n + 1):
        product = str(a * b)
        print(f'{product:>4}', end = "")
    print("")
