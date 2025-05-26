###EXERCISE 1###
import random

numbers = set()

while len(numbers) < 3:
    #generates 3 random integers between 100 and 999 that is divisible by 5
    num = random.randint(100, 999)
    if (num % 5 == 0):
        numbers.add(num)

print(list(numbers))
