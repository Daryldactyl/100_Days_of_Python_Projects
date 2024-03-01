from turtle import Turtle, ycor

STARTING_POSITION = [(350,0), (350,20), (350, 40), (350, -20), (350,-40)]
STARTING_POSITION_2 = [(-350,0), (-350,20), (-350, 40), (-350, -20), (-350,-40)]
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)










