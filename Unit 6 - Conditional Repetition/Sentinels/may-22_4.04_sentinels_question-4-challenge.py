###QUESTION 4 - CHALLENGE###
#set to a negative value so that input is always bigger
largest = -1
secondLargest = -1

message = "Enter an integer (negative to stop): "
num = int(input(message))

while (num >= 0):
    if (num > largest):
        secondLargest = max(largest, secondLargest)
        largest = num
    num = int(input(message))

print("")

if (largest != -1):
    print("Largest number: ", largest)

if (secondLargest != -1):
    print("Second largest number: ", secondLargest)

print("Goodbye!")
