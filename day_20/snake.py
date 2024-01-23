from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.starting_x = 0

        for i in range(3):
            snake_piece = Turtle(shape="square")
            snake_piece.resizemode("user")
            snake_piece.shapesize(0.25, 0.25, 3)
            snake_piece.color('white')
            snake_piece.penup()
            snake_piece.speed(0)
            snake_piece.goto(x=self.starting_x, y=0)
            self.snake_body.append(snake_piece)
            self.starting_x -= 5

        self.snake_head = self.snake_body[0]
        self.snake_size = len(self.snake_body)

    def turn_left(self):
        self.snake_head.seth(180)

    def turn_right(self):
        self.snake_head.seth(0)

    def turn_up(self):
        self.snake_head.seth(90)

    def turn_down(self):
        self.snake_head.seth(270)

    def move(self, speed):
        for snake_piece in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snake_piece].goto(self.snake_body[snake_piece - 1].pos())
        self.snake_head.forward(speed)

    def grow(self):
        snake_piece = Turtle(shape="square")
        snake_piece.resizemode("user")
        snake_piece.shapesize(0.25, 0.25, 1)
        snake_piece.color('white')
        snake_piece.penup()
        snake_piece.speed(0)
        snake_piece.goto(self.snake_body[-1].pos())
        self.snake_body.append(snake_piece)
        self.snake_size = len(self.snake_body)

