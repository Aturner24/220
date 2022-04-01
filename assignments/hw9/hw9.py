"""
Name: Andrew Turner
hw9.py

Problem: it's hangman lol

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from random import *
from graphics import *

def get_words(file_name):
    wordlist = []
    dawords = open(file_name, 'r')
    for line in dawords.readlines():
        fixword = line.removesuffix('\n')
        wordlist.append(fixword)
    dawords.close()
    return wordlist




def get_random_word(words):
    randompick = randint(0, len(words))
    return words[randompick]


def letter_in_secret_word(letter, secret_word):
    if secret_word.count(letter) > 0:
        return True
    else:
        return False

def already_guessed(letter, guesses):
    counter = 0
    for guess in guesses:
        if letter == guess:
            counter = counter+1
    if counter >= 1:
        return True
    else:
        return False





def make_hidden_secret(secret_word, guesses):
    hidden = list('_') * len(secret_word)
    for guess in guesses:
        for letter in range(len(secret_word)):
            if guess == secret_word[letter]:
                hidden[letter] = guess
    return " ".join(hidden)

def won(guessed):
    if guessed.count('_') == 0:
        return True
    else:
        return False


def play_graphics(secret_word):
    win = GraphWin('Hangman', 500, 500)
    win.setCoords(0, 0, 100, 100)

    #THE HANGED MAN
    Line(Point(25, 70), Point(25, 80)).draw(win)
    Line(Point(25, 80), Point(35, 80)).draw(win)
    Line(Point(35, 80), Point(35, 30)).draw(win)

    head = Circle(Point(25, 65), 5)
    body = Line(Point(25, 60), Point(25, 40))
    larm = body.clone()
    larm.move(-5, 0)

    rarm = body.clone()
    rarm.move(5,0)

    lleg = body.clone()
    lleg.move(-3, -20)

    rleg = body.clone()
    rleg.move(3, -20)

    hanglist = [head, body, rarm, larm, rleg, lleg]
    guesslist = []

    #GAME
    guesslist = []
    wronglist = []
    playing = True
    winnertext = Text(Point(50, 50), "WINNER")
    while playing:
        hidden = make_hidden_secret(secret_word, guesslist)
        hiddentext = Text(Point(70, 70), hidden)
        hiddentext.draw(win)

        guesslistdisplay = Text(Point(50, 35), guesslist)
        guesslistdisplay.draw(win)

        guess = Entry(Point(50 ,25), 5)
        guess.draw(win)
        win.getMouse()

        if not already_guessed(guess.getText(), guesslist):
            guesslist.append(guess.getText().lower())
            if secret_word.count(guess.getText()) == 0:
                wronglist.append(guess.getText())
                hanglist[len(wronglist)-1].draw(win)
        if won(hidden):
            guess.undraw()
            winnertext.draw(win)
            playing = False
        if len(guesslist) > 6:
            guess.undraw()
            winnertext.setText("LOSER")
            winnertext.draw(win)
            playing = False
        guesslistdisplay.undraw()
        hiddentext.undraw()
    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guesslist = []
    win = False
    playing = True
    remainingguess = 6
    while playing:
        print(make_hidden_secret(secret_word, guesslist))
        print("already guessed:", guesslist)
        print("guesses remaining:", remainingguess)
        playerguess = input("guess a letter:")
        if already_guessed(playerguess, guesslist):
            print("already guessed:", guesslist)
            remainingguess = remainingguess + 1
        else:
            guesslist.append(playerguess)

        hidden = make_hidden_secret(secret_word, guesslist)
        if won(hidden):
            print("winner! \n", secret_word)
            playing = False
            win = True
        remainingguess = remainingguess - 1
        if remainingguess == 0:
            playing = False
    if not win:
        print("LOSER \n", secret_word)
        playing = False



if __name__ == '__main__':
    pass
    #play_command_line(secret_word)

    # play_graphics(secret_word)
