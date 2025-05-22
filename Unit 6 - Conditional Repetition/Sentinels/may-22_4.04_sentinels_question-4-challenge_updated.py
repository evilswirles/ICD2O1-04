###QUESTION 4 - CHALLENGE - UPDATED###
#set to a negative value so that input is always bigger
largest = -1
secondLargest = -1

message = "Enter an integer (negative number to stop): "
num = int(input(message))

while (num >= 0):
    if (num > largest):
        if (largest > secondLargest):
            secondLargest = largest
        largest = num
    elif (num > secondLargest):
        secondLargest = num
    num = int(input(message))

print("")

if (largest != -1):
    print("Largest number: ", largest)

if (secondLargest != -1):
    print("Second largest number: ", secondLargest)

print("Goodbye!")
