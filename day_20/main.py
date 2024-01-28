from turtle import Turtle, Screen
from day_20.snake import Snake
from day_20.food import Food
from day_20.scoreboard import ScoreBoard
from time import sleep


def compare_tuples(tuple_1, tuple_2, tolerance=5):
    return abs(tuple_1[0] - tuple_2[0]) <= tolerance and abs(tuple_1[1] - tuple_2[1]) <= tolerance


def game_over():
    global game_on
    game_on = False


width = 500
height = 500

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(False)

score = ScoreBoard()
snake = Snake()
food = Food()
screen.update()
game_on = True
food.spawn(board_width=width, board_height=height, snake_body=snake.snake_body)

while game_on:
    screen.listen()
    screen.onkey(fun=snake.turn_up, key="w")
    screen.onkey(fun=snake.turn_down, key="s")
    screen.onkey(fun=snake.turn_left, key="a")
    screen.onkey(fun=snake.turn_right, key="d")
    screen.onkey(fun=game_over, key="c")
    snake.move(5)

    if compare_tuples(snake.snake_head.pos(), food.food_position, 10):
        print("You got the food!")
        snake.grow()
        food.spawn(board_width=width-50, board_height=height-50, snake_body=snake.snake_body)
        score.increase_score()
        score.display_score()

    if snake.wall_hit(board_width=width, board_height=height):
        print("GAME OVER! You hit the wall!")
        score.display_score()
        game_over()

    if snake.body_hit():
        print("GAME OVER! You ate your own tail!")
        score.display_score()
        game_over()

    x_position_min, x_position_max = int((width / 2) * (-1)), int(width / 2)
    y_position_min, y_position_max = int((height / 2) * (-1)), int(height / 2)

    sleep(0.01)
    screen.update()

screen.exitonclick()
