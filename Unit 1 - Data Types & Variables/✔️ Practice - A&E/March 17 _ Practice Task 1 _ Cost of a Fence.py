#input
l = float(input("What is the length of your backyard? "))
w = float(input("What is the width of your backyard? "))


#processing
p = l + l + w + w
c = 22.25
totalC = p * c

print("Total cost is ", totalC)


#output
#calculating the tax
tax = totalC * 0.13
total = totalC + tax 

#rounding the final cost within two decimals
total = round(total, 2)

#output // The Final Cost
print ("Total cost of the fence is ", total)
