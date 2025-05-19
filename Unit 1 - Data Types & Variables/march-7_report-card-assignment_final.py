import math
import sys

###IDLE COLOURS###
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")


#asks user to input information
nameFirst = input("What is your FIRST name? ")
nameLast = input("What is your LAST name? ")
city = input("What is your City? ")
province = input("What is your Province? ")
schoolName = input("What is your School? ")
mathGrade = float(input("What is your math grade? "))
englishGrade = float(input("What is your English grade? "))
computerGrade = float(input("What is your Computer Science grade? "))


#calculations for class average
def calculate_class_average(mathGrade, englishGrade, computerGrade):
    #calculate the average of the three grades; math, english, cs
    return (mathGrade + englishGrade + computerGrade) / 3


#report card header
print("\n")
print("#########################################")
print("#            Student Report             #")
print("#             WESTERN TDSB              #")
print("#########################################")
print("\n")

#prints information
print("Student name: ", nameFirst, nameLast)
print("Current marks for", nameFirst, "are:\n")
print("Math: ", mathGrade)
print("English: ", englishGrade)
print("Computer Science (CS): ", computerGrade, "\n")


#calculates the class average based on course grades inputted by user
class_average = calculate_class_average(mathGrade, englishGrade, computerGrade)
print(f"\nThe class average is: {class_average:.2f}%")

#check if the class average is 70 percent or above
if class_average == 70:
    color.write("The class average is exactly 70 percent.\n","BUILTIN")
elif class_average > 70:
    color.write("The class average is above 70 percent.\n","STRING")
else:
    color.write("The class average is below 70 percent.\n","COMMENT")

print("All student reports are to be returned to:", schoolName, "\n")
print("City/Province: ", city, "-", province)
