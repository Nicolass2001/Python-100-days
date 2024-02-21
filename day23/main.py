import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1,6) == 1:
        car_manager.generate_car()
        
    car_manager.move_cars()

    if car_manager.hit(player):
        game_is_on = False
        scoreboard.game_over()

    if player.pass_level():
        player.goto_starting_position()
        scoreboard.add_level()
        car_manager.increment_speed()

screen.exitonclick()