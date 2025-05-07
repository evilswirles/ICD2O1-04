nameFirst = input("What is your first name? ")
nameLast = input("What is your last name? ")
workAvailable = input("How many days are you available (eg. Monday, Friday)? ")
phoneNumber = int(input("What is your phone number in case we need to contact you? "))
email = input("What is your email in case we need to contact you? ")

#check age
legalAge = int(input("What is your legal age? "))
yearBorn = int(input("What was the year you were born? "))


#application form header
print("\n")
print("#########################################")
print("#           The King's Arms Pub         #")
print("#             Toronto, Ontario          #")
print("#########################################")
print("\n")

#printing the output, client side
print("Your name is ", nameFirst, nameLast)
print("Hourly pay is: 17.20/hour")

print("You were born on:", yearBorn)
#checking to see if the applicant is old enough to work
if (legalAge >= 18): #if the applicant is over or is 18
    print("You are old enough to work here")

elif (legalAge <= 17): #else if the applicant is under or is 17
    print("You are not old enough to work here")

else: #else the age inputed is not a valid number (age), then try again
    print("Try again")

#prints everything that was inputed above
print("You are available to work ", workAvailable)
print("Your phone number is ", phoneNumber)
print("Your email is ", email)




















