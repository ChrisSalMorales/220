"""
Christopher Morales
lab7.py

Problem: To write a program that uses the graphics package and practice decision statements

Certification of Authenticity:
I certify that this assignment is my own work.
"""
from random import randint
from graphics import*
import math
import time


def get_random(move_amt):
# returns a random integer number in the range [-move_amount, +move_amount]
    return randint(-move_amt, move_amt)

def did_collide(ball, ball2):
# returns boolean based on the collision of the two balls
    distance = math.sqrt((ball2.getCenter().getX() - ball.getCenter().getX())** 2 + (ball2.getCenter().getY() -
                                                                                    ball.getCenter().getY())** 2)
    ball1_rad = ball.getRadius()
    ball2_rad = ball2.getRadius()

    return ((ball1_rad + ball2_rad) >= distance )

def hit_vertical(ball, win):
# returns true if ball hits a vertical wall, false otherwise
    ball_y = ball.getCenter().getY()
    radius = ball.getRadius()
    win_height = win.getHeight()

    return (ball_y < radius) or (win_height - ball.getRadius() <= ball_y)

def hit_horizontal(ball, win):
# returns true if ball hits a horizontal wall, false otherwise
    ball_x = ball.getCenter().getX()
    radius = ball.getRadius()
    edge_one = ball_x - radius
    edge_two = ball_x + radius
    return (edge_one < 0 or win.getWidth() < edge_two)

def get_random_color():
    # returns a random color
    # use get_random(amt)
    return color_rgb(randint(0,255), randint(0,255), randint(0,255))


def bumper():
    win = GraphWin("Bumper", 700, 700)
    win.setBackground('white')
    ball = Circle(Point(randint(0,700),randint(0,700)), 20)
    ball.setFill(get_random_color())
    ball_two = Circle(Point(randint(0, 700), randint(0, 700)), 20)
    ball_two.setFill(get_random_color())
    ball.draw(win)
    ball_two.draw(win)

    ball_dx = get_random(20)
    ball_dy = get_random(20)
    ball_two_dx = get_random(20)
    ball_two_dy = get_random(20)

    while not win.checkMouse():
        ball.move(ball_dx, ball_dy)
        ball_two.move(ball_two_dx, ball_two_dy)
        time.sleep(0.1)

        if did_collide(ball, ball_two):
            ball_dx = -ball_dx
            ball_dy = -ball_dy
            ball_two_dx = -ball_two_dx
            ball_two_dy = -ball_two_dy

        if hit_vertical(ball, win):
            ball_dy = -ball_dy

        if hit_vertical(ball_two, win):
            ball_two_dy = -ball_two_dy

        if hit_horizontal(ball, win):
            ball_dx = -ball_dx

        if hit_horizontal(ball_two, win):
            ball_two_dx = -ball_two_dx

bumper()