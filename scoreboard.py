from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.clear()
        self.text = f"Score: {self.score}"
        self.write(self.text, align=ALIGNMENT, font=FONT)