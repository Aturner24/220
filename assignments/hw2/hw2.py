"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upperbound = eval(input("upper bound:"))
    multiples = upperbound // 3
    x = 0
    y = 0
    for i in range(multiples):
        x = x + 3
        y = y + x
    print(y)

def multiplication_table():
    for line in range(10):
        for row in range(10):
            print((line+1) * (row+1), end='\t')
        print()

def triangle_area():
  sidea = eval(input("Side length of A"))
  sideb = eval(input("Side length of B"))
  sidec = eval(input("Side length of C"))
  s = (sidea + sideb + sidec)/2
  print("The area of the given triangle is:", math.sqrt(s*(s-sidea)*(s-sideb)*(s-sidec)))




def sum_squares():
    lr = eval(input("Lower Range:"))
    ur = eval(input("Upper Range:"))
    result = 0
    for multiple in range(lr, ur+1 ):
        result = (multiple**2) + result
    print(result)



def power():
    base = eval(input("Input base:"))
    exponent = eval(input("Input exponent:"))
    print(base ** exponent)

if __name__ == '__main__':
    pass
