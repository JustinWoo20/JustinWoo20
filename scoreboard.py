from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Fantasy", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def l_get_point(self):
        self.l_score += 1
        self.update_score()
    def r_get_point(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-40, y=240)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(x=40, y=240)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)


    def l_winner(self):
        self.goto(0, 0)
        self.write(f"Left Player Wins!", align=ALIGNMENT, font=FONT)
    def r_winner(self):
        self.goto(0, 0)
        self.write(f"Right Player Wins!", align=ALIGNMENT, font=FONT)