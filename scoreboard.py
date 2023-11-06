
from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",20,"normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_value = 0  # Change the variable name to avoid conflicts
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(f"Score : {self.score_value}",align=ALIGN, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.score_value += 1
        self.clear()
        self.write(f"Score : {self.score_value}",align=ALIGN, font=FONT)

    def know_game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"       Game Over \nyour final score is : {self.score_value}",align=ALIGN,font=FONT)