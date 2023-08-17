from turtle import Turtle

DASH_SIZE = 10
GAPS = 15
LINE_THICKNESS = 5
FONT = ("Courier", 20, "normal")


class FieldLine(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0.00, -350.0)
        self.setheading(90)
        self.pensize(LINE_THICKNESS)
        self.dasher()

    def dasher(self):
        while self.ycor() < 350.00:
            self.pendown()
            self.forward(DASH_SIZE)
            self.penup()
            self.forward(GAPS)
