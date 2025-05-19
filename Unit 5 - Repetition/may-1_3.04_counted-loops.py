###QUESTIONS 1-3###
#for x in range(0, 5, 1):
    #print(x)


###QUESTION 3A###
#for x in range(0, 5, 1):
    #print("The loop has run " + str(x) + " times.")


###QUESTION 4###
#number_input = int(input("Please input a positive number (integer): ")) #asks the user to input a positive number

#if (number_input < 0): #if the inputted number is less than 0
    #print("Please input a positive number.")
#else: #if it is not a positive number
    #for i in range(number_input + 1):
        #print(i)


###QUESTION 5###
starting_number = int(input("Please input the starting number (an integer): "))
step_value = int(input("Please input the step value (a positive integer): "))
ending_number = int(input("Please input the ending number (a positive integer): "))

if (ending_number < 0) or (step_value <= 0):
    print("Please input a positive ending number and a positive step value: ")
else:
    for i in range(starting_number, ending_number + 1, step_value):
        print(i)
