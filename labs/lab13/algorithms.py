"""
Name: Andrew Turner
lab13.py
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
def read_data(filename):
    readfile = open(filename, 'r')
    return readfile.read().split()

def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i = i + 1
    return False

def selection_sort(values):
    for value in range(len(values)):
        mindex = value
        for i in range(value+1, len(values)):
            if values[i] < values[value]:
                mindex = i
        holder=values[mindex]
        values[mindex] = values[value]
        values[value] = holder
    return values

def calc_area(rect):
    height = abs(rect.getP1().getY() - rect.getP2().getY())
    length = abs(rect.getP1().getX() - rect.getP2().getX())
    return height * length
def rect_sort(rectangles):
    for value in range(len(rectangles)):
        mindex = value
        for i in range(value+1, len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[value]):
                mindex = i
        holder=rectangles[mindex]
        rectangles[mindex] = rectangles[value]
        rectangles[value] = holder
    return rectangles



