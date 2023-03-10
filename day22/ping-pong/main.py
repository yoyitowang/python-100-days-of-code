from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

PADDLE_X = 350
r_paddle = Paddle((PADDLE_X, 0))
l_paddle = Paddle((-PADDLE_X, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.xcor() > PADDLE_X+30:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -(PADDLE_X+30):
        ball.reset_position()
        scoreboard.r_point()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(y=True)
    if (ball.xcor() > PADDLE_X-30 and ball.distance(r_paddle) < 50) or (ball.xcor() < PADDLE_X+30 and ball.distance(l_paddle) < 50):
        ball.bounce(x=True)


screen.exitonclick()