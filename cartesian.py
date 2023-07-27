#!/usr/bin/env python3

import turtle
import math

def main(pen_color = (1, 1/2, 0), bg_color = "black"):
    point_range = range(-extent, extent, (extent*2) // num_points)

    # Function to draw a point at a given (x, y) coordinate
    def draw_point(x, y, color=pen_color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(2, pen_color)

    # Function to draw a point at a given (x, y) coordinate
    def draw_tack(x, y, color=pen_color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.seth(90)
        turtle.pencolor(color)
        turtle.forward(30)
        turtle.pencolor(pen_color)

    # Set up the turtle
    turtle.hideturtle()
    turtle.tracer(10,0)
    turtle.bgcolor(bg_color)
    turtle.pencolor(pen_color)

    # Draw X and Y axis
    for point in point_range:
        draw_point(0, point)
        draw_point(point, 0)

    turtle.done()

main(extent=450, amplitude=70)
