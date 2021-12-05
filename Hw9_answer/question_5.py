import turtle



row = 5
x_init = -300
y_init = -300
side_length = 30
turtle.screensize(400, 400)
turtle.speed(15)

#left
left_hexagon = row//2 + row%2
for j in range(left_hexagon):
    y_init_left = y_init + side_length*j*1.5*2
    for i in range(4):
        turtle.penup()
        turtle.setheading(30)
        turtle.goto(x_init + i*(side_length*2*(3**0.5)/2), y_init_left)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(150)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(210)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(270)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(330)
        turtle.pendown()
        turtle.forward(side_length)
#right
right_hexagon = row // 2
for j in range(right_hexagon):
    y_init_right = y_init + side_length*j*2*1.5 + side_length*1.5
    for i in range(4):
        turtle.penup()
        turtle.setheading(30)
        turtle.goto(x_init + i*(side_length*(3**0.5)) + side_length*(3**0.5)/2, y_init_right)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(150)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(210)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(270)
        turtle.pendown()
        turtle.forward(side_length)
        turtle.penup()
        turtle.setheading(330)
        turtle.pendown()
        turtle.forward(side_length)

turtle.hideturtle()
turtle.mainloop()
