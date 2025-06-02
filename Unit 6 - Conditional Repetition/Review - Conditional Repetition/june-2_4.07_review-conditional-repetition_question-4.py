###PART 1 - CODING QUESTIONS###
###QUESTION 4###
import random
headCount = 0
flipCount = 0

headTarget = int(input("Please enter the number of heads: "))

while (headCount < headTarget):
    flip = random.randint(0, 1)
    flipCount += 1

    if (flip == 1): #heads
        print("Heads")
        headCount += 1
    else:
        print("Tails")
        
print("Total flips:", flipCount)
