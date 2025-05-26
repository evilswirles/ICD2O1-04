###EXERCISE 2###
import random #to make sure all tickets are completely random

#tickets are stored in a list
tickets = [] #list
count = 0 #initializes the count to 0

#generates 100 tickets
while (count < 100):
    ticket = random.randrange(100000, 1000000)
    #if the ticket already exists...
    found = False
    i = 0
    while (i < count):
        if (tickets[i] == ticket):
            found = True
        i = i + 1

    if (found == False):
        tickets.append(ticket)
        count = count + 1

#two different winners are picked each time the program is ran
win1 = random.randrange(0, 100)
win2 = random.randrange(0, 100)

while (win1 == win2):
    win2 = random.randrange(0, 100)

#tickets are printed
print("Tickets:")
i = 0
while (i < 100):
    print("*", tickets[i])
    i = i + 1

#winners are printed
print("\nWinning Tickets:")
print("*", tickets[win1])
print("*", tickets[win2])
