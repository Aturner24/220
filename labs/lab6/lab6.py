"""Andrew Turner
Lab 6 solution
2/24/2022

"""
from graphics import *
def vigenere():
    win = GraphWin("vigenere", 500, 500)
    win.setCoords(0, 0, 20, 20)
    win.setBackground('yellow')

    message_text = Text(Point(5, 15), "Message to code:")
    message_entry = Entry(Point(15, 15), 20)
    message_text.draw(win)
    message_entry.draw(win)

    cipher_text = Text(Point(5, 13), "Enter Keyword:")
    cipher_entry = Entry(Point(15, 13,), 20)
    cipher_entry.draw(win)
    cipher_text.draw(win)

    rect = Rectangle(Point(5, 5), Point(15, 2))
    rect.draw(win)
    rectext = Text(rect.getCenter(), "Encode")
    rectext.draw(win)

    cipherreturn = Text(Point(10, 8), '')
    win.getMouse()
    message = message_entry.getText()
    cipher = cipher_entry.getText()
    #convert message
    message = message.upper()
    message = message.replace(" ", "")
    #convert cipher
    cipher = cipher.upper()
    cipher = cipher.replace(" ", "")
    converted = ""
    for letter in range(len(message)):
        convmessage = ord(message[letter]) - 65
        convcipher = ord(cipher[letter%len(cipher)]) - 65
        newcode = (convmessage + convcipher)%26
        converted = converted + chr(newcode+65)

    cipherreturn.setText(converted)
    cipherreturn.draw(win)
    close = Text(Point(10, 6), "Click to close")
    close.draw(win)
    win.getMouse()