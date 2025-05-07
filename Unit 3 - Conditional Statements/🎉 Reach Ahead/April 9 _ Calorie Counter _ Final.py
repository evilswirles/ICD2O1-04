#calorie counter heading
print("\n")
print("####################################################")
print("#   Welcome to Waffle's Gluttonous Food Emporium   #")
print("#                 Established 2025                 #")
print("####################################################")
name = input("Name for the order: ")
print("\n")

#menu item calorie lists
burgers = [950, 800, 200, 0]  #options 1-4
sides = [400, 200, 60, 1000, 0]  #options 1-5
drinks = [235, 230, 118, 0]  #options 1-4
desserts = [200, 300, 300, 90, 0]  #options 1-5

#burger choice
print("Here are the four burger choices:")
print("1 - Triple Cheeseburger with melted cheese (950 calories)")
print("2 - Fish Burger with Cheese (800 calories)")
print("3 - Veggie Burger (200 calories)")
print("4 - No burger")
burger_choice = int(input("Please enter one burger choice: ")) - 1
print("\n")

#make sure the burger choice is correct
if (burger_choice < 0) or (burger_choice >= len(burgers)):
    print("Invalid burger choice. You will get 'No burger'.")
    burger_choice = 3  #no burger
elif (burger_choice == 3):
    print("You have chosen No burger.")
else:
    print(f"You have chosen a burger with {burgers[burger_choice]} calories.")

#side choice
print("Here are the five side order choices:")
print("1 - Loaded fries (400 calories)")
print("2 - Onion Rings (200 calories)")
print("3 - Baked Potato (60 calories)")
print("4 - Salad that can feed a family of eight (1000 calories)")
print("5 - No side order")
side_choice = int(input("Please enter one side order choice: ")) - 1
print("\n")

#make sure the side choice is correct
if (side_choice < 0) or (side_choice >= len(sides)):
    print("Invalid side choice. You will get 'No side order'.")
    side_choice = 4  #no side order
elif (side_choice == 4):
    print("You have chosen No side order.")
else:
    print(f"You have chosen a side with {sides[side_choice]} calories.")

#drink choice
print("Here are the four drink choices:")
print("1 - Soft Drink (235 calories)")
print("2 - Root Beer Float (230 calories)")
print("3 - Malk (118 calories)")
print("4 - No drink")
drink_choice = int(input("Please enter one drink choice: ")) - 1
print("\n")

#make sure the drink choice is correct
if (drink_choice < 0) or (drink_choice >= len(drinks)):
    print("Invalid drink choice. You will get 'No drink'.")
    drink_choice = 3  #no drink
elif (drink_choice == 3):
    print("You have chosen No drink.")
else:
    print(f"You have chosen a drink with {drinks[drink_choice]} calories.")

#dessert choice
print("Here are the five dessert choices:")
print("1 - Apple Pie (200 calories)")
print("2 - Sundae (300 calories)")
print("3 - Soft Serve Ice Cream from our totally not broken machine (300 calories)")
print("4 - Fruit Cup (90 calories)")
print("5 - No dessert")
dessert_choice = int(input("Please enter one dessert choice: ")) - 1
print("\n")

#make sure the dessert choice is correct
if (dessert_choice < 0) or (dessert_choice >= len(desserts)):
    print("Invalid dessert choice. You will get 'No dessert'.")
    dessert_choice = 4  #no dessert
elif (dessert_choice == 4):
    print("You have chosen No dessert.")
else:
    print(f"You have chosen a dessert with {desserts[dessert_choice]} calories.")

#calculate the total calories
total_calories = (
    burgers[burger_choice] +
    sides[side_choice] +
    drinks[drink_choice] +
    desserts[dessert_choice]
)

#output total calories w/ message for total calories
print(f"{name}, your total calorie count is: {total_calories} calories.")

if (total_calories > 2000):
    print("Fatty. You made some not so healthy choices. Go for a walk.")
elif (total_calories > 1500):
    print("todo")
else:
    print("Good for you. You made some healthy choices")

print("Thank you for visiting Waffle's Gluttonous Food Emporium.")
