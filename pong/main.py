from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 60:
        ball.hit()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 60:
        ball.hit()

    if ball.xcor() > 390:
        scoreboard.p1_scored()
        ball.reset_position()
        ball.reset_bounce()
    if ball.xcor() < -390:
        scoreboard.p2_scored()
        ball.reset_position()
        ball.reset_bounce()