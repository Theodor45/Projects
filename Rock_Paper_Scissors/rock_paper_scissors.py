from ast import Index
import random
print("Rock Paper Scissors\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 

while True:
    try:
        choice = int(input("Enter 1 for rock, 2 for paper and 3 for scissors: ")) - 1
        break
    except ValueError:
        print("The input was not a valid integer.")
        exit()

array = [rock, paper, scissors]

if choice not in [0,1,2]:
    print("Please enter either 0, 1 or 2.")
    exit()
print(array[choice])

computer_choice = int(random.randint(0, 2))
print(f"Computer chose:\n{array[computer_choice]}")

isWinning = None
if choice == computer_choice:
    print("Try again.")
    exit()

diff = choice - computer_choice

if diff < 0:
    if diff == -1:
        isWinning = False
    else:
        isWinning = True
elif diff > 0:
    if diff == 1:
        isWinning = False
    else:
        isWinning = True

if isWinning == True:
    print("You win!")
else:
    print("You lose!")
