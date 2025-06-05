money = float(input("How much money did you spend? "))
purchase = int(input("How many widgets did you purchase? "))

purchase = purchase * money
purchase = round(purchase, 2)

d = 0

if (purchase < 0) or (money < 0):
    print("Invalid")
elif (purchase > 325) or (money > 1000):
    print("You get a discount if 158")
    d = purchase*0.15
else:
    print("Completed purchase. Enjoy your purchase of widgets!")

total = purchase - d
tax = total *0.13
finalTotal = total + tax
