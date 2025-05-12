###NESTED LOOPS - EXAMPLE 2###
#print the number
for i in range(1, 11):
    print(i, end="")

    #print the right number of stars
    for j in range(i):
        print("*", end="")

    print("")
