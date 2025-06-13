###HIGHER OR LOWER CARD GAME - LEVEL 1 BASIC###
import random

#level 1: welcome message
print("Welcome to Ryan's Higher or Lower Card Game!")

#level 2: random card generation and display
random.randint(1, 2)

cardOne = random.randint(1, 10) #the first card
cardTwo = random.randint(1, 10) #the second card
print("Your first card is", cardOne)
print("\n")

#level 3: player guesses
print("Will the next card be higher or lower? ")
yourGuess = input("Input \"h\" for higher, and \"l\" for lower\n==> ")

if (cardTwo > cardOne) and (yourGuess == "h"):
    print("Correct!")
elif cardTwo < cardOne and (yourGuess == "l"):
    print("Correct!")
elif (cardTwo == cardOne):
    print("It's a tie! No points this round.")
else:
    print("Incorrect!")

print("Current card is", cardOne)
print("Next card is", cardTwo)
