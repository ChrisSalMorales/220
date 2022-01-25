"""
Christopher Morales
lab2.py

Problem: The purpose of this program is to provide the root-mean-square average, the harmonic mean and
the geometric mean, using only values entered into the program.

Certification of Authenticity:
I certify that this assignment is my own work.
"""


def means():
    number_that_will_be_inputted = eval(input("enter the values to be entered:"))
    rms_accumulator = 0
    harmonic_accumulator = 0
    geometric_accumulator = 1
    for entered_values in range(number_that_will_be_inputted):
        values_for_means = eval(input("enter value:"))
        squared = values_for_means ** 2
        rms_accumulator += squared
        one_divided_by_values_inputted = 1 / values_for_means
        harmonic_accumulator += one_divided_by_values_inputted
        geometric_accumulator *= values_for_means
    inside_the_arithmetic_mean = rms_accumulator / number_that_will_be_inputted
    rms_mean = round(inside_the_arithmetic_mean ** 0.5, 3)
    harmonic_mean = round(number_that_will_be_inputted / harmonic_accumulator, 3)
    geometric_mean = round(geometric_accumulator ** (1/number_that_will_be_inputted), 3)
    print("The RMS is:", rms_mean)
    print("The Harmonic mean is:", harmonic_mean)
    print("The Geometric mean is:", geometric_mean)
