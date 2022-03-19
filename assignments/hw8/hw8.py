"""
Name: Christopher Morales
hw8.py

Problem: to use accumulations and use conditional control structures

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] += 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    total_sum = 0
    for i in range(len(nums)):
        total_sum = total_sum + nums[i]
    return total_sum


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    pass


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):



def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass


if __name__ == '__main__':
    pass
