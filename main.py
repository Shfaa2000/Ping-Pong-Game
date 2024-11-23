import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_pp import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Octocode: Ping Pong")
screen.tracer(0)
default_sleep = 0.1

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)
    time.sleep(default_sleep)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1
    if ball.xcor() >= 330 and ball.distance(paddle_r) <= 50:
        ball.x_move *= -1
        default_sleep *= 0.9
    if ball.xcor() <= -330 and ball.distance(paddle_l) <= 50:
        ball.x_move *= -1
        default_sleep *= 0.9

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.x_move *= -1
        scoreboard.l_point()
        default_sleep = 0.1
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_move *= -1
        scoreboard.r_point()
        default_sleep = 0.1


screen.exitonclick()