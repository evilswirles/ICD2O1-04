###QUESTION 1###
while True:
    #user input; asks for user to input a number
    userInput = input("Enter a string. Type \"quit\" to exit the program: ")
    if (userInput == "quit"): #waits for user to input "quit" to exit the program
        print("Goodbye!") #if successful, the program will output "Goodbye!" and exit
        break
    else:
        print(userInput) #prints the user input
