"""
Name: Christopher Morales
lab_nine.py

Problem: use python's built-in functions, develop while control structures,
and use boolean logic

Certification of Authenticity:
I certify that this assignment is my own work.
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def print_board(board):
    """ prints the values of board """
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
    position = position -1
    if position < 0 or position > 8 or board[position] == 'x' or board[position] == 'o':
        return False
    else:
        return True

def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    for i in range(0, 3, 1):
        if board[i] == board[i+3] == board[1+6]:
            return True
    for i in range(0, 8, 3):
        if board[i] == board[i +1] == board[i+2]:
            return True
    if board[0] == board[4] == board[6]:
        return True
    return False

def game_over(board):
    tie = True
    for i in range(9):
        if board[i] != 'x' and board[i] !='o':
            tie = False
        return winning_game(board) or tie

def get_winner(board):
    if winning_game(board):
        x_counter = 0
        o_counter = 0
        for position in board:
            if position == 'x':
                x_counter += 1
            elif position == 'o':
                o_counter += 1
        if x_counter == o_counter:
            return 'o'
        else:
            return 'x'
    else:
        return None


def play(board):
    character = 'x'
    playing = True
    while playing:
        while game_over(board) != True:
            for i in range(9):
                print_board(board)
                print("{}'s, choose a position: ".format(character))
                position = int(input(""))
                while is_legal(board, position) != True:
                    print("{}'s, choose a position: ".format(character))
                    position = int(input(""))
                fill_spot(board, position, character)

                if (winning_game(board)):
                    print_board(board)
                    print("Player", get_winner(board), "won!")
                elif (game_over(board)):
                    print_board(board)
                    print("Tie!")

                if character == 'x':
                    character = 'o'
                else:
                    character = 'x'
        cont = input("Would you like to continue playing: ")
        if cont[0] != 'y':
            playing = False

def main():
    play(build_board())

if __name__ == '__main__':
    main()
