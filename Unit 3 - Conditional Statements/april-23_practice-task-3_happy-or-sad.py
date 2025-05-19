dogName = input("What is the name of your dog? ") #input the name of your dog

smallTreat = int(input("How many small treats? ")) #small treats
mediumTreat = int(input("How many medium treats? ")) #medium treats
largeTreat = int(input("How many large treats? ")) #large treats

score = 1 * smallTreat + 2 * mediumTreat + 3 * largeTreat


print("Your dog's name is", dogName)

if (score >= 10):
    print("your dog is happy")
else:
    print("Your dog is sad")
