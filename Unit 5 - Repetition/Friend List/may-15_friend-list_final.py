import random

###STEP 1 - GET THE LIST OF FRIENDS###
friends = []

print("Welcome! Please enter the first name of each friend. Press \"d\" when your are done.")

done = False
while not done:
    name = input()
    if (name == "d"):
        done = True
    else:
        friends.append(name)

###STEP 2 - DISPLAY THE ORIGINAL LIST OF FRIENDS###
def printNames(names):
    for idx, name in enumerate(names):
        print(f"{idx + 1}. {name}")

friendCount = len(friends)
print(f"\nYou have entered {friendCount} friends.")
printNames(friends)

###CHALLENGE - PART 1###
movieFriends = []

#check if there are at least 2 friends to choose from
if len(friends) < 2:
    print("\nYou do not have enough friends to go to the movies with 😥")
    print(f"You currently have {len(allFriends)} friend(s).")
else:
    #randomly select 2 unique friends
    movieFriends = random.sample(friends, 2)

    #display the movie friends
    print("\nThe two friends going to the movies with you are: ", end="")
    print(", ".join(movieFriends))

###STEP 3 - GET THE "BEST FRIENDS" LIST FROM ORIGINAL LIST###
bestFriends = []
friendNumbers = []

print("\nWhich friends would you like to move to your Best Friends list?")
print("Type the number of each friend in the Friends list and 0 when done.")

done = False
while not done:
    friendNumber = int(input())
    if (friendNumber == 0): #check for done
        done = True
    elif (friendNumber < 0) or (friendNumber > friendCount): #validate friend number
        print("Invalid friend number.")
    else: #valid friend number
        if friendNumber not in friendNumbers:
            friendNumbers.append(friendNumber)

#move friends in reverse order so friend numbers don't change
friendNumbers.sort(reverse=True)
for friendNumber in friendNumbers:
    idx = friendNumber - 1
    name = friends.pop(idx)
    bestFriends.append(name)
        
bestFriends.reverse()

###STEP 4 - DISPLAY THE BEST FRIENDS LIST###
print("\nHere are your Friends:")
printNames(friends)

print("\nHere are your Best Friends:")
printNames(bestFriends)
