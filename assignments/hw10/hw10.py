"""
Name: Andrew Turner
hw10.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def fibonacci(number):
    if number < 1:
        return None
    fiblist = [1, 1, 2, 3, 5]
    if number <= len(fiblist):
        return fiblist[number - 1]
    else:
        while number > len(fiblist):
            listlen = len(fiblist)
            firstnum = fiblist[listlen - 1]
            secondnum = fiblist[listlen - 2]
            fiblist.append(firstnum + secondnum)
        return fiblist[number -1]

def double_investment(principle, rate):
    principleaccum = principle
    annual = principle * (rate + 1)
    years = 0
    while annual > principleaccum:
        annual = principleaccum * (rate + 1)
        principleaccum = principleaccum + annual
        years = years + 1
    return years

def syracuse(n):
    returnlist = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
            returnlist.append(int(n))
        else:
            n = 3*n + 1
            returnlist.append(int(n))
    return returnlist

def goldbach(n):
    pass


