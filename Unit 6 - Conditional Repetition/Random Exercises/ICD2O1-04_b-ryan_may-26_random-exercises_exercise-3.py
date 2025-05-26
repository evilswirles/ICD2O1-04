###EXERCISE 3###
import random

text = input("Please enter a word (ex. Hello World): ")
index = random.randrange(0, len(text))
character = text[index]

print("Random character:", character)
