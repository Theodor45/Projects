from classes import WriteStateName
from classes import ScoreBoard
import turtle
import pandas

# Setting up the game
screen = turtle.Screen()
screen.title('U.S States Guesser')
image = 'blank_states_img.gif'
screen.addshape(image)

scoreboard = ScoreBoard()
writer = WriteStateName()

# Making the background map
turtle.penup()
turtle.shape(image)

# Getting the necessary values
data = pandas.read_csv('50_states.csv')
states = data['state'].tolist()
x = data['x'].tolist()
y = data['y'].tolist()
x_y = []
for f in range(len(states)):
    x_y.append((x[f], y[f]))

# Adjustments
answer_list = []
score = 0

# Main game loop
while True:
    scoreboard.show_score()
    answer = screen.textinput(title="Guess the State", prompt='State name: ')
    answer_state = str(answer).title()
    if answer_state in states and answer_state not in answer_list:
        scoreboard.addscore()
        answer_list.append(answer_state)
        score += 1
        place = states.index(answer_state)
        x_and_y = x_y[place]
        writer.writedaname(x_and_y_pair=x_and_y, name=answer_state)

    elif answer_state in answer_list:
        print("You already entered that dummy!")
        continue

screen.mainloop()