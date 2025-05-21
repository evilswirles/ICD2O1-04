###QUESTION 2###
total = 0 #total is set at the starting number, 0

while True:
    num = int(input("Enter an integer (negative to stop): "))
    if (num < 0): #if the number is less than 0
        break
    total += num * num  #square of the number and add to total

print("Sum of squares:", total) #output the sum of the square and the total
