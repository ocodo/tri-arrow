#!/usr/bin/env python3

from turtle import *

scale = 1
speed(0)
hideturtle()
color('black', 'white')
begin_fill()
penup()
backward(45 * 11)
left(90)
forward(45 * 9)
right(90)

for _ in range(24):
    for _ in range(24):
        for _ in range(3):
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

        penup()
        forward(45 * scale)
    backward(45 * scale * 24)
    right(60)
    forward(45 * scale)
    left(60)

end_fill()
done()
