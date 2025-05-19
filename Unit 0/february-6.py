import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
t.speed(8) #speed the turtle is going

t.pendown() #start of rectangle
t.forward(300)
t.right(90)
t.forward(150)
t.right(90)
t.forward(300)
t.right(90)
t.forward(150)

t.penup() #end of rectangle
t.forward(150)

t.fillcolor("#008000") #fill for square

t.begin_fill()

t.pencolor("red")

t.pendown() #start of square
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)

t.end_fill() #end fill for square

t.penup()
t.pencolor("#000000")
t.forward(200)

t.fillcolor("#D1E5F4") #fill for my own shape (light blue)

t.begin_fill()

t.pendown() #start of my own shape
t.forward (100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(40) #
t.left(90)
t.forward(140) #

t.end_fill() #end fill for my own shape (light blue)

t.penup() #end of own shape
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(330)

t.pendown()
t.forward(150)
t.left(145)
t.forward(75)
t.right(90)
t.forward(75)
t.left(125)
t.forward(145)
t.left(145)
t.forward(75)
t.right(90)
t.forward(75)

t.penup()
t.forward(90)
t.left(215)


#last line of code
wn.exitonclick()
