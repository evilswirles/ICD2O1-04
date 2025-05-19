def ticket_price(age):
    if age >= 0 and age <= 5:
        return "FREE"
    elif age >= 6 and age <= 12:
        return "$10"
    elif age >= 13 and age <= 17:
        return "$15"
    elif age >= 18:
        return "$20"
    else:
        return "Invalid age"

try:
    age = int(input("Enter the age of the visitor: "))
    price = ticket_price(age)
    print(f"The price of a ticket for a {age}-year-old is: {price}")
except ValueError:
    print("Please enter a valid number for age. Age is not valid if it includes decimals. Please input age as a whole number.")













