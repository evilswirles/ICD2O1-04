###QUESTION 1###
#user input
first_input = input("Please enter the first word or phrase: ")
second_input = input("Please enter the second word or phrase: ")

#remove spaces and convert to lowercase
first_input_cleaned = first_input.replace(" ", "").lower()
second_input_cleaned = second_input.replace(" ", "").lower()

#sort the characters and compare
if sorted(first_input_cleaned) == sorted(second_input_cleaned):
    print(f'"{first_input}" and "{second_input}" are anagrams.')
else:
    print(f'"{first_input}" and "{second_input}" are NOT anagrams.')
