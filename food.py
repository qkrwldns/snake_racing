from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle") # 터틀에 있는 기능을 스스로 쓸 수 있게 되는거임..
        self.up()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # 원래의 오브젝트 크기의 50%만큼을 가지는거
        self.color("red")
        self.speed(10)
        self.reset_food()  # food.reset_food 가 되려면 클래스안에 함수가 있어야 호출 가능? 아니면 좀 더 복잡하게 될듯..
    def reset_food(self):
        random_x = random.randint(-280, +280)
        random_y = random.randint(-280, +280)
        self.goto(random_x, random_y)

