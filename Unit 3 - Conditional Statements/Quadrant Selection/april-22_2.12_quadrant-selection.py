x = int(input("What is your value for x? ")) #x value
y = int(input("What is your value for y? ")) #y value


if (x > 0) and (y > 0):
    print("You are in Quadrant 1")

elif (x < 0) and (y > 0):
    print("You are in Quadrant 2")

elif (x < 0) and (y < 0):
    print("You are in Quadrant 3")

elif (x > 0) and (y < 0):
    print("You are in Quadrant 4")

else:
    print("Unknown value, please try again.")



#if (x == 0) and (y == 0):
    #print("origin")
#elif (x == 0):
    #print("y axis")
#elif (y == 0):
    #print("x axis")
