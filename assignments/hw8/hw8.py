"""
Name:Andrew Turner
hw8.py
I certify that this assignment is entirely my own work.

"""

from graphics import *
from math import *

def add_ten(nums):
    numsaccum = []
    for number in nums:
        numsaccum.append(number + 10)
    nums = numsaccum
    return nums

def square_each(nums):
    numsaccum = []
    for number in nums:
        numsaccum.append(number**2)
    nums = numsaccum
    return nums
def sum_list(nums):
    sumaccumulator = 0
    for number in nums:
        sumaccumulator = sumaccumulator + number
    return sumaccumulator

def to_numbers(nums):
    numsaccum = []
    for string in nums:
        numsaccum.append(eval(string))
    nums = numsaccum
    return nums

def sum_of_squares(nums):
    listofnumbers = to_numbers(nums)
    squared = square_each(listofnumbers)
    return sum_list(squared)



def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year%400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = sqrt((center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = sqrt((center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light blue")
    circle_two.draw(win)
    text = Text(Point(5, 3), "the circles overlap")
    if did_overlap(circle_one, circle_two) is True:
        text.draw(win)
    else:
        text.setText('the circles do not overlap')
        text.draw(win)
    Text(Point(5, 2), "click to end program").draw(win)
    win.getMouse()
    win.close()



def did_overlap(circle_one, circle_two):
    center = circle_one.getCenter()
    center2 = circle_two.getCenter()
    text = Text(Point(3, 5), "The circles overlap")
    distance = sqrt((center2.getX() - center.getX()) ** 2 + (center2.getY() - center.getY()) ** 2)
    if distance < circle_one.getRadius() + circle_two.getRadius():
        return True
    else:
        return False

if __name__ == '__main__':
    pass
