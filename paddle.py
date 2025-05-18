from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)