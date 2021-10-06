from pprint import pprint
from random import randint


def start_game():
    print("Welcome to Battleships!")
    player_name = input("Please enter your name:\n")
    choose_game_type()
    

def choose_game_type():
    rows = int(input("Please type the number of rows you would like to play with:\n"))
    columns = int(input("Please type the number of columns you would like to play with:\n"))
    computer_board(rows, columns)

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




