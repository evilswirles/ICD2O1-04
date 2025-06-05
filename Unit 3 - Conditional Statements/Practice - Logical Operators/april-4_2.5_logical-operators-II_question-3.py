###QUESTION 3###
chocChip = int(input("How many boxes of Chocolate Chip cookies do you wish to purchase? "))
raisin = int(input("How many boxes of Raisin do you wish to purchase? "))
shortbread = int(input("How many boxes of shortbread do you wish to purchase? "))

#calculations
totBoxes = chocChip + raisin + shortbread
cost = totBoxes * 6.95

#output
if (chocChip == 5) or (raisin == 5) or (shortbread == 5):
    d = 0.10
    print("\n!!You get a 10% discount!!")
    print("Your final price is:")
elif (chocChip < 0) or (raisin < 0) or (shortbread < 0):
    print("Invalid.")
else:
    d = 0
    print("Your final price with tax for the boxes of cookies is:")

#final cost
d = cost * d
subTot = cost - d
tax = subTot*0.13
total = subTot+tax
total = round(total,2)
print(total)
