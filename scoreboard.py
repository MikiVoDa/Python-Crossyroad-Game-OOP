from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240, 270)
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)