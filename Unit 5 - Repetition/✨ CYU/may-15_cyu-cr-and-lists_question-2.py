###QUESTION 2###
#create a list containing ten positive integers
list2 = ["5", "5", "15", "20", "20", "30", "35", "40", "50", "50"]

#use a for loop to square each number in the list (list2)
numbersSquared = []
for num in list2:
    numberInt = int(num)
    squared = numberInt * numberInt
    numbersSquared.append(squared)

#using a for loop iterates through the modified list
#for each number; if the number is greater than 60 print it
print("Numbers that are greater than 60: ")
for num in numbersSquared:
    if num > 60: #verifies that the number is greater than 60
        print(num)

