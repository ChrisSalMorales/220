"""
Christopher Morales
lab_six.py

Problem: To write a program that implements the Vigenere cipher

Certification of Authenticity:
I certify that this assignment is my own work.
"""
from graphics import*


def vigenere():
    win = GraphWin("Vigenere", 500, 400)
    message_to_code = "Message to code"
    message_to_code_two = "Enter Keyword"
    message = Text(Point(100, 100), message_to_code)
    phrase = Entry(Point(258, 100), 30)
    message_two = Text(Point(100, 150), message_to_code_two)
    phrase_two = Entry(Point(225, 150), 20)
    message.draw(win)
    message_two.draw(win)
    phrase.draw(win)
    phrase_two.draw(win)
    encode_button = "Encode"
    message_three = Text(Point(250, 200), encode_button)
    message_three.draw(win)
    button = Rectangle(Point(210,180),Point(290,220))
    button.draw(win)
    win.getMouse()
    text_var = phrase.getText()
    text_var_two = phrase_two.getText()
    message_to_code_three = text_var.upper().strip()
    encoding = text_var_two.upper().strip()
    final = ""
    for i in range(len(message_to_code_three)):
        curent_message_letter = ord(message_to_code_three[i]) - 65
        key_to_use_as_code = ord(encoding[i % len(encoding)]) - 65
        newchar = chr(curent_message_letter + key_to_use_as_code + 65)
        final = final + newchar
    win.getMouse()
    message_three.undraw()
    button.undraw()
    output = Text(Point(250, 200), "Resulting Message")
    output_two = Text(Point(250, 220), final)
    output.draw(win)
    output_two.draw(win)
    click_to_close_text = Text(Point(250, 350), "Click Anywhere to Close Window")
    click_to_close_text.draw(win)
    win.getMouse()
    win.close()

vigenere()