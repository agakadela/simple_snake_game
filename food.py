"""food.py module for Food class"""
from turtle import Turtle
import random


class Food(Turtle):
    """Class for the food object."""

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('red')
        self.speed('fastest')
        random_x_pos = random.randint(-280, 280)
        random_y_pos = random.randint(-280, 280)
        self.goto(random_x_pos, random_y_pos)

    def refresh(self):
        """Refresh food position"""
        random_x_pos = random.randint(-280, 280)
        random_y_pos = random.randint(-280, 280)
        self.goto(random_x_pos, random_y_pos)
