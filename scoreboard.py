from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        # check if current score is higher than high score
        # if yes, update high score to current score
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.clear()
        self.text = f"Score: {self.score} High Score:  {self.high_score}"
        self.write(self.text, align=ALIGNMENT, font=FONT)

    # def reset(self):
    #     self.clear()
    #     self.__init__()