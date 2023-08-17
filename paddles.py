from turtle import Turtle

STEP_FORWARD = 30
STEP_BACKWARD = -30
POSITION_OF_BARS = 740.00


class Bars:

    def __init__(self):
        self.players = []

        for i in range(2):
            player = Turtle()
            player.penup()
            player.color("white")
            player.shape("square")
            player.shapesize(stretch_wid=1, stretch_len=4)
            player.setheading(90)

            self.players.append(player)

            player.goto(POSITION_OF_BARS - (i * 2 * POSITION_OF_BARS), 0.00)

        self.P1 = self.players[0]
        self.P2 = self.players[1]

    def p1_up(self):
        self.P1.forward(STEP_FORWARD)

    def p2_up(self):
        self.P2.forward(STEP_FORWARD)

    def p1_down(self):
        self.P1.backward(STEP_FORWARD)

    def p2_down(self):
        self.P2.backward(STEP_FORWARD)
