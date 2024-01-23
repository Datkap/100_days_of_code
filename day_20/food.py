from turtle import Turtle
from random import randint, choice


class Food:
    def __init__(self):
        self.food = Turtle(shape="square")
        self.food.resizemode("user")
        self.food.shapesize(0.25, 0.25, 3)
        self.food.penup()
        self.food.color('red')
        self.food_position = self.food.pos()

    def spawn(self, board_width, board_height):
        x_position_min, x_position_max = int((board_width / 2) * (-1)), int(board_width / 2)
        y_position_min, y_position_max = int((board_height / 2) * (-1)), int(board_height / 2)
        x_position, y_position = randint(x_position_min, x_position_max), randint(y_position_min, y_position_max)
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'cyan']
        self.food.color(choice(colors))
        self.food.goto(x=x_position, y=y_position)
        self.food_position = self.food.pos()