from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 180)
        self.write(arg=f"{self.p1_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(280, 180)
        self.write(arg=f"{self.p2_score}", align="center", font=("Courier", 80, "normal"))

    def p1_scored(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_scored(self):
        self.p2_score += 1
        self.update_scoreboard()