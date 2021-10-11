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
    SCORE1 = 0
    SCORE2 = 0
    user_row1 = 0
    user_column1 = 0
    
    for x in range(100):
        board_one, SCORE2 = computer_choice(board_one, rows, columns, SCORE2)
        board_two, SCORE1 = users_choice(board_two, rows, SCORE1)
    

        print(f"This is your score:{SCORE1}")
        print(f"This is the Computers score:{SCORE2}")

        print_board(board_one, rows)
        print("Your Board")
        print(f"Computer chose coordinates {user_row1}, {user_column1}")


        print_board2(board_two, rows)
        print("Computer's Board")

        print(f"This is your score:{SCORE1}")
        print(f"This is the Computers score:{SCORE2}")

        if SCORE1 == rows:
            print("You Win!")
            start_game()

        if SCORE2 == rows:
            print("Computer Wins!")
            start_game()


def user_board(rows, columns):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    for x in range(12):
        calculate_ships(game_board, rows, columns)
    print_board(game_board, rows)
    print("Your board")
    return game_board

def computer_board(rows, columns):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    for x in range(12):
        calculate_ships(game_board, rows, columns)
    print_board(game_board, rows)
    print("Computer's board")
    return game_board

def calculate_ships(game_board, rows, columns):
    a = random.randrange(rows)
    b = random.randrange(columns)
    if game_board[a][b] == ".":
        game_board[a][b] = "#"
    elif game_board[a][b] == "#":
        calculate_ships(game_board, rows, columns)
    return game_board

def users_choice(board_two, rows, SCORE1):
    
    while True:
        user_row1 = input("Please type the first number of your coordinate:\n")

        if correct_input1(user_row1, rows):
            break

    while True:
        user_column1 = input("Please type the second number of your coordinate:\n")

        if correct_input2(user_column1, rows):
            break

    user_row1 = int(user_row1)
    user_column1 = int(user_column1)

    # if user_row1 < rows and user_row1 >= 0 and user_column1 < rows and user_column1 >= 0:
    print("Hello there")
    if board_two[user_row1][user_column1] == ".":
        board_two[user_row1][user_column1] = "M"
        
    elif board_two[user_row1][user_column1] == '#':
        board_two[user_row1][user_column1] = "X"
        SCORE1 = SCORE1 + 1
        print(f"This is the correct {SCORE1}")
        
        # SCORE1 = scores1(SCORE1, rows)
    elif board_two[user_row1][user_column1] == "M":
        print("You have already chosen that coordinate, please choose again!")
        SCORE1 = SCORE1
        users_choice(board_two, rows, SCORE1)
        
    elif board_two[user_row1][user_column1] == "X":
        print("You have already chosen that coordinate, please choose again!")
        SCORE1 = SCORE1
        users_choice(board_two, rows, SCORE1)
    return board_two, SCORE1
            

    # elif user_row1 != int or float or user_column1 != int or float:
    #     print(f"Please choose a number between 0 - {rows - 1}")
    #     SCORE1 = SCORE1
    #     users_choice(board_two, rows, SCORE1)

def correct_input1(user_row1, rows):
    try:
        if int(user_row1) > rows or int(user_row1) < 0:
            raise ValueError(
                f"Please choose a number between 0 - {rows - 1}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please choose a number between 0 - {rows - 1}\n")
        return False
    
    return True

def correct_input2(user_column1, rows):
    try:
        if int(user_column1) > rows or int(user_column1) < 0:
            raise ValueError(
                f"Please choose a number between 0 - {rows - 1}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please choose a number between 0 - {rows - 1}\n")
        return False
    
    return True

def computer_choice(board_one, rows, columns, SCORE2):
    user_row = int(random.randrange(rows))
    user_column = int(random.randrange(columns))
    if board_one[user_row][user_column] == '.':
        board_one[user_row][user_column] = "M"
    elif board_one[user_row][user_column] == '#':
        board_one[user_row][user_column] = "X"
        SCORE2 = scores2(SCORE2, rows)
    elif board_one[user_row][user_column] == "M":
        computer_choice(board_one, rows, columns, SCORE2)
    elif board_one[user_row][user_column] == "X":
        computer_choice(board_one, rows, columns, SCORE2)
    return board_one, SCORE2

def scores2(SCORE2, rows):
    SCORE2 = SCORE2 + 1
    return SCORE2

def print_board(board, rows):
    print(' ', end=" ")
    print(f'{nums_top(rows)}')
    
    for row, x in zip(board, range(rows)):
        print(f'{x}| ' + '   '.join(row) + ' |')

    print(' ' + ' ‾' * rows * 2)

def print_board2(board, rows):

    print("The is print_board2") 

    print(' ', end=" ")
    print(f'{nums_top(rows)}')

    for x in range(rows):
        for y in range(rows):
            if board[x][y] == "#":
                board[x][y] = "@"

    for row, x in zip(board, range(rows)):
        print(f'{x}| ' + '   '.join(row) + ' |')

    print(' ' + ' ‾' * rows * 2)
    
def nums_top(rows):
    for x in range(rows):
        print(f'_{rows - (rows - x)}_', end=" ")
    return ''

    # for x in range(rows):
    #     for y in range(rows):
    #         if board[x][y] == ".":
    #             board[x][y] = "#"



def main():
    start_game()

main()

# def user_choice():

# def computer_choice():

# def user_hit():

# def computer_hit():

# def user_winner():

# def computer_winner():




