"""
Name: Christopher Morales
homework_getting_started.py

Problem: Using basic python programming to solve mathematical problems using inputs, arithmetics, and outputs.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooting_percentages = round(shots_made / total_shots * 100, 2)
    print("Shooting Percentage: ", shooting_percentages, "%")


def coffee():
    pounds_of_coffee = eval(input("How many pounds of coffee would you like? "))
    coffee_costs = round(pounds_of_coffee * 10.50, 2)
    shipping_costs = round(pounds_of_coffee * 0.86, 2)
    total_costs = coffee_costs + shipping_costs + 1.50
    print("You're total is: ", total_costs)


def kilometers_to_miles():
    kilometers_traveled = eval(input("How many kilometers did you travel? "))
    miles_traveled = round(kilometers_traveled * 0.62111801, 1)
    print("That's", miles_traveled, "miles!")
