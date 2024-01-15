from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, font=("Courier", 50, "normal"))

    def l_goal(self):
        self.l_score += 1
        self.update()

    def r_goal(self):
        self.r_score += 1
        self.update()
