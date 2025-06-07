###CYOA - DAY 1###
aura = 0 #user starts off with 0 aura, then earns more aura as the CYOA progresses

#lists
questionTwo = [ 
    "1. Try and find its owner",
    "2. Eat it",
    "3. Take it with you and act like you own it",
    "4. Do nothing and walk away"
]
questionThree = [
    "1. Buy that weird green glowing milk",
    "2. Buy regular milk ($3)",
    "3. Buy expensive imported milk ($12)",
    "4. Attempt to steal the milk"
]
questionFour = [
    "1. Offer to help your coworker",
    "2. Ignore them",
    "3. Report them to your boss",
    "4. Secretly make their work harder"
]
questionFive = [
    "1. Turn it in to the police",
    "2. Keep the money",
    "3. Try and find the owner yourself",
    "4. Leave it be"
]

#question 1
name = input("What is your name? ")
print("Hello,", name, ". Try not to get into any trouble!")
print("\n")

#question 2
print("You are walking down the street and encounter a lost dog, what do you do?")
print(questionTwo)
print("==> To enter your answer, please enter the corresponding number (eg. 1)")
dogChoice = input("Please enter your answer: ")

if (dogChoice == "1"):
    print("You have returned the dog back to its rightful owner. In return for your good deed, the owner has graciously decided to award you $500. 'Awesome!' you say back to the owner.")
    aura = aura + 2
    print("⏳Current aura:", aura)
elif (dogChoice == "2"):
    print("You disgusting piece of human trash. You decided to \"bring\" the dog back to your house, and try to cook and eat it, but it was a setup. You have been arrested by the police.")
    print("❌Game over, loser. Restart the program to try again.")
elif (dogChoice == "3"):
    print("You attempt to pick up the dog and run away, but the dog starts barking which attracts the attention of nearby neighbours, and you get bitten in the proccess. ")
    aura = aura - 1
    print("⏳Current aura:", aura)
elif (dogChoice == "4"):
    print("You stare at the dog, and the dog stares back at you with sadness in its eyes. In the end, you decide to just mind your own business. You do not gain any aura.")
    print("⏳Current aura:", aura)

#question 3
print("\n")
print("After encountering that weird dog, you decide to buy some milk at your local 7/11. You walk up to the fridge, but there's so mamy different options, you don't know which one to choose.")
print(questionThree)
print("==> To enter your answer, please enter the corresponding number (eg. 1)")
