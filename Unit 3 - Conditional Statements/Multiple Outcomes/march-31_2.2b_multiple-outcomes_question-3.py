###QUESTION 3###
weight = float(input("Enter your weight in kg: "))

if (weight > 80):
    print("You are classified as Heavy Weight.")
elif (60 <= weight <= 80):
    print("You are classified as Medium Weight.")
else:
    print("You are classified as Light Weight.")
