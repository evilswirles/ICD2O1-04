###PART 1 - CODING QUESTIONS###
###QUESTION 2###
import random
positive = 0
negative = 0
number = 1

print("Numbers:")

while (number != 0):
    number = random.randint(-50, 50)
    print(number)
    
    if (number > 0):
        positive += 1
    elif (number < 0):
        negative += 1

print("Positive:", positive)
print("Negative:", negative)

total = positive + negative
if (total > 0):
    negativePercent = positive * 100 / total
    negativePercent = negative * 100 / total
    print("Positive percent:", negativePercent)
    print("Negative percent:", negativePercent)
else:
    print("Zero was first!")
