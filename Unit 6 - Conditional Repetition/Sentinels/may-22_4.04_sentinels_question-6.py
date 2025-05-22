###QUESTION 6###
num = int(input("Enter a number: "))
stop = input("Enter a word to stop the program: ")

message = f"Enter a word (\"{stop}\" to stop): "
word = input(message)

while (word != stop):
    for i in range(num):
        print(word, end=" ")
    print("\n")
    word = input(message)

print("\nGoodbye!")
