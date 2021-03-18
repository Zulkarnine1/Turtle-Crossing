from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.display_score()


    def display_score(self):
        self.clear()
        self.goto(-240,240)
        self.color("black")
        self.write(f"Score: {self.score}",align="left",font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"Game over", align="left", font=FONT)


    def update_score(self):
        self.score += 1
        self.display_score()


