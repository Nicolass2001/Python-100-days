from turtle import Turtle

FONT = ('Courier', 40, "normal")

class Score(Turtle):

    def __init__(self, side):
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        if side:
            position = (-40, 230)
        else:
            position = (40, 230)
        self.setposition(position)
        self.score = 0
        self.write_score()

    def add_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.score}", align="center", font=FONT)

