#!/usr/bin/env python3

from turtle import *

screen_width, screen_height = screensize()
scale = 1.2
columns = int(20 // scale)
rows = int(20 // scale) - 1

red_factor = 0.2
green_factor = 0.4
blue_factor = 0.5

bgcolor("black")
hideturtle()
pensize(2)
pd()
left(90)
tracer(12,0)
goto(screen_width,-screen_height)
stroke_color = "black"

for row in range(rows):
    for column in range(columns if row % 2 == 0 else columns -1 ):
        for diamond in range(3):
            diamond = ((diamond + 2) % 3) + 1
            red = min(1, red_factor * diamond + (column / 100))
            green = min(1, (green_factor * diamond + (column / 50)))
            blue = min(1, (blue_factor * diamond + (row / 100)))
            print(f"r: {red}")
            print(f"g: {green}")
            print(f"b: {blue}")
            color(stroke_color, (red, green, blue))
            begin_fill()
            left(60)
            forward(25 * scale)
            right(120)
            forward(25 * scale)
            right(60)
            forward(25 * scale)
            right(120)
            forward(25 * scale)
            end_fill()
        pu()
        left(60)
        forward(25 * scale)
        left(60)
        forward(25 * scale)
        right(120)
        pd()
    pu()

    right(60)
    for step_back in range(columns - 1):
        right(60)
        forward(25 * scale)
        left(60)
        forward(25 * scale)
    left(60)
    forward(25 * scale)
    right(60)
    forward(25 * scale)
    left(60)
    pd()

done()
