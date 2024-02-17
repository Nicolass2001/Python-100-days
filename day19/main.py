import turtle as t

tim = t.Turtle()
screen = t.Screen()

tim.shape('turtle')


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_rigth():
    tim.rt(10)


def turn_left():
    tim.lt(10)


def clear_and_center():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_rigth)
screen.onkey(key="c", fun=clear_and_center)
screen.exitonclick()