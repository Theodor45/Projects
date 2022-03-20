from turtle import Turtle
import json
import turtle

class WriteStateName(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.hideturtle()

    def writedaname(self, x_and_y_pair, name):
        self.goto(x_and_y_pair)
        self.write(arg=name, align='center')
        del self


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.score = 0
        self.highscore = json.load('highscore.json')

    def addscore(self):
        self.score += 1

    def show_score(self):
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score

        with open('highscore.json',mode = 'w+') as high:
            if int(high.read()) < self.highscore:
                high.truncate(0)
                high.write(str(self.highscore))

        self.goto(300, 250)
        self.write(arg=f'Score: {self.score}, Highscore: {self.highscore}', align='center')
