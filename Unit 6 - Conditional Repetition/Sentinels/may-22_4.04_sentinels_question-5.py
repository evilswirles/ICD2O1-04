###QUESTION 5###
num = int(input("Enter a number: "))

message = "Enter a word (\"done\" to stop): "
word = input(message)

while (word != "done"):
    for i in range(num):
        print(word, end=" ")
    print("\n")
    word = input(message)

print("\nGoodbye!")
