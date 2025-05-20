###MODIFY - QUESTION 1###
print("Repeater")
print("Type in a message and I'll repeat it 5 times")
message = input("Message: ")
print("")

counter = 0

while (counter < 5):
    print(str((counter + 1) * 10) + ". " + message)
    counter += 1
