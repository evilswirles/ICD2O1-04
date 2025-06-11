###CYOA - DAY 3###

#user starts off with 0 aura, then earns more aura as the CYOA progresses
aura = 0

def askUserToChoose(choices):
    #print all of the choices for the user
    for index, choice in enumerate(choices):
        print(f"{index + 1}. {choice}")

    #ask user for their choice
    n = int(input("Please enter your choice: "))

    #check if choice is valid
    while (n < 1) or (n > len(choices)):
        print("Invalid choice")
        n = int(input("\nPlease enter your choice: "))

    #return the valid choice
    print("")
    return n

def encounterDog():
    choices = [
        "🕵️‍♂️Try and find its owner",
        "🐶Take dog",
        "🍳Eat it",
        "🚶‍♂️‍➡️Do nothing and walk away"
    ]
    
    print("You are walking down the street and encounter a lost dog, what do you do?")
    choice = askUserToChoose(choices)
    if (choice == 1): #try and find its owner
        findOwner()
    elif (choice == 2): #take dog
        takeDog()
    elif (choice == 3): #eat dog
        eatDog()
    elif (choice == 4): #do nothing and walk away
        doNothingWithDog()

def findOwner():
    global aura
    aura += 1
    
    print("You have returned the dog back to its rightful owner. In return for your good deed, the owner has graciously decided to give you a shiny new car. 'Awesome!' you say back to the owner.")
    print("⏳Current aura:", aura)

    choices = [
        "🧪Buy that weird green glowing milk",
        "🥛Buy regular milk ($3)",
        "👮‍♂️Attempt to steal the milk"
    ]

    choice = askUserToChoose(choices)
    if (choice == 1): #green milk
        greenMilk()
    elif (choice == 2): #regular milk
        regularMilk()
    elif (choice == 3): #steal milk
        stealMilk()

def takeDog():
    print("TODO: take dog")

def eatDog():
    print("You disgusting piece of human trash. You decide to bring the dog back to your house, and try to cook and eat it, but it was a setup. You have been arrested by the police.")
    endGame()

def doNothingWithDog():
    print("TODO: do nothing with dog")

def greenMilk():
    print("TODO: green milk")

def regularMilk():
    print("TODO: regular milk")

def stealMilk():
    print("TODO: steal milk")
    endGame()

def endGame():
    global aura
    print("❌Game over, loser. Restart the program to try again.")
    print("⏳Current aura:", aura)



#lists
questionFour = [
    "Throw the green glowing milk at robber",
    "Act like nothing is happening"
]
questionFive = [
    "",
]
questionSix = [
    "Offer to help your coworker",
    "Report them to your boss",
    "Secretly make their work harder"
]

#ask for name
name = input("What is your name? ")
print(f"👋 Hello, {name}. Try not to get into any trouble!\n")

#start game
encounterDog()
