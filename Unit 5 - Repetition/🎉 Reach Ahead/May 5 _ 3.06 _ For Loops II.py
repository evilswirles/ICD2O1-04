###PRACTICE - CODE RUN###
sum = 0

print("\n")
print("This program will add 3 integers.")

for i in range (3):
    num = int(input("Enter number: "))
    sum += num

print("The sum is ", sum)


###QUESTION 1###
total_win = 0
total_lose = 0

print("This program...")
print("")

for i in range (10):
    print("Game", i+1, ": ")

    #asks you to input the result of the game, 10 times
    r = input("Enter the result of game (W) or (L): ")
    print("")

    #calculating the total wins
    if (r == "W"):
        total_win = total_win + 1

    #calculating the total losses
    elif (r == "L"):
        total_lose = total_lose + 1

    else:
        #entering an invalid letter other than "W" or "L" will output this response
        print("This is an invalid entry")
        print("")

    print("The total Wins so far is", total_win)
    print("The total Loses so far is", total_lose)
    print("")

print("You have won", total_win, "games.") #tells you the total amount of games won
print("")
print("You have lost", total_lose, "games.") #tells you the amount of games lost
print("")


###QUESTION 2###
hst_rate = 0.13 #the HST rate

#asks the user how many grocery items that they have
grocery_items = int(input("Input the number of grocery items: "))

cost_total = 0.0 #the total cost

#using a for loop to get the cost of each grocery item. If you input 20 items, cost for each item
for i in range(1, grocery_items + 1):
    cost = float(input(f"Enter the cost of item #{i}: $"))
    cost_total += cost

#calculate the HST and final total
hst = cost_total * hst_rate
final_total = cost_total + hst_rate

#displays the total results
print(f"\nSubtotal: ${cost_total:.2f}")
print(f"HST (13%): ${hst:.2f}")
print(f"Total cost: ${final_total:.2f}")


###QUESTION 3###
total = 0

for i in range(5):
    mark = float(input(f"Enter your current mark {i + 1}: "))
    total += mark

average = total / 5
print("Average of the marks inputted: ", average)