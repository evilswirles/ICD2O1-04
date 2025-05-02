###QUESTION 1A###
#for j in range(10, 0, -2):
    #print(j)


###QUESTION 1B###
#for p in range(1, 10):
    #print("go")


###QUESTION 1C###
#for j in range(0, 12):
    #print(j)


###QUESTION 1D###
#for j in range(1, 10, -1):
    #print(j)


###QUESTION 1E###
#for n in range(1, 4):
    #print(n * n)
    #print(n + 10)
    #print(n - 1)


###QUESTION 1F###
#for j in range(-5, 3, 2):
    #print(j)


###QUESTION 1G###
#for p in range(0, 10):
    #print("go", end="")


###QUESTION 1H###
#for n in range(1, 6):
    #print("n\n")


###QUESTION 2A###
#for count in range(0, 5, 1):
    #print(str(count))


###QUESTION 2B###
#for count in range(5, 0, -1):
    #print(str(count))


###QUESTION 3A###
#for i in range(1, 21):
    #print(i)


###QUESTION 3B###
#for i in range(1, 50, 2):
    #print(i)


###QUESTION 3C###
#for p in range(0, 20):
    #print("ryan", end="")


###QUESTION 3D###
#user_name = input("Please enter in your name: ")
#n = int(input("How many times do you want your name printed? "))

#for i in range(n):
    #print(user_name)


###QUESTION 3E###
#for i in range(100, 0, -10):
    #print(i)


###QUESTION 3F###
#number = int(input("Please enter a positive integer: "))

#for i in range(number, 0, -1):
    #print(i)

#print("Blast off! 🚀")


###QUESTION 3G###
m = int(input("Please enter the starting integer: "))
n = int(input("Please enter the ending integer: "))
s = int(input("Please enter the step value: "))

if (s == 0):
    print("Step value cannot be 0.")
elif (m < n) and (s > 0) or (m > n) and (s < 0):
    for i in range(m, n + (1 if s > 0 else -1), s):
        print(i)
else:
    print("Step value does not allow reaching from m to n.")
