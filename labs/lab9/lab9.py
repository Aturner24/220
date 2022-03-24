"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    return [1,2,3,4,5,6,7,8,9]


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position-1]).isnumeric() == True:
        return True
    else:
        return False


def fill_spot(board, position, character):
    character = character.strip()
    character = character.lower()
    board[position-1] = character


def game_is_won(board):
    if str(board[0]) == str(board[1]) == str(board[2]):
        return True
    elif str(board[3]) == str(board[4]) == str(board[5]):
        return True
    elif str(board[6]) == str(board[7]) == str(board[8]):
        return True
    elif str(board[0]) == str(board[3]) == str(board[6]):
        return True
    elif str(board[1]) == str(board[4]) == str(board[7]):
        return True
    elif str(board[2]) == str(board[5]) == str(board[8]):
        return True
    elif str(board[0]) == str(board[4]) == str(board[8]):
        return True
    elif str(board[2]) == str(board[4]) == str(board[6]):
        return True
    else:
        return False

def game_over(board):
    checker = 1
    for space in board:
        if str(space).isnumeric() == True:
            checker = checker * 0
    if game_is_won(board) == True:
        return True
    elif checker == 0:
        return False
    else:
        return True


def get_winner(board):
    xtally = 0
    otally = 0
    for space in board:
        if space == "x":
            xtally = xtally + 1
        elif space == "o":
            otally = otally + 1
        else:
            pass
    if game_over(board):
        if xtally > otally:
            return "x"
        if xtally == otally:
            return "o"
    else:
        return None




def play(board):
    playagain = 'y'
    turn = 1
    print('instructions')
    while playagain[0] == 'y':
        while game_over(board) == False:
            print_board(board)
            if turn%2 == 0:
                print("o's turn")
                omove = eval(input("o's, choose a position"))
                if 1<= int(omove) <=9 and is_legal(board, omove):
                    fill_spot(board, int(omove), "o")
                else:
                    print("move is not valid, try again")
                    turn - 1

                turn = turn + 1
            else:
                print("x's turn")
                xmove = eval(input("x's, choose a position"))
                if 1 <= int(xmove) <= 9 and is_legal(board, xmove):
                    fill_spot(board, int(xmove), "x")
                else:
                    print("move is not valid, try again")
                    turn - 1
                turn = turn + 1
        if game_is_won(board) == False:
            print_board(board)
            print("it's a tie!")
        else:
            print_board(board)
            print(get_winner(board), "won!")
        playagain = input("Do you want to play again?").lower()
        if playagain[0] == "y":
            board = build_board()
            turn = 1






def main():
    play(build_board())


if __name__ == '__main__':
    main()
