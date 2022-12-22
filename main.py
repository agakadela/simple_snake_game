"""Main file for snake game"""
import time
import functools
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


def snake_moving(direction):
    """running move function from snake class"""
    snake.move(direction)


screen.listen()
for k in ["Up", "Down", "Left", "Right"]:
    screen.onkeypress(functools.partial(snake_moving, k), key=k)

GAME_IS_ON = True

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move(None)

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()


screen.exitonclick()
