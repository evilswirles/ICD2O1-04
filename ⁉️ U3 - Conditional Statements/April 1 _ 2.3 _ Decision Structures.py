name = input("What is your name? ")

print("It is nice to meet you", name)

print("Select the number that represents how you are feeling today.")
print("Excited = 1, Happy = 2, OK = 3, Tired = 4")
print("\n")

feeling = int(input("How are you feeling today? "))

if(feeling == 1):
    print("You chose option 1, therefore you are Excited")

elif(feeling == 2):
    print("You chose option 2, therefore you are Happy")

elif(feeling == 3):
    print("You chose option 3, therefore you are OK")

elif(feeling == 4):
    print("You chose option 4, therefore you are Tired")

else:
    print("Invalid input")
