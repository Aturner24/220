"""
Name: Andrew Turner
hw1.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter Length"))
    width = eval(input('Enter Width'))
    height = eval(input('Enter Height'))
    volume = length * width * height
    print('Volume =', volume)


def shooting_percentage():
    shots_total = eval(input("Enter the player's total shots:"))
    shots_made = eval(input("Enter how many shots the player made:"))
    shotpercent = (shots_made/shots_total) * 100
    print("Shooting Percentage:", shotpercent, "%")


def coffee():
    pounds = eval(input("How many pounds of coffee do you want?"))
    price = (pounds * 11.36) +1.50
    print("You're total is: $", price)


def kilometers_to_miles():
    kilos = eval(input("How many kilometers did you travel?"))
    miles = .62137 * kilos
    print("that's", miles," miles!")



if __name__ == '__main__':
    pass
