from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=(FONT))

    def point(self):
        self.level += 1
