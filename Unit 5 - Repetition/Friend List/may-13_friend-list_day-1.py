###STEP 1 - GET THE LIST OF FRIENDS###
list1 = []  #friends names are stored in this list

#user input
numberOfFriends = int(input("How many friends do you want to enter? "))

for i in range(numberOfFriends):
    n = input("Enter name of friend #" + str(i + 1) + ": ")
    list1.append(n)

###STEP 2 - DISPLAY THE ORIGINAL LIST OF FRIENDS###
print("\nList of your friends:")
for friend in list1:
    print("• " + friend)

###STEP 3 - GET THE 'BEST FRIENDS' LIST FROM ORIGINAL LIST###
list2 = []  #best friend names are stored in this list

bestFriendCount = int(input("\nHow many friends do you want to add to your Best Friends list? "))

print("Please enter the names of your best friends from the original list.")

while len(list2) < bestFriendCount:
    entry = input(f"Enter best friend name(s) ({bestFriendCount - len(list2)} remaining): ")

    #handle comma-separated input
    names = [name.strip() for name in entry.split(",")]

    for name in names:
        if name in list1:
            if name not in list2:
                list2.append(name)
                print(f"✅ Added: {name}")
            else:
                print(f"⚠️ {name} is already in your Best Friends list.")
        else:
            print(f"❌ {name} is not in your original friends list.")

###STEP 4 - DISPLAY THE BEST FRIENDS LIST###
print("\nYour Best Friends List:")
for bestFriend in list2:
    print("• " + bestFriend)
