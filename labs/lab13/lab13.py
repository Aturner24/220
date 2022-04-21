"""
Name: Andrew Turner
lab13.py
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

import time
def trade_alert(filename):
    reading = open(filename, 'r')
    timer = 0
    for trade in reading.read().split():
        timer = timer + 1
        if int(trade) > 830:
            print("Warning, Trades over 830 in 1 second at:", timer, "seconds")
        elif int(trade) == 500:
            print("Alert, exactly 500 trades in 1 second at:", timer, 'seconds')
    reading.close()
