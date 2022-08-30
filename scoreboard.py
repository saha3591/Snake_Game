from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.refresh()

    def ending_message(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
