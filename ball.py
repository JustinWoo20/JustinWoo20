from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        if self.move_speed > 0:
            self.move_speed *= 0.75

    def new_ball(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.paddle_bounce()
