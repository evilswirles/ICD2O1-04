###TASK 6 - BEAST###
#start
number = 7
QUIT = "n"
guess = 0

#while QUIT = n:
while (QUIT == "n"):
    #if the guess != number:
    if (guess != number):
        print("Guess what number I am thinking of!")
        user_input = input(">>> ") #user input

        if user_input.isdigit():
            guess = int(user_input)

            #if the guess = number:
            if (guess == number):
                print("Correct!")
            else:
                print("Wrong! Do you want to quit (y/n)?")
                QUIT = input().lower()
            # END IF

        else:
            print("Invalid input.")
