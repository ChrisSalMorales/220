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
    result = 1
    number_in_sequence = eval(input('how many terms would you like?'))
    for i in list(range(1, number_in_sequence, 2)):
        result = (i)
    for b in list(range(1, number_in_sequence, 2)):
        result = (b)
    print(result)


def pi():
    fraction = 1
    terms = eval(input('how many terms in the series?'))
    for i in range(1, terms + 1):
        denominator = (2 * i) / (2 * i +1)
        numerator = (2 * i) / (2 * i -1)
        fraction = fraction * numerator * denominator
    answer_of_pi = fraction * 2
    print(answer_of_pi)

