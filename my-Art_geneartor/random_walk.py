from turtle import Turtle
import random
import turtle

paths = ['right', 'left']

t = Turtle()
t.pensize(20)
t.forward(20)
turtle.screensize(500, 500, 'white')
t.speed(25)
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

while True:
    t.color(random_color())
    choice = random.choice(paths)
    if choice == 'right':
        t.right(90)
    elif choice == 'left':
        t.left(90)
    t.forward(50)    
    





screen = turtle.Screen()
screen.exitonclick()
