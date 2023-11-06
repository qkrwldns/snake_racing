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
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.reset_food()
        score.update_score()  # Call the updated method
        snake.extend()
    # wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        game = False
        score.know_game_over()

    # tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game = False
            score.know_game_over()
window.exitonclick()