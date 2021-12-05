import turtle


n = 30
x = -300
y = -300

turtle.speed(15)

turtle.screensize(400, 400)
turtle.penup()
turtle.pencolor('black')

for i in range(19):
    turtle.goto(x, y + n * i)
    turtle.pendown()
    turtle.forward(18 * n)
    turtle.penup()


turtle.left(90)
for i in range(19):
    turtle.goto(x + n * i, y)
    turtle.pendown()
    turtle.forward(18 * n)
    turtle.penup()

turtle.hideturtle()
turtle.mainloop()