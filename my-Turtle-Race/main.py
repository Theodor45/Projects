import random
from re import T, U
from turtle import Turtle, Screen

race_on = False
screen = Screen()
colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput("Make your bet!", 'Which color will win the race? Enter a color: ').lower
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle('turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x = -230, y = y_pos[turtle_index])
    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won!")
                exit()
            else:
                print(f"You lost! The {winning_color} turtle won!")
                exit()
        distance = random.randint(0, 10)
        turtle.forward(distance)



screen.exitonclick()
