from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_clock_wise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def move_anti_clock_wise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_anti_clock_wise)
screen.onkeypress(key="d", fun=move_clock_wise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
