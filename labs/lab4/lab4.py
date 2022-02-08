"""
Christopher Morales
lab4.py

Problem: To create a program that uses graphics.py to create a Valentine card

Certification of Authenticity:
I certify that this assignment is my own work.
"""
from graphics import*


def greeting_card():
    win = GraphWin("Happy Valentine's Day", 700, 700)
    win.setCoords(0,0,10,10)
    win.setBackground("white")

    body_heart = Polygon(Point(5,3),Point(7,5),Point(5,7),Point(3,5))
    body_heart.setFill('pink')
    body_heart.setOutline('pink')

    left_bump_of_heart = Circle(Point(4,6),1.4)
    left_bump_of_heart.setFill('pink')
    left_bump_of_heart.setOutline('pink')

    right_bump_of_heart = Circle(Point(6,6),1.4)
    right_bump_of_heart.setFill('pink')
    right_bump_of_heart.setOutline('pink')

    valentine_text = Text(Point(5,8), "Happy Valentine's Day")
    valentine_text.setSize(30)
    valentine_text.setFace("courier")

    arrow_body = Polygon(Point(1,5.25), Point(2,5.25), Point(2,4.75), Point(1,4.75))
    arrow_body.setOutline('black')
    arrow_body.setFill('black')

    arrow_head = Polygon(Point(2,5.5),Point(2.5,5),Point(2,4.5))
    arrow_head.setFill('black')
    arrow_head.setOutline('black')

    body_heart.draw(win)
    left_bump_of_heart.draw(win)
    right_bump_of_heart.draw(win)
    valentine_text.draw(win)
    arrow_head.draw(win)
    arrow_body.draw(win)

    for move_arrow in range(12):
        arrow_body.move(.5,0)
        arrow_head.move(.5,0)
        time.sleep(0.4)

    message = Text( Point(5,1), "Click anywhere to close")
    message.setSize((15))
    message.draw(win)
    win.getMouse()
    win.close()
