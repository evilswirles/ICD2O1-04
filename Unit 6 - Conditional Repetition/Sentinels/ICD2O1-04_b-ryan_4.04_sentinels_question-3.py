###QUESTION 3###
#set to a negative value so that input is always bigger
largest = -1

message = "Enter an integer (negative to stop): "
num = int(input(message))

while (num >= 0):
    largest = max(largest, num)
    num = int(input(message))

if (largest != -1):
    print("Largest number:", largest)

print("Goodbye!")
