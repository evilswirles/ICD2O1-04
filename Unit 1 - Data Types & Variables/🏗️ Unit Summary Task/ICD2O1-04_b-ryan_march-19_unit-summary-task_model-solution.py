import math
import sys

###IDLE COLOURS -- DO NOT CHANGE###
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")


#asks user to input information
nameFirst = input("What is your FIRST name? ")
nameLast = input("What is your LAST name? ")
workAvailable = input("How many days a week are you available to work? ")
phoneNumber = input("What is your Phone Number? ")
email = input("What is your email address? ")

def check_age_for_pub():
    current_year = 2025 #get the current year
    
#input for the age or year born
age = int(input("What is your age? "))
year_born = int(input("What was the year you were born (eg. 2009)? "))

department = input("What department (pub, kitchen, floor) do you wish to work in? ")


#application form header
print("\n")
print("#########################################")
print("#           The King's Arms Pub         #")
print("#             Toronto, Ontario          #")
print("#########################################")
print("\n")

#prints information
print("Open Monday-Sunday") #hard coded
print("Applicant's name: ", nameFirst, nameLast)
print("Availability ", workAvailable)
print("Phone Number: ", phoneNumber)
print("Email: ", email)
print("Department: ", department)

#check if the age is above 18
if age > 18:
        color.write("You are above the age to work at The King's Arms.\n","STRING")
else:
        color.write("You are not above the age to work at The King's Arms.\n","COMMENT")

#run the function
check_age_for_pub()
