"""Andrew Turner
Lab 10 solution
3/31/2022

"""
from graphics import *
from button import Button
from door import Door
if __name__ == '__main__':
    win = GraphWin("doors", 400, 500)
    door1 = Door(Rectangle(Point(100, 150), Point(300, 450)), "closed")
    door1.color_door('red')
    door1.draw(win)

    exit = Button(Rectangle(Point(100, 15), Point(300, 75)), "Exit")
    exit.color_button('yellow')
    exit.draw(win)
    click = win.getMouse()
    while not exit.is_clicked(click):
        if door1.is_clicked(click):
            if door1.get_label() == "closed":
                door1.open("green", "open")
            else:
                door1.close("red", "closed")
        click = win.getMouse()