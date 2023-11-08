from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#상수로 쓸때 모두 대문잘로 씀 그리고 언더바로 구분

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in STARTING_POSITIONS:
            new = Turtle()
            new.shape("square")
            new.color("yellow")
            new.penup()
            new.goto(i)
            self.segments.append(new)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()   # 삭제가 아니라 화면 밖으로 이동,,?
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        new = Turtle()
        pos_x = self.segments[len(self.segments)-1].xcor()
        pos_y = self.segments[len(self.segments)-1].ycor()
        new.shape("square")
        new.color("yellow")
        new.penup()
        new.goto(pos_x,pos_y)
        self.segments.append(new)


    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            pos_x = self.segments[i-1].xcor()
            pos_y = self.segments[i - 1].ycor()
            self.segments[i].goto(pos_x,pos_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# 숫자들을 상수로 바꿔주는 이유는 위치나 속도를 원할때마다 코드 속에서 찾아서 숫자를 바꾸는게 아니라 그냥 상수안의 숫자만 바꾸면 됨 더 쉬워짐

