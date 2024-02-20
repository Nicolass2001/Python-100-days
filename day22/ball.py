from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self, side):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.home(side)

    def move(self):
        self.forward(10)

    def bounceTopDown(self):
        self.setheading(-self.heading())
        self.settiltangle(-self.heading())

    def bounceLeftRight(self):
        self.setheading(-self.heading() + 180)
        self.settiltangle(-self.heading())
        self.move_speed *= 0.9

    def home(self, side):
        super().home()
        self.move_speed = 0.1
        self.random_setheading(side)

    def random_setheading(self, side):
        direction = random.randint(0, 1) # up-down
        heading = (random.randint(25, 40) + 180 * side) * (-1) ** direction
        self.setheading(heading)
        self.settiltangle(-self.heading())
