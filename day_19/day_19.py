from turtle import Turtle, Screen, reset

turtle = Turtle()
screen = Screen()
turtle.speed(10)


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_right():
    turtle.right(5)


def turn_left():
    turtle.left(5)


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="a")
screen.onkey(fun=turn_left, key="d")
screen.onkey(fun=screen.reset, key="c")


screen.exitonclick()