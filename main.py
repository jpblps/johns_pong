from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import time


screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

ball = Ball()

player1 = Player((-350, 0))

player2 = Player((350, 0))

screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with paddles.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.move_speed *= 0.9

    if ball.distance(player1) < 50 or ball.distance(player2) < 50:
        ball.bounce_x()
        ball.move_speed *= 0.99

    # Detect ball out of bounds and update scoreboard.
    if 405 > ball.xcor() > 395:
        scoreboard.p1_point()
        ball.reset_position()
        ball.move_speed = 0.05

    if -405 < ball.xcor() < -395:
        scoreboard.p2_point()
        ball.reset_position()
        ball.move_speed = 0.05

screen.exitonclick()
