from turtle import Turtle, Screen
from paddle import Paddle
import time
from divider import Divider
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
game_is_on = True


paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
divider = Divider()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down,"Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle1) < 50 and ball.xcor() > 330 or ball.distance(paddle2) < 50 and ball.xcor() < -330:
        ball.hit()
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()