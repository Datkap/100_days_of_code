from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.starting_x = 0

        for i in range(20):
            snake_piece = Turtle(shape="square")
            snake_piece.resizemode("user")
            snake_piece.shapesize(0.25, 0.25, 5)
            snake_piece.color('white')
            snake_piece.penup()
            # snake_piece.speed(0)
            snake_piece.goto(x=self.starting_x, y=0)
            self.snake_body.append(snake_piece)
            self.starting_x -= 5

        self.snake_head = self.snake_body[0]
        self.snake_size = len(self.snake_body)

    def turn_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.seth(180)

    def turn_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.seth(0)

    def turn_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.seth(90)

    def turn_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.seth(270)

    def move(self, speed):
        for snake_piece in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snake_piece].goto(self.snake_body[snake_piece - 1].pos())
        self.snake_head.forward(speed)

    def grow(self):
        snake_piece = Turtle(shape="square")
        snake_piece.resizemode("user")
        snake_piece.shapesize(0.25, 0.25, 5)
        snake_piece.color('white')
        snake_piece.penup()
        # snake_piece.speed(0)
        snake_piece.goto(self.snake_body[-1].pos())
        self.snake_body.append(snake_piece)
        self.snake_size = len(self.snake_body)

    def body_hit(self):
        return self.snake_head.pos() in [snake_piece.pos() for snake_piece in self.snake_body[1:]]

    def wall_hit(self, board_width, board_height):
        x_position_min, x_position_max = int((board_width / 2) * (-1)), int(board_width / 2)
        y_position_min, y_position_max = int((board_height / 2) * (-1)), int(board_height / 2)
        return self.snake_head.xcor() < x_position_min or self.snake_head.xcor() > x_position_max or \
               self.snake_head.ycor() < y_position_min or self.snake_head.ycor() > y_position_max

