###QUESTION 1###
message = "Enter a string. Type \"quit\" to exit the program: "
userInput = input(message)

while (userInput != "quit"):
    print(userInput)
    userInput = input(message)

print("Goodbye!")
