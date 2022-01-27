"""
Andrew Turner
lab2.py

1. calculate the different means of a number
2.user will input multiple numbers and the program will output the different means of all of them
3.
    -user inputs numbers
    -the program takes the numbers and adds/multiplies them
    -program uses numbers in equations to find different means
    -program outputs means
"""
import math

def means():
    rmsaccum = 0
    harmoaccum = 0
    geoaccum = 1
    ammountofvalues = eval(input("How many values in argument?:"))
    for i in range(ammountofvalues):
        newval = eval(input("Input value:"))
        rmsaccum = (newval ** 2) + rmsaccum
        harmoaccum = 1/newval + harmoaccum
        geoaccum = newval * geoaccum
    print(round(math.sqrt(rmsaccum/ammountofvalues), 3), "\n", round(ammountofvalues/harmoaccum, 3),
    "\n", round(geoaccum ** (1/ammountofvalues), 3))