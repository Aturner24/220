"""
Name: Andrew Turner
lab12.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
def find_and_remove_first(list, value):
    list.remove((list.find(value)))

def good_input():
    userinput = eval(input("give a number between 1 and 10"))
    while userinput < 1 or userinput > 10:
        print("ERROR, USER INPUT IS OUTSIDE THE INPUT RANGE")
        userinput = eval(input("give a number between 1 and 10"))
    return userinput

def num_digits():
    number = eval(input('enter a positive integer'))
    while number > 0:
        intcount = 1
        newnum = number//10
        while newnum > 0:
             intcount = intcount + 1
             newnum = newnum//10
        print("the amount of digits is", intcount)
        number = eval(input('enter a positive integer'))

def hi_lo_game():
    from random import randint
    secret = randint(1, 100)
    guesscount = 0
    win = False
    while guesscount < 7:
        guess = eval(input("guess a number between 1 and 100"))
        while guess < 1 or guess > 100:
            print("guess outside range, try again")
            guess = eval(input("guess a number between 1 and 100"))
        guesscount = guesscount + 1
        if guess == secret:
            win = True
            print("you win in", guesscount, "guesses!")
            guesscount = 7
        elif guess > secret:
            print("Too high, guesses left:", 7 - guesscount)

        elif guess < secret:
            print("Too Low, guesses left:", 7 - guesscount)
    if not win:
        print("Sorry, you lose. The number was", secret)






