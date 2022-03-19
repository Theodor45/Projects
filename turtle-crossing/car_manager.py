from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __del__(self):
        print(f"Deleted: {self}")
    
    def __init__(self):
        super().__init__('square')
        self.speed('fast')
        self.hideturtle()
        self.setheading(180)
        self.shapesize(1, 2.5)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(320, random.randint(-250, 250))
        self.showturtle()

    def move(self):
        self.forward(10)

