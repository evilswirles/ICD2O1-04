###QUESTION 2###
total = 0

#sequence 1
for a in range(1, 1237, 1):
    print(a)
    total = total + a

#sequence 2
for a in range(2, 8001, 3):
    print(a)
    total = total + a

#sequence 3
for a in range(-10, 11, 2):
    print(a)
    total = total + a

#sequence 4
for a in range(100, -101, -1):
    print(a)
    total = total + a

#sequence 5
for a in range(101, 202, 5):
    print(a)
    total = total + a

#output
print("Cumulative total is:", total)
