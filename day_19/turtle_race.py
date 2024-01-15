from turtle import Turtle, Screen
import random

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'cyan']
screen = Screen()
height = 400
width = 500
screen.setup(width=width, height=height)
number_of_turtles = int(screen.numinput(title="Number of turtles", prompt="How many turtles are going to participate in"
                                                                      " the race?", minval=2, maxval=10))
playing_turtles_colors = random.sample(colors, number_of_turtles)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? You can select"
                                  f" from: {', '.join(playing_turtles_colors)}.")
# Create playing turtles
playing_turtles = {}
for turtle_color in playing_turtles_colors:
    current_turtle = Turtle(shape="turtle")
    current_turtle.color(turtle_color)
    current_turtle.penup()
    playing_turtles[turtle_color] = current_turtle

# Define game board parameters
starting_x_position = (width / 2 - 20) * -1
finishing_x_position = width / 2 - 10
spacing = 40
total_vertical_space = height - spacing * (len(playing_turtles) - 1)
top_space = total_vertical_space / 2
y_coordinates = [-(height / 2) + top_space + i * spacing for i in range(len(playing_turtles))]
turtle_positions = {}


# Move turtles to srtating position
for turtle in playing_turtles.keys():
    playing_turtles[turtle].goto(x=starting_x_position, y=y_coordinates[list(playing_turtles.keys()).index(turtle)])
    turtle_positions[turtle] = playing_turtles[turtle].pos()

print(turtle_positions)

screen.exitonclick()

