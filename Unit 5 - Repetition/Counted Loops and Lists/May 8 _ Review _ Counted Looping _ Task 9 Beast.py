###TASK 9 - BEAST###
scores = []

for i in range(10):
    score = float(input(f"Enter score #{i + 1}: ")) #asks for user to input score
    scores.append(score) #appends the score to add the user input

print("Scores entered:", scores)
