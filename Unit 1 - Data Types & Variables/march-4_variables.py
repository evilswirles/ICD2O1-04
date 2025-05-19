###Part 1###
a = 5
b = "NAME"
c = 4.3232
d = "4.3232"
e = True
f = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
g = 4.3232 + 4.1234 + 2.3212


###Part 2###
a = 3
b = 6
c = 9

print("a + b x c = " , a+b*c)


###Part 3###
a = 3
b = 6
c = 9
d = 10

print("a + b x c =\n" , a+b*c)
print("a + b x c - d = " , a+b*c-d)


###Part 4###
#import math

#a = input("enter base of triangle = ")
#b = input("enter height of triangle = ") #14.1

#area = a*b/2
#area = round(area, 2)


###Part 5###


###Part 6###
import math

student_name = "Ryan Chi-Wai Bower"
school = "Western Technical-Commercial School"
year = "2023   2024"
student_number = "348763681"

card = f"""
{'='*40}
            TDSB STUDENT CARD        
{'='*40}
Name:           {student_name}
School:         {school}
year:           {year}
Student Number: {student_number}
{'='*40}
"""

print("\n" * 10)  #vertical spacing
print(card)
