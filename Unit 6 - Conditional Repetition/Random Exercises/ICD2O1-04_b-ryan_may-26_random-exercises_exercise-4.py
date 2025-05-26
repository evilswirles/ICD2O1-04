###EXERCISE 4###
doubles = 0

for i in range(1, 4):
    dice1 = int(input(f"Roll {i} - Enter first die: "))
    dice2 = int(input(f"Roll {i} - Enter second die: "))
    if dice1 == dice2:
        doubles += 1

print("Doubles rolled:", doubles)
