import turtle
import random

turtle.speed(100)
turtle.circle(50)
angle = 0
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


while angle != 360:
    turtle.color(random_color())
    turtle.seth(angle)
    turtle.circle(70)
    angle += 3



screen = turtle.Screen()
screen.exitonclick()