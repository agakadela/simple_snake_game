"""Main file for snake game"""
from turtle import Screen
import time
import functools
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()

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
    snake.move('right')



screen.exitonclick()
