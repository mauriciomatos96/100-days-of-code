from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 265)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update()
        self.hideturtle()




    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="Center", font=('Courier', 24, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_high_score:
                new_high_score.write(str(self.high_score))
        self.score = 0
        self.update()

    def point(self):
        self.score += 1
        self.update()