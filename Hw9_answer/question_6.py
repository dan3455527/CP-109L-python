import turtle
import math

t=turtle.Turtle()

t.speed(15)
t.pencolor('red')
t.fillcolor("red")


t.begin_fill()
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.penup()
t.end_fill()

t.pencolor('blue')
t.fillcolor("blue")

t.goto(0,100)
t.pendown()
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()



R=18.75

t.pencolor('white')
t.fillcolor("white")

t.goto(75,150)
t.left(180)
t.pendown()
t.forward(2*R)
t.right(165)
t.forward(4*R*math.cos(math.pi*15/180))

t.begin_fill()
for i in range(11):
    t.right(150)
    t.forward(4*R*math.cos(math.pi*15/180))

t.penup()
t.end_fill()


t.pencolor('blue')
t.fillcolor("blue")


t.setheading(270)
t.goto(75-R/15*17,150)
t.begin_fill()
t.circle(R/15*17)
t.end_fill()

t.pencolor('white')
t.fillcolor("white")

t.setheading(270)
t.goto(75-R,150)
t.begin_fill()
t.circle(R)
t.end_fill()

t.hideturtle()
turtle.mainloop()