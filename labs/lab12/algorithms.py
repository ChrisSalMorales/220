"""
Christopher Morales
lab13.py

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

def is_in_binary(search_val, values):
    lower_number = 0
    higher_number = len(values) - 1
    while lower_number <= higher_number:
        middle = (lower_number + higher_number)// 2
        guess_value = middle
        if search_val == guess_value:
            return middle
        elif search_val < guess_value:
            higher_number = middle - 1
        else:
            lower_number = middle + 1
    return -1

def selection_sort(values):
    for i in range(len(values)-1):
        min_index = i
        for h in range(i + 1, len(values)-1):
            if values[h] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]

def calc_area(rect):
    list = []
    for i in rect:
        list.append(i[0]*i[1])
    selection_sort(list)
    return list

def rect_sort(rectangles):
