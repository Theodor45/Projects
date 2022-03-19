import gc
import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

all_cars = []
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

times_ran = 0
game_is_on = True
while game_is_on:
    scoreboard.print_score()
    times_ran += 1
    if times_ran == 6:
        times_ran = 0
        new_car = CarManager()
        all_cars.append(new_car)
    for f in all_cars:
        if f.xcor() < -320:
            del f
        elif f.distance(player) < 20:
            scoreboard.game_over()
            time.sleep(2)
            exit()
        else:
            f.move()
    if player.ycor() > 300:
        player.goto(0, -280)
        scoreboard.add_to_score()

    time.sleep(0.1)
    screen.update()
