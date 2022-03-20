import json

with open('highscore.json', mode='r') as high:
    highscore = json.load(high)
print(highscore)