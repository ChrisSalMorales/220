"""
Christopher Morales
lab5.py

Problem: To create a couple of functions meant to practice using python graphics and python string

Certification of Authenticity:
I certify that this assignment is my own work.
"""
import math
from graphics import*

def triangle():
     win = GraphWin ('Triangle',700, 700)
     # The Points of the Triangle
     point_one = win.getMouse()
     point_two = win.getMouse()
     point_three = win.getMouse()
     # Finding the Perimeter
     side_ax = point_two.getX() - point_one.getX()
     side_ay = point_two.getY() - point_one.getY()
     side_a = math.sqrt((side_ay ** 2) +(side_ax ** 2))
     side_bx = point_three.getX() - point_two.getX()
     side_by = point_three.getY() - point_two.getY()
     side_b = math.sqrt((side_by ** 2) + (side_bx ** 2))
     side_cx = point_one.getX() - point_three.getX()
     side_cy = point_one.getY() - point_three.getY()
     side_c = math.sqrt((side_cy ** 2) + (side_cx ** 2))
     perimeter = side_a + side_b + side_c
     # Finding Surface
     s = perimeter / 2
     area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
     # Drawing the Triangle
     triangle = Polygon(point_one, point_two, point_three)
     perimeter_text = ('The Perimeter is', round(perimeter, 2))
     result_perimeter = Text(Point(350, 600), perimeter_text)
     area_text = ("The Area is", round(area, 2))
     result_area = Text(Point(350, 620), area_text)
     result_perimeter.draw(win)
     result_area.draw(win)
     triangle.draw(win)


def color_shape():
     # create window
     win_width = 400
     win_height = 400
     win = GraphWin("Color Shape", win_width, win_height)
     win.setBackground("white")
     # create text instructions
     msg = "Enter color values between 0 - 255\nClick window to color shape"
     inst = Text(Point(win_width / 2, win_height - 20), msg)
     inst.draw(win)
     # create circle in window's center
     shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
     shape.draw(win)
     # redTexPt is 50 pixels to the left and forty pixels down from center
     red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
     red_text = Text(red_text_pt, "Red: ")
     red_text.setTextColor("red")
     # green_text_pt is 30 pixels down from red
     green_text_pt = red_text_pt.clone()
     green_text_pt.move(0, 30)
     green_text = Text(green_text_pt, "Green: ")
     green_text.setTextColor("green")
     # blue_text_pt is 60 pixels down from red
     blue_text_pt = red_text_pt.clone()
     blue_text_pt.move(0, 60)
     blue_text = Text(blue_text_pt, "Blue: ")
     blue_text.setTextColor("blue")
     # Entry Boxes
     red_entry_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
     red_entry_box.draw(win)
     green_entry_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
     green_entry_box.draw(win)
     blue_entry_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
     blue_entry_box.draw(win)
     red_text.draw(win)
     green_text.draw(win)
     blue_text.draw(win)
     for i in range(5):
          win.getMouse()
          r = eval(red_entry_box.getText())
          g = eval(green_entry_box.getText())
          b = eval(blue_entry_box.getText())
          shape.setFill(color_rgb(r, g, b))
     # Wait for another click to exit
     message = Text(Point(win_width / 2, 50),"Click to Close")
     message.draw(win)
     win.getMouse()
     win.close()


def process_string():
     word_of_choice = input("Feel free to insert any word")
     print(word_of_choice[0])
     print(word_of_choice[-1])
     print(word_of_choice[1:4])
     print(word_of_choice[0] + word_of_choice [-1])
     print(word_of_choice[0:3] * 10)
     for i in (word_of_choice):
          print(i)
     print(len(word_of_choice))


def processing_list():
     pt = Point(5, 10)
     values = [5, "hi", 2.5, "there", pt, "7.2"]
     print(values[1] + values[3])
     print(values[0] + values[2])
     print(values[1] * 5)
     print(values[2:5])
     print(values[2], values[3], values[0])
     print(values[2], values[0], values[5])
     print(values[2] + values[0] + float(values[5]))
     print(len(values))


def another_series():
     terms = eval(input('How many terms would you like to do?'))
     accumulator = 0
     for i in range(terms):
          series = 2 + 2 * (i % 3)
          print(series, end=" ")
          accumulator = accumulator + series
     print('sum =', accumulator)


def target():
     win = GraphWin ("Target", 500, 500)
     win.setBackground('white')
     circle_one = Circle(Point(250,250), 250)
     circle_one.setFill('white')
     circle_one.setOutline('black')
     circle_two = Circle(Point(250,250), 200)
     circle_two.setFill('black')
     circle_two.setOutline('black')
     circle_three = Circle(Point(250,250), 150)
     circle_three.setFill('blue')
     circle_three.setOutline('black')
     circle_four = Circle(Point(250,250), 100)
     circle_four.setFill('red')
     circle_four.setOutline('black')
     circle_five = Circle(Point(250,250), 50)
     circle_five.setFill('yellow')
     circle_five.setOutline('black')
     circle_one.draw(win)
     circle_two.draw(win)
     circle_three.draw(win)
     circle_four.draw(win)
     circle_five.draw(win)
     message = Text(Point(250, 250), "Click to Close")
     message.draw(win)
     win.getMouse()
     win.close()
