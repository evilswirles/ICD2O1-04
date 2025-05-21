###QUESTION 2###
sumOfSquares = 0

message = "Enter an integer (negative to stop): "
num = int(input(message))

while (num >= 0):
    sumOfSquares += num * num
    num = int(input(message))

print("Sum of squares:", sumOfSquares)
