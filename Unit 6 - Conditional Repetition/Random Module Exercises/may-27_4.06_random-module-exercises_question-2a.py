###QUESTION 2A###
import random

#initializing the variables
tosses = []
headsCount = 0 #starting at 0


for i in range(20): #coin will be tossed 20 times
    #randomizes the output of either Heads or Tails
    toss = random.choice(['Heads', 'Tails'])
    tosses.append(toss)
    #makes sure that if there is a "Heads", it will add it to "headsCount"
    if (toss == 'Heads'):
        headsCount += 1

print("Coin Tosses:", tosses)
print("Number of Heads:", headsCount)
