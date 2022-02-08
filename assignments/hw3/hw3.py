"""
Name: Christopher Morales
homework_three.py

Problem: The purpose of these programs is to show efficient use of for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    sum_of_grades = 0
    how_many_grades_will_be_entered = eval(input('how many grades will you enter?'))
    for amount_of_times_grades_entered in range(1, how_many_grades_will_be_entered + 1):
        print('Enter grade:')
        grade_entered = eval(input(''))
        sum_of_grades = sum_of_grades + grade_entered
    average_of_grades = sum_of_grades / how_many_grades_will_be_entered
    print('average is', round(average_of_grades, 1))


def tip_jar():
    sum_of_tips = 0
    for loop_of_question in range(5):
        print('how much would you like to donate?')
        amount_donated = eval(input(''))
        sum_of_tips = sum_of_tips + amount_donated
    print('total tips:', round(sum_of_tips, 2))


def newton():
    approx = 1
    number_square_root = float(eval(input('What number do you want to square root?')))
    improve_approximation = int(eval(input('How many times should we improve the approximation?')))
    for approximation in range(improve_approximation):
        approx = (approx + (number_square_root / approx)) / 2
    print('the square root is approximately', approx)


def sequence():
    number_in_sequence = eval(input('how many terms would you like?'))
    for i in range(number_in_sequence):
        number_in_sequence = i + 1 - (i % 2)
        print(number_in_sequence, end ='\t')


def pi():
    accumulator = 1
    term_series = eval(input('how many terms in the series?'))
    for i in range(1, term_series + 1):
        numerator = i +(i%2)
        denomerator = i + 1-(i%2)
        accumulator = accumulator * (numerator * denomerator)
    result = accumulator * 2
    print(result)
pi()

