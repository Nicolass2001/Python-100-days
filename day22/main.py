from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import utils
import time

LEFT_SIDE = True
RIGHT_SIDE = False

screen = Screen()
utils.set_screen(screen)

paddle_left = Paddle((-280,0))
paddle_right = Paddle((280,0))
score_left = Score(LEFT_SIDE)
score_right = Score(RIGHT_SIDE)
ball = Ball(RIGHT_SIDE)

utils.asign_keys(screen, paddle_left, paddle_right)
utils.set_net()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceTopDown()
    
    if ball.xcor() < -260 and ball.distance(paddle_left) < 50:
        ball.bounceLeftRight()
    
    if ball.xcor() > 260 and ball.distance(paddle_right) < 50:
        ball.bounceLeftRight()

    if ball.xcor() < -270:
        ball.home(RIGHT_SIDE)
        score_right.add_score()
        paddle_left.goto_start()
        paddle_right.goto_start()

    if ball.xcor() > 270:
        ball.home(LEFT_SIDE)
        score_left.add_score()
        paddle_left.goto_start()
        paddle_right.goto_start()
