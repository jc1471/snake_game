from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Futura", 12, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.update_score

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)

    def update_score(self, score):
        self.write(arg=f'Score: {score}', move=False, align=ALIGNMENT, font=FONT)