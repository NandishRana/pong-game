from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.goto(0.00, 280.00)
        self.hideturtle()

        self.score_P1 = 0
        self.score_P2 = 0
        self.update_scoreboard("placeHolder")



    # def game_over(self):
    #     self.clear()
    #     self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)


    def update_scoreboard(self, player):
        self.clear()
        if player == "P1":
            self.score_P1 += 1
        elif player == "P2":
            self.score_P2 += 1
        self.write(f"{self.score_P1} {self.score_P2}", False, align=ALIGNMENT, font=FONT)
