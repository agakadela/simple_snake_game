"""snake.py module for Snake class"""
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake():
    """Class for the snake object"""

    def __init__(self):
        self.x_position = 0
        self.snake_elements = []
        self.create_snake()
        self.head = self.snake_elements[0]

    def create_snake(self):
        """Create snake object"""
        for position in STARTING_POSITIONS:
            self.add_snake_element(position)

    def add_snake_element(self, position):
        """Add new element to snake"""
        snake_elem = Turtle('square')
        snake_elem.color('white')
        snake_elem.penup()
        snake_elem.goto(position)
        self.snake_elements.append(snake_elem)

    def move(self, direction):
        """Move snake object"""
        for snake_elem in range(len(self.snake_elements) - 1, 0, -1):
            new_x = self.snake_elements[snake_elem - 1].xcor()
            new_y = self.snake_elements[snake_elem - 1].ycor()
            self.snake_elements[snake_elem].goto(new_x, new_y)
        if isinstance(direction, str):
            match direction.lower():
                case 'up':
                    if self.head.heading() != DOWN:
                        self.head.setheading(UP)
                case 'down':
                    if self.head.heading() != UP:
                        self.head.setheading(DOWN)
                case 'left':
                    if self.head.heading() != RIGHT:
                        self.head.setheading(LEFT)
                case 'right':
                    if self.head.heading() != LEFT:
                        self.head.setheading(RIGHT)
                case _:
                    pass
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        """Add new element to snake"""
        self.add_snake_element(self.snake_elements[-1].position())
