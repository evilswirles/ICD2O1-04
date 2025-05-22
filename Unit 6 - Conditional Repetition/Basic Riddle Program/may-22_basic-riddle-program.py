###BASIC RIDDLE PROGRAM###
#start
tries = 1 #initializes at 1

#riddle
print("What gets wetter the more it dries? ")
answer = input("Input your answer/guess for the riddle: ")


if (tries < 3) and (answer != "Towel"):
    print("Incorrect. Try again.")
    tries += 1

    print("What gets wetter the more it dries?")
    answer = input("Input your answer/guess for the riddle: ")

    #second guess out of three
    if (tries < 3) and (answer != "towel"):
        print("Incorrect. Try again.")
        tries += 1

        print("What gets wetter the more it dries?")
        answer = input("Input your answer/guess for the riddle: ")

        #third guess out of three
        if (tries < 3) and (answer != "towel"):
            print("Incorrect. Try again.")
            tries += 1

            print("What gets wetter the more it dries?")
            answer = input("Input your answer/guess for the riddle: ")

#final
if (answer == "Towel"):
    print("Good job!")
else:
    print("Three tries are up. The riddle was \"Towel\"")
