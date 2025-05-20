###TASK 3 - PRO###
#START
#any other password inputted is invalid
password = "ilovepython"
guess = ""

while (guess != password):
    print("Please enter the password.")
    guess = input(">>> ")

    if (guess != password):
        print("Access denied! Please try again.")

print("Password accepted. Welcome back user!")
#END WHILE
#END
