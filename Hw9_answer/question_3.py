import turtle




N = int(input("input the numeber of triangle : "))
x_init = -300
y_init = -300
side_length = 50
turtle.screensize(400, 400)
turtle.speed(15)

#draw bottom tri
bottom_tri_num = N//2 + N%2
for i in range(bottom_tri_num):
    turtle.penup()
    turtle.goto(x_init+side_length*i, y_init)
    turtle.setheading(60)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(300)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(side_length)
# draw upper tri
upper_tri_num = N//2
x_init = x_init + side_length/2
y_init = y_init + (side_length/2*(3**0.5))
for i in range(upper_tri_num):
    turtle.penup()
    turtle.goto(x_init+side_length*i, y_init)
    turtle.setheading(300)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(60)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(side_length)

turtle.hideturtle()
turtle.mainloop()
