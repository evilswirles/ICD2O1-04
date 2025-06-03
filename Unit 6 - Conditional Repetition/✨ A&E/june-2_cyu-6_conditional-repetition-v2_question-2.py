###QUESTION 2###
#intializes all to 0
letterA = 0
letterE = 0
letterI = 0
letterO = 0
letterU = 0
letterY = 0

#user input
character = input("Please enter a character. Type \"Quit\" to exit the program: ")

#while loop
while character != "Quit":
    #check for each vowel (both lowercase and uppercase)
    if character == "a" or character == "A":
        letterA = letterA + 1
    elif character == "e" or character == "E":
        letterE = letterE + 1
    elif character == "i" or character == "I":
        letterI = letterI + 1
    elif character == "o" or character == "O":
        letterO = letterO + 1
    elif character == "u" or character == "U":
        letterU = letterU + 1
    elif character == "y" or character == "Y":
        letterY = letterY + 1

    #asks for user input again
    character = input("Please enter a character. Type \"Quit\" to exit the program: ")

print("Count of each vowel:")
print("A:", letterA)
print("E:", letterE)
print("I:", letterI)
print("O:", letterO)
print("U:", letterU)
print("Y:", letterY)
