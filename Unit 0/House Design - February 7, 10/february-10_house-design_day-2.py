import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#b3ebf2")  #changes the background colour
t.speed(12) #speed of the turtle

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

t.fillcolor("#ffde21") #fill for the roof

t.begin_fill()

t.pendown() #garage windows 1
t.forward(55) #
t.left(90)
t.forward(15)
t.left(90)
t.forward(55) #
t.left(90)
t.forward(15)
t.end_fill()

t.penup()
t.left(90)
t.forward(55)
t.forward(40) #space between

t.fillcolor("#ffde21") #fill for the roof

t.begin_fill()

t.pendown() #garage windows 2
t.forward(55)
t.left(90)
t.forward(15)
t.left(90)
t.forward(55)
t.left(90)
t.forward(15)
t.end_fill()


t.penup()
t.forward(15)

t.fillcolor("#AF8055") #fill for the roof

t.begin_fill()

t.pendown()
t.left(90)
t.forward(65)
t.right(90)
t.forward(60)
t.right(109) #
t.forward(198)
t.end_fill() #end fill for the roof

t.penup()
t.forward(50)
t.right(160)
t.forward(350)
t.left(90)
t.forward(20)

t.pendown() #door
t.forward(53)
t.right(90)
t.forward(30)
t.right(90)
t.forward(53)
t.right(90)
t.forward(30)

t.penup()
t.forward(40)

t.pendown() #window of house #2
t.forward(35)
t.right(90)
t.forward(30)
t.right(90)
t.forward(35)
t.right(90)
t.forward(30) #end of window #2

t.penup()
t.left(90)
t.forward(105)
t.left(90)

t.pendown() #window of house #1
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30) #end of window #1

t.penup()
t.left(90)
t.forward(150)
t.left(90)
t.forward(67)
t.right(140) #

t.fillcolor("#808080") #fill for the roof

t.begin_fill()

t.pendown() #roof
t.forward(150)
t.right(77) #
t.forward(170)
t.end_fill()

t.penup()

#last line of code
wn.exitonclick()
