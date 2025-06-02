###PART 1 - CODING QUESTIONS###
###QUESTION 3###
import random
done = False
sumOfNumbers = 0

while not done:
    number1 = random.randint(-5, 5)
    number2 = random.randint(-5, 5)
    print("N1:", number1, "N2:", number2)

    if (number1 == -number2):
        done = True
    else:
        sumOfNumbers += number1
        sumOfNumbers += number2

print("Sum of numbers: ", sumOfNumbers)
