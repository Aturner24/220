"""
Name: Andrew Turner
<hw6>.py


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    print("that is ${0:0.2f}".format(eval(input("enter an integer"))))

def encode():
    message = input("Enter a message to be encoded")
    key = eval(input("Enter a key to encode the message with"))
    codedmessage = ''
    for letter in message:
        c = ord(letter) + key
        codedmessage = codedmessage + chr(c)
    print(codedmessage)


def sphere_area(radius):
    print(4*math.pi*(radius**2))


def sphere_volume(radius):
    print(4/3*math.pi*(radius**3))


def sum_n(number):
    sumaccum = 0
    for n in range(1, number+1):
        sumaccum = sumaccum + n
    print('total:',sumaccum)


def sum_n_cubes(number):
    cubeaccum = 0
    for n in range(1, number+1):
        cubeaccum = cubeaccum + n**3
    print(cubeaccum)


def encode_better():
    message = input("input message to encode")
    cipher = input("input cipher")
    newmessage = ''
    for place in range(len(message)):
        switch = ord(message[place]) - 65
        ciphswitch = ord(cipher[place % len(cipher)]) - 65
        newmessagecode = (switch + ciphswitch) % 58
        newmessage = newmessage + chr(newmessagecode + 65)
    print(newmessage)

if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
