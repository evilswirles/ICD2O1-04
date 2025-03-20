import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#F5DEB3")  #changes the background colour

t.fillcolor("#7B3F00") #tree trunk

t.begin_fill()

t.pendown()
t.forward(50)
t.left(90)
t.forward(90)
t.left(90)
t.forward(50)
t.left(90)
t.forward(90)

t.end_fill()

t.penup()
t.back(90)
t.right(90)

t.fillcolor("#5bb450") #tree

t.begin_fill()

t.pendown()
t.forward(60)
t.right(120)
t.forward(150)
t.right(120)
t.forward(150)

t.right(120)
t.forward(70)

t.end_fill()


t.penup() #end of Tree
t.forward(200)


t.left(90)
t.forward(200)

t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

#last line of code
wn.exitonclick()
