#!/usr/bin/env python3

from turtle import *

screen_width, screen_height = screensize()

scale = 1
columns = 50 // 1
rows = 25 // 1

bgcolor("black")
# speed(0)
# tracer(24,10)
tracer(0,0)
hideturtle()
pu()
pensize(2)

goto(-960,-510)
pd()
# showturtle()
left(90)

for col in range(50):
    for row in range(rows):
        ch = (row + 1)/25
        fill_color = (ch/3 + ((row/rows)/1.6), ch/2 + 0.2, 0.7)
        stroke_color = (ch/3 + ((row/rows)/1.6),ch/2 + 0.21, 0.8)
        color(stroke_color, fill_color)
        begin_fill()
        for arrow in range(3):
            pendown()
            forward(25 * scale)
            left(120)
            forward(10 * scale)
            right(60)
            forward(10 * scale)
            right(120)
            forward(25 * scale)
            right(60)
            forward(25 * scale)
            right(120)
            forward(10 * scale)
            right(60)
            forward(10 * scale)
            left(120)
            forward(25 * scale)
            left(60)

        end_fill()
        penup()
        forward(45 * scale)
    if col % 2 == 0:
        reverse = rows + 1
    else:
        reverse = rows

    backward(45 * scale * reverse)
    right(60)
    forward(45 * scale)
    left(60)


done()
