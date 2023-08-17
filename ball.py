from turtle import Turtle
import random

INITIAL_DIRECTION = random.randint(0, 360)


class TheBall(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.speed("slowest")
        self.shape("circle")
        self.color("white")
        self.refresh()
        self.setheading(INITIAL_DIRECTION)

    def refresh(self):
        random_y = random.randint(-350, 350)
        self.goto(0.00, random_y)

