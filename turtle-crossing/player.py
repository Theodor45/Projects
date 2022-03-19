from turtle import Turtle
import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__('turtle')
        self.hideturtle()
        self.setheading(90)
        self.color('red')
        self.penup()
        self.goto(0, -280)
        self.showturtle()
        self.showturtle()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() < -270:
            pass
        else:
            self.backward(MOVE_DISTANCE)


        
