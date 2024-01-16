from turtle import Turtle, Screen
import random

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'cyan']
screen = Screen()
height = 500
width = 500
screen.setup(width=width, height=height)
number_of_turtles = int(screen.numinput(title="Number of turtles", prompt="How many turtles are going to participate "
                                                                          "in the race?", minval=2, maxval=10))
playing_turtles_colors = random.sample(colors, number_of_turtles)
user_bet = ''
while user_bet not in colors:
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
finishing_x_position = width / 2 - 25
spacing = 40
total_vertical_space = height - spacing * (len(playing_turtles) - 1)
top_space = total_vertical_space / 2

for i in range(len(playing_turtles.keys())):
    starting_y_position = -(height / 2) + top_space + i * spacing
    playing_turtles[list(playing_turtles.keys())[i]].goto(x=starting_x_position, y=starting_y_position)

turtle_won = False

while not turtle_won:
    turtles_move_order = list(playing_turtles)
    random.shuffle(turtles_move_order)
    for turtle in playing_turtles:
        moving_distance = random.randint(1, 10)
        playing_turtles[turtle].forward(moving_distance)
        if playing_turtles[turtle].xcor() >= finishing_x_position:
            print(f"{turtle.capitalize()} won the race!")
            if turtle == user_bet:
                print("Your bet was correct!")
            else:
                print("Unfortunately you didn't guess it...")
            turtle_won = True

screen.exitonclick()
