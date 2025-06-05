###QUESTION 1###
aC = float(input("How much money is in your checking account? "))
aS = float(input("How much money is in your savings account? "))

if (aC > 1000) or (aS > 1500):
    sC=0
else:
    sC=0.15 #if you do not have more than the specified amount in your account, you receive a 0.15 charge

print("Your service charge is", sC, "per cheque")
