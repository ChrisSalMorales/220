"""
Christopher Morales
lab12.py

Problem: The purpose of this program is to develop while control structures,
use python's built-in list methods, and perform
linear search on data.

Certification of Authenticity:
I certify that this assignment is my own work.
"""

def read_data(filename):
    opened_file = open(filename, "r")
    values = opened_file.read()
    values_two = values.split()
    acc = 0
    data_list = []
    while acc < len(values_two):
        data_list.append((values_two[acc]))
        acc += 1
    return data_list

def is_in_linear(search_val, values):
    acc = 0
    while acc < len(values):

        acc += 1
        if a == search_val:
            return True
        else:
            return False

is_in_linear(1, [1,2,3,4])

