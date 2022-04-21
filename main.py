#1-create the screen 2-create and move a paddle
#3-create another paddle 4-create the ball and make it move
#5-detect collision with wall and bounce 6-detect collision with paddle
#7-detect when paddle misses 8-keep score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()      #1
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My pong game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeypress(l_paddle.go_up, "w")

game_is_on = True   #2
while game_is_on:
    #time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()