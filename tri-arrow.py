#!/usr/bin/env python3

from turtle import *

columns = 26
rows = 24

scale = 1.8
tracer(0,0)
speed(0)
hideturtle()
pensize(2)

penup()
left(90)
backward(45 * 11)
left(90)
forward(45 * 11)
right(90)

for a in range(columns):
    for b in range(rows):
        ch = (b + 1)/25
        fill_color = (ch/3 + ((a/columns)/1.6), ch/2 + 0.2, 0.7)
        stroke_color = (ch/3 + ((a/columns)/1.6),ch/2 + 0.21, 0.8)
        color(stroke_color, fill_color)
        begin_fill()
        for c in range(3):
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
    if a % 2 == 0:
        reverse = columns - 1
    else:
        reverse = columns - 2

    backward(45 * scale * reverse)
    right(60)
    forward(45 * scale)
    left(60)


done()
