###QUESTION 2###
def calculate_discount(tv_type, size):
    if (tv_type == "plasma"):
        discount = 5  # 5% for plasma
    elif (tv_type == "LCD"):
        if (size == 30):
            discount = 8  # 8% for 30" LCD
        elif (size == 42):
            discount = 10  # 10% for 42" LCD
        else:
            discount = 0  # No discount for other sizes of LCD
    else:
        discount = 0  # No discount for other TV types

    return discount

tv_type = input("Enter the TV type (plasma/LCD): ").lower()
size = int(input("Enter the TV size (in inches): "))

discount = calculate_discount(tv_type, size)
if discount == 0:
    print("No discount.")
else:
    print(f"Discount is {discount}% of the selling price.")
