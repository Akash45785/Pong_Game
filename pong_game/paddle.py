from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)
        screen.update()

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
        screen.update()

