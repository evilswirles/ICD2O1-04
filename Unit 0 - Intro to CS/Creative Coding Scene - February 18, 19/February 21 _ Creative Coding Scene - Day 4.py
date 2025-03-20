import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()
sun = turtle.Turtle()
flag = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#ADD8E6")  #changes the background colour
t.speed(10) #speed of the turtle turtle
sun.speed(10) #speed of the sun turtle
flag.speed(10) #speed of the flag turtle

t.penup()
t.right(90) #start of green grass
t.forward(200)
t.right(90)

t.fillcolor("#5bb450") #tree
t.begin_fill()
t.pencolor("green")
t.pendown() #pendown for drawing of grass
t.forward(370)
t.back(715)
t.right(90) #rotates 3 times ("t.right(90)" x3)
t.right(90)
t.right(90)
t.forward(125)
t.right(90)
t.forward(700) # longs
t.right(90)
t.forward(125)
t.end_fill() #end fill for grass

t.pencolor("black")
t.penup()
t.right(90)
t.forward(120)
t.left(90)

t.pendown() #start of cottage house
t.fillcolor("#B39B84") #door frame fill
t.begin_fill() #cottage front fill
t.pencolor("#C38560")
t.forward(200)
t.right(90)
t.forward(260) #
t.right(90)
t.forward(200)
t.end_fill() #cottage front fill

t.pencolor("green")
t.right(90)
t.forward(260)
t.right(90)
t.right(90)
t.forward(110)
t.left(90)

t.fillcolor("#B39B84") #door frame fill
t.begin_fill()
t.pencolor("black") #door frame
t.forward(55)
t.right(90)
t.forward(40)
t.right(90)
t.forward(55)
t.back(27.5)
t.right(90)
t.end_fill() #end of door frame fill

t.penup() #doorknob
t.forward(12)
t.pendown() #start of circle of doorknob
t.circle(3) # doorknob

t.penup()
t.forward(137)
t.left(90)
t.forward(10)
t.left(90)
t.left(90)
t.forward(183)
t.right(90)

t.pendown() #chimney
t.pencolor("#C38560")
t.forward(50)
t.left(90)

t.pencolor("#3d2814")
t.forward(70)
t.right(90)
t.forward(30)
t.right(90)
t.forward(70)

t.right(90) #TODO
t.pencolor("#B39B84") #TODO
t.forward(30)
t.right(90)
t.pencolor("black")
t.pencolor("red") #start of chimney bricks, red
t.forward(15)
t.forward(55) 
t.right(90)
t.forward(30)
t.right(90)
t.forward(10) #turns
t.right(90)
t.forward(30) #brick forward
t.left(90)
t.forward(10)
t.left(90)
t.forward(30)
t.right(90)
t.back(10)
t.forward(10)
t.forward(10)
t.right(90)
t.forward(30)
t.left(90)
t.forward(10)
t.left(90)
t.forward(30)
t.right(90)
t.back(10)
t.forward(10)
t.forward(10)
t.right(90)
t.forward(30)
t.left(90)
t.forward(10)
t.left(90)
t.forward(30)
t.right(90)
t.back(10)
t.forward(10)
t.forward(10) #end of chimney

t.penup()
t.forward(100)
t.right(90)
t.forward(30)
t.left(90)
t.forward(50)

t.pendown() #start of cottage window pane
t.pencolor("#494F55")
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.back(15)
t.left(90)
t.forward(30)
t.back(15)
t.right(90)
t.forward(15)
t.back(15)
t.back(15)

t.penup()
t.left(90)
t.back(15)
t.left(90)

t.penup()
t.forward(140)

t.pendown() #second window pane
t.back(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.back(15)
t.left(90)
t.forward(30)
t.back(15)
t.right(90)
t.back(15)
t.forward(15)
t.forward(15)
t.penup() #end of second window pane

t.home()
t.penup()
t.forward(70)

flag.penup() #flag with polygon
flag.forward(70)
flag.right(90)
flag.forward(200)
flag.right(90)
flag.pendown() #start of flag with polygon
flag.pencolor("#FFC0CB") #flag pole for polygon flag, pink

flag.fillcolor("#FFC0CB") #begin fill for flag pole, pink
flag.begin_fill()
flag.forward(15)
flag.right(90)
flag.forward(300)
flag.right(90)
flag.forward(15)
flag.right(90)
flag.forward(300)
flag.back(300)
flag.left(90)

flag.end_fill() 


# flag.pencolor("red") #TODO PEN-COLOUR




sun.penup() #yellow sun
sun.forward(365)
sun.left(90)
sun.forward(300)

sun.pencolor("yellow") #yellow sun pen colour
sun.fillcolor("#FFFF00") #yellow sun fill
sun.begin_fill()
sun.pendown() #start of yellow sun
sun.circle(50)
sun.end_fill() #end of yellow sun fill
sun.right(90)
sun.right(90)
sun.right(90)


#last line of code
wn.exitonclick()
