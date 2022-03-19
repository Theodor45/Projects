from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fast')
        self.level = 0
        self.highscore = 0

    def add_to_score(self):
        self.level += 1

    def print_score(self):
        self.hideturtle()
        self.goto(-280, 250)
        self.clear()
        self.write(f"LEVEL: {self.level}", align='left', font=FONT)


    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)
