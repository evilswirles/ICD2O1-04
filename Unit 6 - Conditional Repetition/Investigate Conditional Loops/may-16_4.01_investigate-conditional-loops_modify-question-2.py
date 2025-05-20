###MODIFY - QUESTION 2###
print("Repeater")
print("Type in a message and I'll repeat it")
message = input("Message: ")
times = int(input("How many times? "))
print("")

counter = 0

while counter < times:
    print(str((counter + 1) * 10) + ". " + message)
    counter += 1
