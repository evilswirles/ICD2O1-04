import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
t.pendown() #puts down pen, first box
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)

t.penup() #picks up the pen
t.back(150)
t.right(90)
t.back(70)
t.right(90)

t.pendown() #puts down pen, second box
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(70)

t.penup() #picks up pen, finished box, starting Double Triangle
t.back(390)

t.pendown() #puts down pen for Double Triangle
t.forward(100)
t.left(95)


#last line of code
wn.exitonclick()
