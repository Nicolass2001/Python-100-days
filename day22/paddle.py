from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, initial_position):
        super().__init__(shape="square")
        self.initial_position = initial_position
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.8, stretch_len=4)
        self.setheading(90)
        self.goto_start()

    def up(self):
        self.forward(10)

    def down(self):
        self.back(10)

    def goto_start(self):
        self.goto(self.initial_position)