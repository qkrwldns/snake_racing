from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


window = Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake = Snake()
score = Score()
food = Food()

window.listen()
window.onkey(snake.up,"Up")
window.onkey(snake.down,"Down")
window.onkey(snake.left,"Left")
window.onkey(snake.right,"Right")

game = True
while game:
    window.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.reset_food()
        score.update_score()  # Call the updated method
        snake.extend()
        score.plus_score()
    # wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        score.reset()
        snake.reset()
    # tail
    for i in snake.segments[1:]:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            score.reset()
            snake.reset()


window.exitonclick()