from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

pad1 = Paddle((350, 0))
pad2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(pad1.move_up, "Up")
screen.onkey(pad1.move_down, "Down")

screen.onkey(pad2.move_up, "w")
screen.onkey(pad2.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect collision with paddle
    if ball.distance(pad1) < 50 and ball.xcor() > 320 or ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_pos()
        score.left_point()
    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_pos()
        score.right_point()


screen.exitonclick()
