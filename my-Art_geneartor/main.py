from turtle import Turtle
from turtle import Screen
from random import choice
colors = ['crimson', 'spring green', 'blue', 'orange', 'purple', 'yellow', 'dark violet', 'cyan', 'red', 'green']
turtle = Turtle()
def draw_shape(side_num):
    angle = 360 / side_num
    for num in range(side_num):
        turtle.right(angle)
        turtle.forward(100)

for side in range(3, 11):
    turtle.color(choice(colors))
    draw_shape(side)


screen = Screen()
screen.exitonclick()
