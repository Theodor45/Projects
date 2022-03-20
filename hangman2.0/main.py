import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

print(logo)
# Getting the random number
chosen_word = random.choice(word_list)
# Making the display word
display = []
for char in chosen_word:
    display += "_"
# Defining some needed variables
lives = len(stages) - 1
end_of_game = False

# To clear the terminal, but i don't know how to use it
def clear(): os.system('clear') #on Linux System
tries = 0
previous_guess = ""
# Starting the actual game loop
while not end_of_game:
    tries =+ 1
    # Getting and checking input
    print(f"{' '.join(display)}")
    guess = str(input("Guess a letter: "))
    if len(guess) != 1:
        print("Guess one letter at a time!")
        exit()
    if previous_guess == guess:
        print("You already guessed that dummy...")
        continue
    previous_guess = guess
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        # Changing the letter in display as well
        if letter == guess:
            display[position] = guess
    # Punishing the player 
    if guess not in chosen_word:
        lives -= 1
        print(f"There was no {guess} in the word. You lose a life!")
    # Winning and losing the game
    if lives == 0:
        end_of_game = True
        print("\nYou lose!")
        print(f"\t{chosen_word} was the answer!")
    elif "_" not in display:
        end_of_game = True
        print("\nYou win!")
    # Printing the ASCII art
    print(stages[lives])




