from turtle import Turtle, Screen
from day_20.snake import Snake
from day_20.food import Food


def compare_tuples(tuple_1, tuple_2, tolerance=5):
    return abs(tuple_1[0] - tuple_2[0]) <= tolerance and abs(tuple_1[1] - tuple_2[1]) <= tolerance


width = 600
height = 600

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(False)

snake = Snake()
food = Food()
screen.update()
game_on = True
food.spawn(board_width=width, board_height=height)

counter = 0
while game_on:
    counter += 1
    screen.listen()
    screen.onkey(fun=snake.turn_up, key="w")
    screen.onkey(fun=snake.turn_down, key="s")
    screen.onkey(fun=snake.turn_left, key="a")
    screen.onkey(fun=snake.turn_right, key="d")
    snake.move(5)
    if compare_tuples(snake.snake_head.pos(), food.food_position, 10):
        print("You got the food!")
        snake.grow()
        food.spawn(board_width=width-50, board_height=height-50)
        print(snake.snake_size)
    screen.update()

screen.exitonclick()

