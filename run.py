from pprint import pprint
from random import randint

def computer_board(size):
    game_board = [["." for x in range(size)] for y in range(size)]
    for row in game_board:
            print(" ".join(row))

def user_board(size):
    game_board = [["." for x in range(size)] for y in range(size)]
    for row in game_board:
            print(" ".join(row))

# def user_choice():

# def computer_choice():

# def user_hit():

# def computer_hit():

# def user_winner():

# def computer_winner():

def main():
    computer_board(10)
    user_board(10)

main()




