"""
Name: Christopher Morales
homework_2.py

Problem: The task given is to provide programs that use only inputs, outputs, and arithmetics.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with:
Brooke Duvall in the Computer Science Tutoring Lab
"""
import math


def sum_of_threes():
    sum_of_three = 0
    upper_bound = eval(input("What is the upper bond?"))
    for i in range(0, upper_bound + 1):
        if i % 3 == 0:
            sum_of_three += i
    print("sum of threes is", sum_of_three)


def multiplication_table():
    for multiplication_one in range(1, 11):
        for multiplication_two in range(1, 11):
            print(multiplication_one * multiplication_two, end="\t")
        print()


def triangle_area():
    a_length = eval(input("Enter side a length: "))
    b_length = eval(input("Enter side b length: "))
    c_length = eval(input("Enter side c length: "))
    s = (a_length + b_length + c_length) / 2
    before_squaring = s * (s - a_length) * (s - b_length) * (s - c_length)
    area_of_a_triangle = math.sqrt(before_squaring)
    print("area is", area_of_a_triangle)


def sum_squares():
    sum_squares_lower_and_upper_range = 0
    lower_range = eval(input("Enter lower range:"))
    upper_range = eval(input("Enter upper range:"))
    for sum_times_squares in range(lower_range, upper_range + 1):
        sum_squares_lower_and_upper_range += sum_times_squares * sum_times_squares
    print(sum_squares_lower_and_upper_range)


def power():
    power_result = 1
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    for power_loop in range(1, exponent + 1):
        power_result = base * power_result
    print(base, "^", exponent, "=", power_result)
