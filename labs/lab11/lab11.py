"""
Name: Andrew Turner
lab11.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import *


def three_door_game():
    win = GraphWin('3 doors game', 650, 550)
    door1 = Door(Rectangle(Point(50, 150), Point(200, 450)), "Door 1")
    door1.color_door('brown')
    door1.draw(win)

    door2 = Door(Rectangle(Point(250, 150,), Point(400, 450)), 'Door 2')
    door2.color_door('brown')
    door2.draw(win)

    door3 = Door(Rectangle(Point(450, 150,), Point(600, 450)), 'Door 3')
    door3.color_door('brown')
    door3.draw(win)

    exit = Button(Rectangle(Point(50, 15), Point(200, 75)), "Exit")
    exit.color_button('yellow')
    exit.draw(win)

    instructions = Text(Point(325, 500), "Pick a door")
    instructions.draw(win)

    wincount = 0
    losecount = 0
    losescore = Rectangle(Point(450, 15), Point(525, 75))
    winscore = Rectangle(Point(525, 15), Point(600, 75))
    winscore.draw(win)
    losescore.draw(win)

    wintext = Text(winscore.getCenter(), wincount)
    losetext = Text(losescore.getCenter(), losecount)
    wintext.draw(win)
    losetext.draw(win)

    click = win.getMouse()
    doorlist = [door1, door2, door3]
    while not exit.is_clicked(click):
        secretdoor = randint(1, 3)
        for door in doorlist:
            if secretdoor == doorlist.index(door) + 1:
                door.set_secret(True)
            else:
                door.set_secret(False)

        for door in doorlist:
            if door.is_clicked(click):
                if door.is_secret():
                    wincount = wincount + 1
                    wintext.setText(wincount)
                    door.open("green", "WIN")
                else:
                    losecount = losecount + 1
                    losetext.setText(losecount)
                    door.open("red", "LOSE")
                    for unopened in doorlist:
                        if unopened.is_secret():
                            unopened.open("green", "LOSE")
        instructions.setText("Click to play again")
        click = win.getMouse()
        if exit.is_clicked(click):
            win.close()
        else:
            door1.close("brown", "Door 1")
            door2.close("brown", "Door 2")
            door3.close("brown", "Door 3")
            instructions.setText("Pick a door")
            click = win.getMouse()




