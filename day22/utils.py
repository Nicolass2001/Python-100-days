from turtle import Turtle

def set_net():
    for i in range(-14, 15):
        aux = Turtle(shape="square")
        aux.penup()
        aux.color("white")
        aux.shapesize(stretch_wid=0.5, stretch_len=0.2)
        aux.setpos(0, i*20)

def set_screen(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

def asign_keys(screen, paddle_left, paddle_right):
    screen.listen()
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")
    screen.onkey(paddle_right.up, "i")
    screen.onkey(paddle_right.down, "k")