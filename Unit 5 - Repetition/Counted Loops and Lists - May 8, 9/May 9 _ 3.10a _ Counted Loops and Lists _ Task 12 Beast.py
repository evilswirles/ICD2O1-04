###TASK 12 - BEAST###
#user input
password = input("Please enter your password: ")
upper = 0

for i in range(0, len(password)):
    if 'A' <= password[i] <= 'Z':
        upper += 1

#password has to have more than one uppercase letter
if (upper > 1):
    print("Password accepted")

#if the password does not have more than one uppercase letter, it will be denied
else:
    print("Password denied")
