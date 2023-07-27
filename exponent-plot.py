#!/usr/bin/env python3

import turtle
import math

def main(pen_color = (1, 1/2, 0), bg_color = "black"):
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
        turtle.forward(10)
        turtle.pencolor(pen_color)

    # Set up the turtle
    turtle.hideturtle()
    turtle.tracer(20,0)
    turtle.bgcolor(bg_color)
    turtle.pencolor(pen_color)

    scale = 20

    grid = range(-30, 30)

    # Draw X and Y axis
    for point in grid:
        draw_point(0, point * 20)
        draw_point(point * scale, 0)

    # Y = X²
    for x in grid:
        y = x * x
        draw_tack(x * scale, y * 2, 'cyan')

    # Y = X³
    for x in grid:
        y = x * x * x
        draw_tack(x * scale, y * 0.5, 'red')

    turtle.done()

main()
