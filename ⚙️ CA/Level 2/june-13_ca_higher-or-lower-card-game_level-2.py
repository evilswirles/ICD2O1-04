import random

name = input("What is your name? ")

#step 1: welcome and setup
print(f"Hallo, {name}. Welcome to Ryan's Higher or Lower Card Game!")
print("You will be playing 5 rounds in total. Try to guess if the next card is higher or lower!")
print("If the cards are the same, it will count as a incorrect guess.\n")

yourScore = 0
gameRounds = 5
roundNumber = 1

#step 2: game loop (5 rounds)
while (roundNumber <= gameRounds):
    print("Round", roundNumber)

    yourCurrentCard = random.randint(1, 10)
    print("The current card is:", yourCurrentCard)

    #step 3: player guess and input handling
    yourGuess = input("Will the next card be higher or lower? (h/l): ")

    # Manual lowercase handling
    if (yourGuess == "H"):
        (yourGuess == "h")
    if (yourGuess == "L"):
        yourGuess == 'l'

    #step 4: generate "next" card and compate
    nextCard = random.randint(1, 10)

    if (nextCard > yourCurrentCard) and (yourGuess == "h"):
        print("Correct")
        yourScore = yourScore + 1
    elif (nextCard < yourCurrentCard) and (yourGuess == "l"):
        print("Correct!")
        yourScore = yourScore + 1
    else:
        print("Incorrect!")

    #step 5: scoring and feedback
    print("Current card was:", yourCurrentCard)
    print("Next card was:", nextCard)
    print("Current score:", yourScore)

    roundNumber = roundNumber + 1

#step 6: end of game summary
print("Game Over!")
print("Your total score is:", score, "out of", rounds)
