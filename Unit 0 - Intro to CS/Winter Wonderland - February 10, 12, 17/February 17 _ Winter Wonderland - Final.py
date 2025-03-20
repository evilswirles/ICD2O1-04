import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#191970")  #changes the background colour
t.pencolor("white") #colour of the pen
t.speed(10) #speed of the turtle


t.pencolor("yellow") #colour of the pen
def snowflake_1(): #snowflake 1
    t.right(60)
    t.forward(100)
    t.penup()
    t.back(100)
    t.pendown()


i = 0
while i < 6:
    snowflake_1()
    i += 1

t.penup()
t.forward(150)
t.pendown()

t.pencolor("grey") #colour of the pen
t.forward(60) #snowflake 1 continued
t.back(30)
t.right(90)
t.forward(30)
t.back(60)
t.forward(30)
t.right(30)
t.forward(30)
t.back(60)
t.forward(30)
t.right(30)

t.penup()

t.right(70)
t.forward(30)
t.back(60)
t.forward(30)
t.left(40)
t.forward(370)
t.right(90)

t.pendown() #snowflake 2
t.pencolor("orange") #colour of the pen
t.forward(100)
t.back(50)
t.left(90)
t.forward(60)
t.back(55)
t.back(60)
t.forward(55)
t.right(50)
t.forward(55)
t.back(55)
t.back(55)

t.penup()
t.forward(230)
t.right(40)

t.pencolor("red") #colour of the pen
t.pendown() #snowflake 3
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.left(50)
t.forward(40)

t.penup() #continued 3
t.back(80)

t.pendown()
t.back(40)
t.forward(40)
t.right(50)
t.forward(10) #
t.left(90)

t.penup()
t.forward(30)

t.pendown()
t.forward(40)
t.back(40)

t.penup()
t.back(30)

t.pendown()
t.back(40)
t.forward(40)
t.right(90)
t.forward(16)
t.right(50)
t.forward(40)
t.back(40)

t.penup()
t.back(40)

t.pendown()
t.back(40) #end of snowflake 3

t.penup()
t.right(40)
t.forward(200)

t.pendown() #snowflake 5
t.pencolor("green") #colour of the pen
t.forward(30)
t.back(15)
t.right(90)
t.forward(20)
t.back(20)
t.back(20)
t.forward(20)
t.right(30)
t.forward(30)
t.back(30)
t.back(30)
t.forward(30)
t.left(30)
t.left(30)
t.forward(30)
t.back(30)
t.back(30)

#last line of code
wn.exitonclick()
