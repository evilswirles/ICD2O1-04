###QUESTION 2###
#user input
numbers_input = input("Enter your number (integer) by spaces: ")

#convert into a list of integers
numbers = list(map(int, numbers_input.split()))

#new list with values that occur only once
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

#count how many unique numbers are between 10 and 20
count_between_10_and_20 = 0
for num in unique_numbers:
    if (10 <= num <= 20):
        count_between_10_and_20 += 1

#output, printed
print("List after removing duplicates:", unique_numbers)
print("Count of values between 10 and 20:", count_between_10_and_20)
