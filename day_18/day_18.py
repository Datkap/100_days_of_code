from turtle import Turtle, Screen
from random import random, choice

# Turtle characteristics
turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")

# Challenge 1 - draw a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# Challenge 2 - draw a dashed line
# for _ in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Challenge 3 - draw different shapes
# for edges in range(3, 10):
#     turtle.color(random(), random(), random())
#     turn_angle = 360 / edges
#     for _ in range(edges):
#         turtle.forward(100)
#         turtle.right(turn_angle)

# Challenge 4 - random walk
# def random_walk(num_of_steps):
#     available_directions = [0, 90, 180, 270]
#     turtle.speed(10)
#     size = 1
#     for step in range(num_of_steps):
#         turtle.pensize(size)
#         turtle.color(random(), random(), random())
#         direction = choice(available_directions)
#         turtle.seth(direction)
#         turtle.forward(30)
#         size += 0.1
#
#
# random_walk(200)

# Challenge 5 - Spriograph
# def draw_spirograph(num_of_circles):
#     turtle.speed(0)
#     turn_angle = 360 / num_of_circles
#     for circle in range(num_of_circles):
#         turtle.color(random(), random(), random())
#         turtle.circle(100)
#         turtle.right(turn_angle)
#
#
# draw_spirograph(2)

# Utils
screen = Screen()
screen.exitonclick()
