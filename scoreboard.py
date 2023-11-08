
from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",20,"normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
          # Change the variable name to avoid conflicts
        self.score_value = 0
        with open("score.txt") as score:
            self.high_score = int(score.read())
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(f"Score : {self.score_value}",align=ALIGN, font=FONT)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score_value} High Score: {self.high_score}",align=ALIGN, font=FONT)

    def reset(self):
        if self.score_value > self.high_score:
            self.high_score = self.score_value
            with open("score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score_value = 0 #얘를 reset 함수 맨 처음에 정의하면 if문은 영원히 성립되지 않음 그러니 if문이 끝나고 0으로 설정
        self.update_score()

    def plus_score(self):
        self.score_value += 1
        self.update_score()
