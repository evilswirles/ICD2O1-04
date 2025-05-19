###TRY IT OUT###

#user input
print("Inputing the numbers will get them added up;")
print("All numbers entered will be added up, until a zero is inputted")

total = 0
#asks the user for them to enter a number, keeps looping
number = int(input("Number: "))

while number != 0:
    total += number
    print(f"The total so far is {total}")
    number = int(input("Number: "))

print(f"\nThe total is {total}") #prints the total

