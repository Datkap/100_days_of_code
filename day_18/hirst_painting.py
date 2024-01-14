import colorgram
from turtle import Turtle, Screen, colormode
from random import random, choice

# Collect sample colors
colors = colorgram.extract('day_18/hirst.jpg', 30)
filtered_colors = []
for color in colors:
    color_settings = color.rgb
    if color_settings.r <= 250 and color_settings.b <= 250 and color_settings.g <= 250:
        filtered_colors.append(color_settings)

color_base = []
for color in filtered_colors:
    r = color.r
    g = color.g
    b = color.b
    color_base.append((r, g, b))


# Define functions for the painting
def move_to_next_row(num_of_dots_each_side, dot_size, spacing):
    turtle.penup()
    turtle.right(180)
    row_length = ((num_of_dots_each_side) * dot_size) + ((num_of_dots_each_side) * spacing)
    turtle.forward(row_length)
    turtle.right(90)
    turtle.forward(dot_size + spacing)
    turtle.right(90)


def set_starting_pos(move_distance, num_of_dots_each_side):
    turtle.penup()
    turtle.seth(270)
    turtle.forward(move_distance*num_of_dots_each_side/2)
    turtle.seth(180)
    turtle.forward(move_distance*num_of_dots_each_side/2)
    turtle.pendown()
    turtle.seth(0)


def draw_hirst_painting(num_of_dots_each_side, dot_size, spacing, color_base):
    move_distance = dot_size + spacing
    set_starting_pos(move_distance, num_of_dots_each_side)
    for row in range(num_of_dots_each_side):
        for dot_in_row in range(num_of_dots_each_side):
            turtle.color(choice(color_base))
            turtle.begin_fill()
            turtle.circle(dot_size)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(move_distance)
            turtle.pendown()
        move_to_next_row(num_of_dots_each_side, dot_size, spacing)


# Paint a painting
turtle = Turtle()
colormode(255)
turtle.shape("turtle")
turtle.speed(0)
turtle.color((207, 160, 82))
draw_hirst_painting(15, 10, 20, color_base)
turtle.color('white')

screen = Screen()
screen.exitonclick()

