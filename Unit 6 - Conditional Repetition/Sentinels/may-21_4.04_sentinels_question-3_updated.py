###QUESTION 3 - UPDATED###
#set to a negative value so that input is always bigger
largest = -1

message = "Enter an integer (negative number to stop): "
num = int(input(message))

while (num >= 0):
    if (num > largest):
        largest = num
    num = int(input(message))

print("\n")

if (largest != -1):
    print("Largest number:", largest)

print("\n")
print("Goodbye!")
