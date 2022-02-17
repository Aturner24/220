from math import *
from graphics import *

def triangle():
    wintriangle = GraphWin("Triangle", 500, 500)
    wintriangle.setCoords(0,0,500,500)
    p1 = wintriangle.getMouse()
    p2 = wintriangle.getMouse()
    p3 = wintriangle.getMouse()
    tri = Polygon(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()), Point(p3.getX(), p3.getY()))
    tri.draw(wintriangle)

    Text(Point(250, 50), "Click to close").draw(wintriangle)
    wintriangle.getMouse()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

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

    red_text_entry_pt = red_text_pt.clone()
    red_text_entry_pt.move(60, 0)
    red_text_entry = Entry(red_text_entry_pt, 8)
    red_text_entry.draw(win)
    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    green_text_entry_pt = green_text_pt.clone()
    green_text_entry_pt.move(60, 0)
    green_text_entry = Entry(green_text_entry_pt, 8)
    green_text_entry.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    blue_text_entry_pt = blue_text_pt.clone()
    blue_text_entry_pt.move(60, 0)
    blue_text_entry = Entry(blue_text_entry_pt, 8)
    blue_text_entry.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    #color shape 5 times
    win.getMouse()
    for click in range(5):
        redvalue = eval(red_text_entry.getText())
        greenvalue = eval(green_text_entry.getText())
        bluevalue = eval(blue_text_entry.getText())
        shape.setFill(color_rgb(redvalue, greenvalue, bluevalue))
        win.getMouse()

    inst.setText("click to close")
    win.getMouse()
    win.close()
def process_string():
    dastring = input("Input a string:")
    print('1.', dastring[0])
    print('2.', dastring[-1])
    print('3.', dastring[2:5])
    print('4.', dastring[0] + dastring[-1])
    print('5.', dastring[0:3]*10)
    print('6.')
    for letter in dastring:
        print(letter, '\n')
    print('7.', len(dastring))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4], values[0]
    print(x)
    x = values[0], values[2], float(values[5])
    print(x)
    x = values[0] + values[2] + eval(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series():
    terms = eval(input("terms:"))
    accumulator = 0
    for num in range(1,terms+1):
        rep = (((num - 1) % 3) +1) * 2
        accumulator = rep + accumulator
        print(rep, end=" ")
    print("\nsum:", accumulator)

def target():
    win = GraphWin("Color Shape", 400, 400)
    rad = 240
    center = Point(200,200)
    radaccumulator = 40
    listofcolors = ["white", 'black', 'blue', 'red', 'yellow']
    for circ in range(5):
        newcir = Circle(center, rad-radaccumulator)
        radaccumulator = radaccumulator + 40
        newcir.setFill(listofcolors[circ])
        newcir.draw(win)
    Text(Point(200, 375), "Click to close").draw(win)
    win.getMouse()


