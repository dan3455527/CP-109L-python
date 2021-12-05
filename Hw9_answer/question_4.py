import turtle



N = 15
rotate_degree = 10
side_length = 100
turtle.speed(15)
# draw square
for i in range(N):
    turtle.setheading(rotate_degree*i)
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(rotate_degree*i+90)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(rotate_degree*i+180)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.penup()
    turtle.setheading(rotate_degree*i+270)
    turtle.pendown()
    turtle.forward(side_length)

turtle.mainloop()
