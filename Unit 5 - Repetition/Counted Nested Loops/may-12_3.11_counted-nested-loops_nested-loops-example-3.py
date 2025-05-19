###NESTED LOOPS - EXAMPLE 3###
import random

#user input
#get multiple symbols from the user
symbol = input("Enter symbols separated by spaces (e.g., ! @ $ %): ").split()
low = int(input("Enter the number to start at: "))
high = int(input("Enter the number to end at: "))

#print the number and random symbols in a mixed order
for i in range(low, high + 1):
    print(i, end=" ")

    for j in range(i):
        #randomly pick one symbol from the list and output it each time
        print(random.choice(symbol), end="")

    print("\n")
