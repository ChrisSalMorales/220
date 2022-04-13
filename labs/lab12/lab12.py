"""
Christopher Morales
lab12.py

Problem: The purpose of this program is to develop while control structures,
use python's built-in list methods, and perform
linear search on data.

Certification of Authenticity:
I certify that this assignment is my own work.
"""
from random import randint

def find_and_remove_first(list,value):
    first_occurence_of_value_index = list.index(value)
    remove_the_value = list.pop(first_occurence_of_value_index)
    inserting_name_into_list = list.insert(first_occurence_of_value_index, 'Christopher Morales')

def nums_digits():
    number = int("")
    while :

def hi_lo_game():
    random_number = randint(1, 100)
    acc = 0
    while acc < 7:
        guess = int(input("Guess the Number:"))
        if guess == random_number:
            print("You win in", acc + 1,"guesses!")
        elif guess > random_number:
            print("too high")
        elif guess < random_number:
            print("too low")
        acc += 1
    else:
        print("Sorry, you lose. The number was ", random_number)
