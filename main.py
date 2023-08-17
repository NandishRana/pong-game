from turtle import Screen
from paddles import Bars
from field import FieldLine
from ball import TheBall
from scoreboard import Score
import time


screen = Screen()

screen.setup(width=1500, height=800)
screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)

paddle = Bars()
playing_field = FieldLine()
ball = TheBall()
score = Score()

screen.listen()

screen.onkeypress(key="Up", fun=paddle.p1_up)
screen.onkeypress(key="Down", fun=paddle.p1_down)

screen.onkeypress(key="w", fun=paddle.p2_up)
screen.onkeypress(key="s", fun=paddle.p2_down)


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    ball.forward(30)

    # Detect collision of the balls and paddles
    if ball.distance(paddle.P1) <40  or ball.distance(paddle.P2) < 40:
        ball.setheading(180-ball.heading())

    # Detect collision of balls with court
    elif ball.ycor() > 350 or ball.ycor() < -350:
        ball.setheading(-ball.heading())

    # Detect collision of balls with boundary
    if ball.xcor() > 740:
        score.update_scoreboard("P1")
        ball.refresh()
    elif ball.xcor() < -740:
        score.update_scoreboard("P2")
        ball.refresh()


screen.exitonclick()
