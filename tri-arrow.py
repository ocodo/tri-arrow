#!/usr/bin/env python3

from turtle import *

scale = 1
tracer(24,200)
speed(0)
hideturtle()

penup()
left(90)
backward(45 * 11)
left(90)
forward(45 * 11)
right(90)

for a in range(26):
    for b in range(24):
        ch = (b + 1)/25
        color('black', (ch/3 + ((a/24)/1.6), ch/2 + 0.2, 0.7))
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
        reverse = 25
    else:
        reverse = 24

    backward(45 * scale * reverse)
    right(60)
    forward(45 * scale)
    left(60)


done()
