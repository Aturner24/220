"""
Andrew Turner
hw4.py



"""
from graphics import *
import math

def squares():
    win = GraphWin('Shapes', 700, 700)
    instructions = Text(Point(350, 100), 'Click to draw a square')
    instructions.draw(win)
    for square in range(6):
        click = win.getMouse()
        rect = Rectangle(Point(click.getX() - 25, click.getY() - 25), Point(click.getX() + 25, click.getY() + 25))
        rect.setFill("red")
        rect.draw(win)
    instructions.setText('Click again to close')
    win.getMouse()
def rectangle():
    win = GraphWin("Draw a funny little rectangle", 700, 500)
    firstpoint = win.getMouse()
    secondpoint = win.getMouse()
    rect = Rectangle(Point(firstpoint.getX(), firstpoint.getY()), Point(secondpoint.getX(), secondpoint.getY()))
    rect.setFill("Green")
    rect.draw(win)
    win.getMouse()
def circle():
    win = GraphWin("Draw a circle", 700, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    d = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY()) **2)
    circ = Circle(Point(p1.getX(), p1.getY()), d)
    radius = Text(Point(350, 200), ("Radius:", d))
    radius.draw(win)
    circ.draw(win)
    win.getMouse()

def pi2():
    num = eval(input("Enter number of terms to sum"))
    thenumber4lmao = 4
    piaccum = 0
    for term in range(1, num*2, 2):
        piaccum = thenumber4lmao/term + piaccum
        thenumber4lmao = thenumber4lmao * -1
    print("pi approximation: ", piaccum)
    print("accuracy", abs(piaccum-math.pi))





if __name__ == '__main__':
    pass