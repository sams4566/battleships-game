from pprint import pprint
import random


def start_game():
    print("Welcome to Battleships!")
    player_name = input("Please enter your name:\n")
    choose_game_type()
  
def choose_game_type():
    rows = int(input("Please type the number of rows and columns you would like to play with:\n"))
    columns = rows 
    board_one = user_board(rows, columns)
    board_two = computer_board(rows, columns)
    
    user_first_choice = users_choice(board_two)
    print_board(user_first_choice)

    computer_first_choice = computer_choice(board_one, rows, columns)
    print_board(computer_first_choice)

    for x in range(100):
        user_first_choice = users_choice(user_first_choice)
        print_board(user_first_choice)

        computer_first_choice = computer_choice(computer_first_choice, rows, columns)
        print_board(computer_first_choice)

def user_board(rows, columns):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    no_of_ships(game_board, rows, columns)
    print_board(game_board)
    print("Your board")
    return game_board

def computer_board(rows, columns):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    no_of_ships(game_board, rows, columns)
    print_board(game_board)
    print("Computer's board")
    return game_board

def no_of_ships(game_board, rows, columns):
    if rows == 4:
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"


    if rows == 5:
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"

    if rows == 6:
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"

    if rows == 7:
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"

    if rows == 8:
        game_board[random.randrange(rows)][random.randrange(columns)] = "#"

def users_choice(board_two):
    user_row = int(input("Please type the first number of your coordinate:\n"))
    user_column = int(input("Please type the second number of your coordinate:\n"))
    check_hit(board_two, user_row, user_column)
    return check_hit(board_two, user_row, user_column)

def check_hit(board_two, user_row, user_column):
    print(board_two)
    if board_two[user_row][user_column] == '.':
        board_two[user_row][user_column] = "M"
    elif board_two[user_row][user_column] == '#':
        board_two[user_row][user_column] = "X"
    return board_two

def computer_choice(board_one, rows, columns):
    user_row = int(random.randrange(rows))
    user_column = int(random.randrange(columns))
    check_hit(board_one, user_row, user_column)
    return check_hit(board_one, user_row, user_column)

def check_hit(board_one, user_row, user_column):
    print(board_one)
    if board_one[user_row][user_column] == '.':
        board_one[user_row][user_column] = "M"
    elif board_one[user_row][user_column] == '#':
        board_one[user_row][user_column] = "X"
    return board_one

        
        # while (a, b) != (c, d):

        # while game_board[rows] == '.':
        #     a = random.randrange(rows)
        #     b = random.randrange(columns)
        #     if game_board[a][b] == "#":
        #         game_board[a][b] = '#'
        #     elif game_board[a][b] == ".":
        #         game_board[a][b] = '#'
        
        # c = random.randrange(rows)
        # d = random.randrange(columns)
        # if game_board[c][d] != "#":
        #     game_board[c][d] = '#'

        # if game_board[random.randrange(rows)][random.randrange(columns)] != "#":
        #     game_board[random.randrange(rows)][random.randrange(rows)] = '#'

def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')




def main():
    start_game()

main()

# def user_choice():

# def computer_choice():

# def user_hit():

# def computer_hit():

# def user_winner():

# def computer_winner():




