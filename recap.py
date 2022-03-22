#Python is a high level interpreted language that was created in 20 february 1991 by 
#Guido van Rossum. It is a general purpose language that is used for small and big projects.

# You can store data that can be changed in variables:

age = 12 # This is an integer
name = 'Theodor' # This is a string
is_not_gay = True # This is a boolean
pp_size = 10.5 #This is a floating point number

# Other data types are:

friends = ['Andrei', 'Alex', 'Florian', 'Darius'] # This is a list
hobbys = {
    'coding': 'Fun and challeging',
    'basketball': "It's really fun",
    'school': "It's kind of annoying"
} # This is a dictionary
hobbys = ("coding", "basketball", "school", 'hacking') # This is a tuple and you can't change it
friends = {"Andrei", "Alex", "Stefan", "Darius"} # This is a set and you can't change it, the order is random

# You can use keywords like:  as, in, for, or, not, etc.
# There are loops:

for f in range(3):
    print('hello world')

i = 3
while i != 0:
    i -= 1
    print('hello world')

# You can make your own functions:

def say_name(name):
    return f"Hi, {name}"

# You can import other people's code

import math
import pandas
import random
import time
import os

# You can open files

with open('new_file', mode='r+') as f:
    f.write("Hello world!")
    content = str(f.read())

# You can make blueprints and then objects from the blueprints
# The blueprints are classes

# Functions in classes are called methods

class Person():

    def __del__(self):
        # This function does something if the object is deleted
        print("NOOO I DIED")

    # The __init__ method is executed when you create a object
    def __init__(self):
        # Self is the name of the object that we create in this case
        self.name = 'Theodor'
        self.age = 18
        self.hobbys = hobbys
    
    def grow(self):
        self.age += 1
    
    def die(self):
        # Del deletes the created object
        del self

andrew = Person()
alex = Person()
alex.die()

# Class inheritance
# You can add methods and class variables with inheritance

class Andrew(Person):
    # super() in this case is the Person() class
    print(super().age)

    def __init__(self):
        super().__del__()
        print("I died lol")

# You can handle python errors with:
# try, except, finally and else

try:
    age = int(input("Enter a number: "))
except ValueError:
    print("Enter a valid number!!")

# There is also:
lambda a, b : a * b

# But i don't know what this does yet

# With raise you can give out your own exceptions
# whenever you want to.
# Exemple

def get(what_to_get, how_many):
    if how_many > 5:
        raise Exception('Too many!')
    elif len(what_to_get.lower()) > 25:
        raise Exception('no')

