import random
import turtle as t


race_started = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
winning_colors = []

for turtle_index in range(0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-75 + 30*turtle_index)
    all_turtles.append(new_turtle)


if user_bet:
    race_started = True

while race_started:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        # rand_distance = 10
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            race_started = False
            winning_colors.append(turtle.pencolor())


if len(winning_colors) > 1:
    print("It's a tie between: ")
    for color in winning_colors:
        print(f" - {color}")
else:
    winning_color = winning_colors[0]
    if winning_color == user_bet:
        print(f"Yow've won! The {winning_color} turtle is the winner!")
    else:
        print(f"Yow've lost! The {winning_color} turtle is the winner!")


screen.bye()