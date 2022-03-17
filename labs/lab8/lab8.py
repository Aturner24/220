
"""
Andrew Turner
Lab8
3/17/2022
bumper cars


"""
from graphics import *
from random import randint
from math import *

def get_random(move_amount):
    return randint(move_amount - move_amount*2, move_amount)
def did_collide(ball, ball2): #returns boolean based if the balls touched :3
    ballcenter = ball.getCenter()
    ball2center = ball2.getCenter()
    ballradius = ball.getRadius()
    ball2radius = ball2.getRadius()
    distance = sqrt(((ball2center.getX() - ballcenter.getX())**2) + ((ball2center.getY() - ballcenter.getY())**2))
    if distance <= ballradius + ball2radius:
        return True
    else:
        return False



def hit_vertical(ball, windowheight): #also returns boolean if hit top and bottom walls
    ballcenter = ball.getCenter()
    ballradius = ball.getRadius()
    if ballcenter.getY() >= windowheight - ballradius or ballcenter.getY() <= ballradius:
        return True
    else:
        return False

def hit_horizontal(ball, windowwidth): #also returns boolean if hit left and right walls
    ballcenter = ball.getCenter()
    ballradius = ball.getRadius()
    if ballcenter.getX() >= windowwidth - ballradius or ballcenter.getX() <= ballradius:
        return True
    else:
        return False

def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))


def bumper():
    win = GraphWin("bumpercars", 500, 500)
    win.setCoords(0, 0, 500, 500)

    car1 = Circle(Point(randint(0,500), randint(0, 500)), 25)
    car1.setFill(get_random_color())
    car1.draw(win)

    car2 = Circle(Point(randint(0, 500), randint(0, 500)), 25)
    car2.setFill(get_random_color())
    car2.draw(win)

    movex1 = get_random(2)
    movey1 = get_random(2)

    movex2 = get_random(2)
    movey2 = get_random(2)

    while not win.checkMouse():
        car1.move(movex1, movey1)
        car2.move(movex2, movey2)

        if did_collide(car1, car2) is True:
            movex1 = movex1 * -1
            movex2 = movex2 * -1
            movey1 = movey1 * -1
            movey2 = movey2 * -1
        if hit_vertical(car1, win.getHeight()) is True:
            movey1 = movey1 * -1
        if hit_vertical(car2, win.getHeight()) is True:
            movey2 = movey2 * -1
        if hit_horizontal(car1, win.getWidth()) is True:
            movex1 = movex1 * -1
        if hit_horizontal(car2, win.getWidth()) is True:
            movex2 = movex2 * -1
        time.sleep(.05)
    win.close()