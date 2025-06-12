###CYOA - DAY 4###
import random

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
        "🍲Eat it",
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
        buyGreenMilk()
    elif (choice == 2): #regular milk
        buyRegularMilk()
    elif (choice == 3): #steal milk
        stealMilk()

def takeDog():
    dogBite = random.randint(1, 2)
    if (dogBite == 1):
        goToHospital()
    else:
        dogLikesYou()

def goToHospital():
    print("The dog ends up biting you, and you contract life-threatening rabies. In the end, you perish.")
    failGame()

def dogLikesYou():
    global aura
    aura += 1

    print("TODO: dog likes you")
    goToPetStore()

def goToPetStore():
    print("TODO: go to pet store")
    pickpocketed = random.randint(1, 2)
    if (pickpocketed == 1): #pickpocketed; can't pay for toy
        cantPayForToy()
    else:
        payForToy() #pay for toy

def cantPayForToy():
    print("TODO: cant pay for toy")
    failGame()

def payForToy():
    global aura
    aura += 1
    
    print("TODO: pay for toy")
    goToWork()

def eatDog():
    print("You disgusting piece of human trash. You decide to bring the dog back to your house, and try to cook and eat it, but it was a setup. You have been arrested by the police.")
    failGame()

def doNothingWithDog():
    print("TODO: do nothing with dog")

def buyGreenMilk():
    choices = [
        "💣Throw green milk at robber",
        "🚪Let robber get away"
    ]        

    print("TODO: green milk")
    choice = askUserToChoose(choices)
    if (choice == 1): #throw green milk at robber
        throwGreenMilkAtRobber()
    elif (choice == 2): #let robber get away
        goToWork()

def throwGreenMilkAtRobber():
    global aura
    aura += 1

    print("TODO: throw green milk")
    print("⏳Current aura:", aura)
    goToWork()

def buyRegularMilk():
    print("You buy regular milk for $40. Your wallet feels much lighter, but hey, you only live once, right?")
    goToWork()

def stealMilk():
    print("You shove the milk carton down your pants, but security catches you red-handed. The Store Manager calls in the cavalry.")
    failGame()

def goToWork():
    choices = [
        "🤝Offer to help your coworker",
        "🗣️Report them to your boss",
        "🔪Secretly make their work harder"
    ]
    
    print("At work, you notice the only female coworker, Sarah, looking really stressed. She's struggling to meet a deadline and looks like she might crash out. What do you do?")
    choice = askUserToChoose(choices)
    if (choice == 1): #offer to help your coworker
        helpCoworker()
    elif (choice == 2): #report them to your boss
        reportCoworker()
    elif (choice == 3): #make their work harder
        makeWorkHarder()

def helpCoworker():
    global aura
    global haveDog

    if haveDog:
        aura += aura #double aura
        print("TODO: have dog")
    else:
        aura += 1
        print("TODO: dont have dog")

    goSkydiving()

def reportCoworker():
    global aura
    aura -= 1
    
    print("TODO")
    goSkydiving()

def makeWorkHarder():
    print("With malice in your eyes, you intentionally mess with Sarah's work files to make her work even harder. When she discovers this, she reports you to HR. You're sacked immediately!")
    failGame()

def goSkydiving():
    global aura

    print("🪂You decide to go skydiving with Sarah. It was a blast.") 

def failGame():
    global aura
    
    print("❌Game over, loser. Restart the program to try again.")
    print("⏳Current aura:", aura)

def endGame():
    global aura
    global name
    
    print("Your day is coming to an end. Let's see how you did...")
    print (f"{name}, your final score is: {aura} Aura")

    if (aura >= 4):
        print ("🍀MODEL CITIZEN ENDING: What an incredible day! You've made a real difference today. The community is lucky to have a model citizen like you.")
    elif (aura >= 1):
        print ("🤷‍♂️MEH ENDING: You had a mixed day with some good choices and some missed opportunities. You made decent decisions, but there is always room for improvement.")
    else:
        print ("😈WORST POSSIBLE ENDING: You horrible piece of human scum! I doubt you even have a soul at this point. You've made a million enemies, caused pain, and acted with poor judgement. You need to seriously rethink your life choices.")

#user starts off with 0 aura, then earns more aura as the CYOA progresses
aura = 0

#user starts off with no dog
haveDog = False

#ask for name
name = input("What is your name? ")
print(f"👋 Hello, {name}. Try not to get into any trouble!\n")

#start game
encounterDog()
