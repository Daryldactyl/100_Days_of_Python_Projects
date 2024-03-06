from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True

player = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down,"Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")



while game_is_on:
    screen.update()
    time.sleep(.1)
    player.move()
    if player.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        player.extend()
    if player.head.xcor() > 290 or player.head.xcor() < -300 or player.head.ycor() > 299 or player.head.ycor() < -290:
        scoreboard.reset()
        player.reset()
    for segment in player.segments[1:]:
        if player.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()























screen.exitonclick()