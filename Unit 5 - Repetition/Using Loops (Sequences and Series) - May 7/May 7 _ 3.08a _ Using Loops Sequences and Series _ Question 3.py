###QUESTION 3###
#user input
f = float(input("Enter the first term: "))
last_term = float(input("Enter the last term: "))
step_value = float(input("Enter the step value: ")) #d

sum = 0 #the sum is set at zero
term = first_term

#adjust the step direction based on first and last
if (f > last_term) and (step_value > 0):
    step_value = -step_value #-d
elif (last_term > f) and (step_value < 0):
    step_value = -step_value #-d

#loop through the sequence and add terms
if (step_value > 0):
    while term <= last_term:
        sum += term
        term += step_value
else:
    while term >= last_term:
        sum += term
        term += step_value

#output
print("The arithmetic sequence's sum is:", sum)
