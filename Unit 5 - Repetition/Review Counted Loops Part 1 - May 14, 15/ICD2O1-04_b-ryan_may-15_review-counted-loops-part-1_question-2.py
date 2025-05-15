#set up constants
valuesToCollect = 10
minValueToCollect = 1
maxValueToCollect = 10
oddValueCount = 0
evenValueCount = 0

print("Enter", valuesToCollect, "integers between", minValueToCollect, "and", maxValueToCollect, "(inclusive)")

#collect the values
for i in range(0, valuesToCollect):
    #wait for the user to input a valid number
    valid = False
    while valid == False:
        #user input value
        message = "" + str(i + 1) + ": "
        value = int(input(message))

        #check if the value is in range
        if (value < minValueToCollect) or (value > maxValueToCollect):
            print("You entered a value outside of the range.")
        else:
            valid = True

    #count odd and even values
    remainder = value % 2
    if remainder == 0: #even
        evenValueCount += 1
    else: #odd
        oddValueCount += 1

#output the number of odd or even values
print("\n")
print("Number of even values: ", evenValueCount)
print("Number of odd values: ", oddValueCount)
