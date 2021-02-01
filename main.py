from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
    # if len(snake.segments) > 3:
    #     for idx, segment in enumerate(snake.segments[1:]):
    #         print(idx, snake.head.distance(segment))





screen.exitonclick()