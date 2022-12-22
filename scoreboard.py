"""scoreboard.py module for Scoreboard class"""
from turtle import Turtle


class Scoreboard(Turtle):
    """Class for scoreboard object"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}", align='center',
                   font=('Arial', 24, 'normal'))

    def game_over(self):
        """Game over"""
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        """Increase score"""
        self.score += 1
        self.update_scoreboard()
