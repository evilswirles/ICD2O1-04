import random

def getUserValue(message):
    userInput = input(message)
    value = userInput.lower()

    if (value == "rock") or (value == "r"):
        return "rock", True
    elif (value == "paper") or (value == "p"):
        return "paper", True
    elif (value == "scissors") or (value == "s"):
        return "scissors", True
    elif (value == "quit") or (value == "q"):
        return "quit", True
    else:
        return userInput, False

def findWinner(userValue, computerValue):
    #check if user wins
    if (userValue == "rock") and (computerValue ==  "scissors"):
        return "user"
    elif (userValue == "scissors") and (computerValue == "paper"):
        return "user"
    elif (userValue == "paper") and (computerValue == "rock"):
        return "user"

    #check if computer wins
    if (computerValue == "rock") and (userValue ==  "scissors"):
        return "computer"
    elif (computerValue == "scissors") and (userValue == "paper"):
        return "computer"
    elif (computerValue == "paper") and (userValue == "rock"):
        return "computer"

    #user and computer tie
    return "tie"

def getComputerValue():
    r = random.randint(1, 3)

    if (r == 1):
        return "rock"
    elif (r == 2):
        return "paper"
    elif (r == 3):
        return "scissors"

#start the game
print("Welcome to the game of Rock Paper Scissors!")
done = False
gameRound = 1
userScore = 0
computerScore = 0

#main game loop
while not done:
    #start a new round
    print("Round", gameRound)

    #get the user's value
    valid = False
    while not valid:
        userValue, valid = getUserValue("Please enter either rock, paper, scissors or quit: ")
        print("You entered", userValue)
        if (valid == False):
            print("Let's try again.")

    #check if the user quit
    if (userValue == "quit"):
        print("Thanks for playing!")
        done = True
    else:
        #get the computer's value
        computerValue = getComputerValue()
        print("Computer plays", computerValue)

        #find a winner
        winner = findWinner(userValue, computerValue)
        if (winner == "user"):
            print("You won this round!")
            userScore += 1
            print("The score is: You:", userScore, "Computer:", computerScore)
        elif (winner == "computer"):
            print("Sorry, the computer won this round!")
            computerScore += 1
            print("The score is: You:", userScore, "Computer:", computerScore)
        else:
            print("It's a tie!")

        print("\n")
        gameRound += 1
