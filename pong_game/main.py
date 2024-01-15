from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
paddle = Turtle()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

ball = Ball()
score = Score()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = 1

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        score.l_goal()
        ball.speed *= 0.9

    if ball.xcor() < -380:
        ball.restart()
        score.r_goal()
        ball.speed *= 0.9

screen.exitonclick()
