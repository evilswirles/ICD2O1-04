###QUESTION 1A###
l = ["*","*","*","*","*"]

print("length:", len(l))

l[2] = "5"

print("third:", l[2])
print("last:", l[-1])


###QUESTION 1B###
l = ["*","*","*","*","*"]

l[0] = "7"
l[4] = "dog"

print(l)


###QUESTION 1C###
word = ["m","i","n","e","c","r","a","f","t"]

print(word[0:4])  # ['m', 'i', 'n', 'e']
print(word[4:8])  # ['c', 'r', 'a', 'f']

str1 = "Minecraft"
print(str1[0:10])


###QUESTION 1D###
zero_list = [0] * 7
one_list = [1] * 6

print(zero_list + one_list)
print(zero_list * 3)
print(one_list + zero_list)
print(zero_list + [2, 2, 2])
