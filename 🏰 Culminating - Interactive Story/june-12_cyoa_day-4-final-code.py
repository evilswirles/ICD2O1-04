###CYOA - DAY 4 FINAL CODE###
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
    
    print("You are walking down the street and encounter a lost dog. What do you do?")
    choice = askUserToChoose(choices)
    if (choice == 1):   #try and find its owner
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
    print("✔️You gain 1 aura")
    print("⏳Current aura:", aura)

    print("\n")
    print("You decide to buy some milk at your local 7/11. You walk up to the fridge, but there's so many different options, you don't know which one to choose.")

    choices = [
        "🧪Buy that weird green glowing milk",
        "🥛Buy regular milk ($40)",
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
    print("The dog ends up biting you on the arm, and you contract life-threatening rabies. In the end, you perish.")
    failGame()

def dogLikesYou():
    global aura, haveDog
    aura += 1
    haveDog = True

    print("After finding out that the lost dog likes you, you decided to head to you local pet store to buy some dog toys and dog treats.")
    goToPetStore()

def goToPetStore():
    pickpocketed = random.randint(1, 2)
    if (pickpocketed == 1): #pickpocketed; can't pay for toy
        cantPayForToy()
    else:
        payForToy() #pay for toy

def cantPayForToy():
    print("As your getting ready to pay, realization hits you. Turns out some homeless guy pickpocketed you, and your dog was no snitch.")
    failGame()

def payForToy():
    global aura
    aura += 1
    
    print("Your dog is one happy camper.")
    print("✔️You gain 1 aura")
    print("⏳Current aura:", aura)
    print("\n")

    goToWork()

def eatDog():
    print("You disgusting piece of human trash. You decide to bring the dog back to your house, and try to cook and eat it, but it was a setup all along. You have been arrested by the police.")
    failGame()

def doNothingWithDog():
    print("You stare at the dog, and the dog stares back at you with sadness in its eyes. In the end, you decide to just mind your own business.")
    print("🔄You do not gain any aura.\n")
    goToWork()

def buyGreenMilk():
    choices = [
        "🦸‍♂️Throw green milk at robber",
        "🚪Let robber get away"
    ]        

    print("You see criminal scum trying to rob the local 7/11. What do you do?")
    choice = askUserToChoose(choices)
    if (choice == 1): #throw green milk at robber
        throwGreenMilkAtRobber()
    elif (choice == 2): #let robber get away
        print("🔄You do not gain any aura.\n")
        goToWork()

def throwGreenMilkAtRobber():
    global aura
    aura += 1

    print("For some reason your green milk has turned hard, so you decide to chuck the milk carton at the robbers head. Good decision. You become a local hero.")
    print("✔️You gain 1 aura")
    print("⏳Current aura:", aura)
    print("\n")
    goToWork()

def buyRegularMilk():
    print("You buy regular milk for $40. Your wallet feels much lighter, but hey, you only live once, right?\n")
    goToWork()

def stealMilk():
    print("You decide to shove the milk carton down your pants, but security catches you red-handed. The Store Manager calls in the cavalry.")
    failGame()

def goToWork():
    choices = [
        "🤝Offer to help your coworker",
        "🗣️Report them to your boss",
        "🔪Secretly make their work harder"
    ]
    
    print("At work, you notice the only female coworker, Sarah, is looking really stressed. She's struggling to meet a deadline and looks like she might crash out. What do you do?")
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
        aura += 2
        print("You offer to help Sarah with her deadline. She's so grateful and mentions she loves dogs. Your dog barks happily, making her smile even more.")
        print("✔️You gain 2 aura (bonus from having dog)")
        print("⏳Current aura:", aura)
    else:
        aura += 1
        print("You offer to help Sarah with her deadline. She's so grateful for your assistance.")
        print("✔️You gain 1 aura")
        print("⏳Current aura:", aura)
    
    print("\nYou and Sarah work together for the next few hours, and you manage to help her meet her deadline just in time!")
    print("Sarah is so relieved and grateful that she suggests you both celebrate by doing something fun together.")
    print("\"I know this might sound crazy\", Sarah says, \"but I've always wanted to try skydiving. Want to join me?\"")
    print("\n")
    goSkydiving()

def reportCoworker():
    global aura
    aura -= 1
    
    print("You decide to report Sarah to your boss for being behind on her work. Your boss appreciates the heads up but Sarah gives you the cold shoulder for the rest of the day.")
    print("❌You lose 1 aura")
    print("⏳Current aura:", aura)
    print("\n")
    goSkydiving()

def makeWorkHarder():
    print("With malice in your eyes, you intentionally mess with Sarah's work files to make her work even harder. When she discovers this, she reports you to HR. You've been terminated for workplace sabotage.")
    failGame()

def goSkydiving():
    global aura

    choices = [
        "🪂Say yes to skydiving",
        "🐔Say no to skydiving"
    ]

    print("You decide to go on a skydiving adventure with Sarah.")
    choice = askUserToChoose(choices)
    if (choice == 1): #say yes to skydiving
        print("You say yes to skydiving with Sarah.")
        aura += 1
        print("✔️You gain 1 aura")
        print("⏳Current aura:", aura)
        print("\n")
        proposalFromSarah()
    elif (choice == 2): #say no to skydiving
        print("You chicken out at the last moment, leaving Sarah to skydive alone.")
        endGame()

def proposalFromSarah():
    global aura

    choices = [
        "💍Say yes to proposal",
        "💔Say no to proposal"
    ]

    print("After an amazing skydiving experience, Sarah decides to propose to you.")
    choice = askUserToChoose(choices)
    if (choice == 1): #say yes to proposal
        sayYesToProposal()
    elif (choice == 2): #say no to proposal
        curseOnYourBloodline()

def sayYesToProposal():
    global aura
    aura += aura #double aura

    print("You say \"Yes\" to Sarah's proposal. She is beyond happy.")
    print("✔️You gain double aura")
    print("⏳Current aura:", aura)
    print("\n")
    endGame()

def curseOnYourBloodline():
    global aura
    aura -= 1 #deducts aura by 1

    print("You say \"No\" to Sarah's proposal. Massive screw up as Sarah's family gets wind of what happened and places a curse on your bloodline. Womp womp.")
    print("❌You lose 1 aura")
    print("⏳Current aura:", aura)
    print("\n")
    endGame()

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
        print ("😈WORST POSSIBLE ENDING: You kind of people make me sick! I doubt you even have a soul at this point. You've made a million enemies, caused pain, and acted with poor judgement. You need to seriously rethink your life choices.")

#user starts off with 0 aura, then earns more aura as the CYOA progresses
aura = 0

#user starts off with no dog
haveDog = False

#ask for name
name = input("What is your name? ")
print(f"👋 Hello, {name}. Try not to get into any trouble!\n")

#start game
encounterDog()
