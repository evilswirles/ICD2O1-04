###TASK 13 - BEAST###
#lists to store values
list1 = ['A', 'E', 'I', 'O', 'U']

#user input
name = input("What is your name? ")

vowels = 0

for letter in name.upper():
    if letter in list1:
        vowels += 1

#output
print("Hello", name + ", you have", list1, "vowel(s) in your name!")
