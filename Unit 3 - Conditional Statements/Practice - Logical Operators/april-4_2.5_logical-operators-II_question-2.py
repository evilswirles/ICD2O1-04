###QUESTION 2###
rfTire = int(input("What is the tire pressure in the right front tire? ")) #right front tire
rlTire = int(input("What is the tire pressure in the right left tire? ")) #right left tire
rrTire = int(input("What is the tire pressure in the right rear tire? ")) #right rear tire
lrTire = int(input("What is the tire pressure in the left rear tire? ")) #left rear tire

if (rfTire == rlTire) and (rrTire == lrTire):
    print("Tire pressure is OK")
else:
    print("Tire pressure is not OK")
