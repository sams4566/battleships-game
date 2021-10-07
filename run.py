from pprint import pprint
import random

SHIP = '#'
HIT = 'X'
MISS = 'M'


def start_game():
    print("Welcome to Battleships!")
    player_name = input("Please enter your name:\n")
    choose_game_type()
    
def choose_game_type():
    rows = int(input("Please type the number of rows you would like to play with:\n"))
    columns = int(input("Please type the number of columns you would like to play with:\n"))
    board = user_board(rows, columns)
    print_board(board)

def user_board(rows, columns):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    no_of_ships(game_board, rows, columns)
    print(game_board)
    return game_board

def no_of_ships(game_board, x, y):
    game_board[random.randrange(x)][random.randrange(y)] = "@"

def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')

# def add_ship(x, y, type="computer"):
#     ships.append((x, y))
#     board[x][y] = "@"


def computer_board(rows, columns):
    game_board = [["." for x in range(rows)] for y in range(columns)]
    for row in game_board:
        print(" ".join(row))

def main():
    start_game()

main()


# def user_board(size):
#     game_board = [["." for x in range(size)] for y in range(size)]
#     for row in game_board:
#             print(" ".join(row))

# def user_choice():

# def computer_choice():

# def user_hit():

# def computer_hit():

# def user_winner():

# def computer_winner():




