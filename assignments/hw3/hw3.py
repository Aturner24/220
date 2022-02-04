"""
Name: Andrew Turner
hw3.py


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def average():
    accumulator = 0
    numberof = eval(input("How many values do you plan on entering?"))
    for value in range(numberof):
        numba = eval(input("Input value:"))
        accumulator = numba + accumulator
    print(accumulator/numberof)


def tip_jar():
    tipaccumulator = 0
    for person in range(5):
        tip = eval(input("how much would you like to donate?"))
        tipaccumulator = tipaccumulator + tip
    print("total tips:", tipaccumulator)


def newton():
    number = eval(input("what number would you like to square root?"))
    times = eval(input("how many times would you like to improve the approximation?"))
    approx = number
    for i in range(times):
        approx = (approx + number/approx)/2
    print("the square root is approximately", approx)



def sequence():
    terms = eval(input("How many terms would you like?"))
    for i in range(1, terms+1):
        print(i - abs(i%2 - 1), end=" ")





def pi():
    terms = eval(input("How many terms in the series?"))
    piaccum = 1
    for i in range(1, terms+1):
        numaccum = (i+abs(i%2))
        denomaccum = (i+abs(i%2-1))
        piaccum = numaccum/denomaccum * piaccum
    print(piaccum*2)


if __name__ == '__main__':
    pass
