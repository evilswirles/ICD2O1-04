###Question 2###
q1 = int(input("What is 5 + 5?"))
q2 = int(input("What is 100 * 50 / 20?"))
q3 = int(input("What is 70 + 1000 / 10?"))
q4 = int(input("What is 90 + 90?"))
q5 = int(input("What is 10 + 1000?"))

#solving the problems
a1 = 5+5
a2 = 100*50/20
a3 = 70+1000/10
a4 = 90+90
a5 = 10+1000

print("5+5=", a1, "you inputted", q1)
print("100*50/20=", a2, "you inputted", q2)
print("70+1000/10=", a3, "you inputted", q3)
print("90+90=", a4, "you inputted", q4)
print("10+1000=", a5, "you inputted", q5)


###Question 3###
name = input("What's your name? ")
age = int(input("How old are you? "))
current_year = int(input("What year is it? "))

age_25 = current_year + (25 - age) if age < 25 else "already 25+"
age_50 = current_year + (50 - age) if age < 50 else "already 50+"
age_75 = current_year + (75 - age) if age < 75 else "already 75+"

print(f"Hello, {name}!")
print(f"You will turn 25 in: {age_25}")
print(f"You will turn 50 in: {age_50}")
print(f"You will turn 75 in: {age_75}")


###Question 4###
pi = 3.14159

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * pi * radius
area = pi * radius ** 2

print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.2f}")

