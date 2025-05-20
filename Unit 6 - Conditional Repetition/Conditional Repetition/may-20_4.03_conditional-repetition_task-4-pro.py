###TASK 4 - PRO###
#START
#create a variable called number and store a number between 1 and 10 in it
number = 7 #number between 1 and 10
guess = 0 #guess is set at 0

#using a While loop, ask the user to guess your number until they get it right
while guess != number:
    print("Guess what number I am thinking of! You can type \"quit\" to exit the program")
    user_input = input()

#extension - add an option for the user to quit guessing and end the program
    if (user_input.lower() == "quit"):
        print("You have chosen to quit the program.")
        break

#make sure you output suitable messages to let the user know if they guessed correctly or not
    if (user_input.isdigit()):
        guess = int(user_input)
        if (guess == number):
            print("✅ Correct!")
        else:
            print("❌ Your guess is wrong. Please try again.")
    else:
        print("Please enter a number between 1 and 10. You can type \"quit\" to exit the program")
#END WHILE
#END
