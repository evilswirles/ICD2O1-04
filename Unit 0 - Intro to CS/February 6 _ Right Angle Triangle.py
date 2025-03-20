import turtle
import math
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
a = 200
b = 200
c = math.sqrt(math.pow(a, 2)+math.pow(b,2))

t.pendown()
t.forward(200)
t.right(90)
t.forward(200)
t.right(135)
t.forward(282)

t.penup()
t.forward(50)

#last line of code
wn.exitonclick()
