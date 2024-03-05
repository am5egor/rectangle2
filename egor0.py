from turtle import *


def cube(x,y, border_color, colour, h, v):
    penup()
    goto(x,y)
    pendown()
    color(border_color, colour)
    begin_fill()
    for i in range(2):
        forward(h)
        left(90)
        forward(v)
        left(90)
    end_fill()

cube(0,0, 'black', 'red', 20, 80)

hideturtle()
exitonclick()

