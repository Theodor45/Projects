import pandas
import time
import os

def clear():
    os.system('clear')

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

end_of_game = False
while not end_of_game:
    word = input('Enter a word: ')
    words = []
    letters = []
    for letter in word:
        letters.append(letter.upper())
    for letter in letters:
        for f in data_dict:
            if f == letter:
                words.append(data_dict[f])
    clear()
    print(words)
    if input("Want to do it again? ('yes'/'no')") == 'yes':
        clear()
        continue
    elif input("Want to do it again? ('yes'/'no')") == 'no':
        print('Bye')
        exit()
    else:
        print("Enter a valid choice!")
        pass


