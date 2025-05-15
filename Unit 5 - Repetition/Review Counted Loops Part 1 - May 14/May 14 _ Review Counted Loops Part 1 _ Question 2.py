###QUESTION 2###
list1 = [] #list to store the 10 numbers

odd = 0
even = 0

for a in range(10):
    #asks the user to input 10 numbers, user input
    n = int(input("Enter number " + str(a + 1) + ": "))
    list1.append(n)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Numbers entered:", list1)
print("Odd numbers:", odd)
print("Even numbers:", even)
