FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.user_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=0,y=270)
        self.write(self.user_score,align="center",font=FONT)

    def increase_score(self):
        self.user_score += 1
        self.update_score()

    def game_over_score(self):
        self.clear()
        self.goto(x=0,y=0)
        self.write(f"YOUR SCORE: {self.user_score}", align="center", font=FONT)



