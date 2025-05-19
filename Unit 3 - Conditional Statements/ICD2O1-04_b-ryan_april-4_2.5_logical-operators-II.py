###QUESTION 1###
#aC = float(input("How much money is in your checking account? "))
#aS = float(input("How much money is in your savings account? "))

#if (aC > 1000) or (aS > 1500):
    #sC=0

#else:
    #sC=0.15 #if you do not have more than the specified amount in your account, you receive a 0.15 charge

#print("Your service charge is", sC, "per cheque")


###QUESTION 2###
#rfTire = int(input("What is the tire pressure in the right front tire? ")) #right front tire
#rlTire = int(input("What is the tire pressure in the right left tire? ")) #right left tire
#rrTire = int(input("What is the tire pressure in the right rear tire? ")) #right rear tire
#lrTire = int(input("What is the tire pressure in the left rear tire? ")) #left rear tire

#if (rfTire == rlTire) and (rrTire == lrTire):
    #print("Tire pressure is OK")

#else:
    #print("Tire pressure is not OK")


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


###QUESTION 4 - BONUS QUESTION###
