###QUESTION 1###
numberOfRows = 7

for i in range(0, numberOfRows):
    print(" " * (numberOfRows - i), "*", end="")

    for j in range(1, i + 1):
        print("**", end="")
    print("")
