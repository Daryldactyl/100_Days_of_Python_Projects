from turtle import Turtle

class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(3)
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        for i in range (30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
