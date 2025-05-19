import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
t.speed(8) #speed of the turtle

t.penup()
t.back(200)

t.fillcolor("#E06350") #fill for body of the house

t.begin_fill()

t.pendown() #body of house
t.pensize(4) #outline of the body of the house
t.forward(250)
t.left(90)
t.forward(200)
t.left(90)
t.forward(250)
t.left(90)
t.forward(200)

t.end_fill() #end fill for the body of the house

t.penup()
t.left(90)
t.forward(250)

t.fillcolor("#B593E1") #fill for body of the garage

t.begin_fill()

t.pendown() #body of garage
t.pensize(1) #outline of the body of the garage
t.forward(180)
t.left(90)
t.forward(100)
t.left(90)
t.forward(180)

t.end_fill() #end fill for the body of the garage

t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(180)
t.left(90)
t.forward(85)
t.left(90)
t.forward(20)

t.pendown() #garage windows 1
t.forward(55) #
t.left(90)
t.forward(15)
t.left(90)
t.forward(55) #
t.left(90)
t.forward(15)

t.penup()
t.left(90)
t.forward(55)
t.forward(40) #space between

t.pendown() #garage windows 2
t.forward(55)
t.left(90)
t.forward(15)
t.left(90)
t.forward(55)
t.left(90)
t.forward(15)

#last line of code
wn.exitonclick()
