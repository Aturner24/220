"""
Name: Andrew Turner
lab12.py

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