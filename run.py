import random


def start_game():
    print('-' * 30)
    print("Welcome to Battleships!")
    print('-' * 30)
    user_name = input("Please enter your name:\n")
    choose_game_type(user_name)


def no_of_rows():
    while True:
        rows1 = input("Board size: Please choose a number between 3 - 6:\n")
       
        if check_data_input(rows1):
            break
        
    rows1 = int(rows1)
    return rows1

def check_data_input(rows1):             
    try:
        if int(rows1) < 3 or int(rows1) > 6:
            raise ValueError(
                f"Invalid entry"
            )
    except ValueError as e:
        print(f"Invalid entry")
        return False

    return True            
  
def choose_game_type(user_name):
    rows = no_of_rows()
    columns = rows
    board_one = user_board(rows, columns, user_name)
    board_two = computer_board(rows, columns)
    SCORE1 = 0
    SCORE2 = 0
    user_row1 = 0
    user_column1 = 0
    user_row2 = 0
    user_column2 = 0
    
    for x in range(100):
        board_one, SCORE2, user_row2, user_column2 = computer_choice(board_one, rows, columns, SCORE2)
        board_two, SCORE1, user_row1, user_column1 = users_choice(board_two, rows, SCORE1)

        print_board(board_one, rows)
        print(f"{user_name}\'s ships")
        print(f"Computer shot at ({user_row2}, {user_column2})")

        print_board2(board_two, rows)
        print("Computer's ships")
        print(f"{user_name} shot at ({user_row1}, {user_column1})\n")

        print('\u0332'.join('Current Scores:'))
        print(f"{user_name}\'s Score: {SCORE1}/{rows * 2} ships sunk")
        print(f"Computer's score: {SCORE2}/{rows * 2} ships sunk\n")

        if SCORE1 == rows * 2 and SCORE2 == rows * 2:
            print("It's a Draw!")
            start_game()

        if SCORE1 == rows * 2:
            print("You Win!")
            start_game()

        if SCORE2 == rows * 2:
            print("Computer Wins!")
            start_game()


def user_board(rows, columns, user_name):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    for x in range(rows * 2):
        calculate_ships(game_board, rows, columns)
    print_board(game_board, rows)
    print(f"{user_name}\'s board")
    return game_board

def computer_board(rows, columns):
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    for x in range(rows * 3):
        calculate_ships(game_board, rows, columns)
    print_board2(game_board, rows)
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
        user_row1 = input("Please choose a row:\n")
        user_column1 = input("Please choose a column:\n")

        if correct_input1(user_row1, rows):
            if correct_input2(user_column1, rows):
                if board_two[int(user_row1)][int(user_column1)] == "X":
                    print("You have already chosen that coordinate!")
                elif board_two[int(user_row1)][int(user_column1)] == "~":
                    print("You have already chosen that coordinate!")
                elif board_two[int(user_row1)][int(user_column1)] == ".":
                    break
                elif board_two[int(user_row1)][int(user_column1)] == "#":
                    break

    user_row1 = int(user_row1)
    user_column1 = int(user_column1)

    if board_two[user_row1][user_column1] == ".":
        board_two[user_row1][user_column1] = "~"
        
    elif board_two[user_row1][user_column1] == '#':
        board_two[user_row1][user_column1] = "X"
        SCORE1 = SCORE1 + 1
    return board_two, SCORE1, user_row1, user_column1
        
def correct_input1(user_row1, rows):
    try:
        if int(user_row1) >= rows or int(user_row1) < 0:
            raise ValueError(
                f"Entries must be between 0 - {rows - 1}"
            )
    except ValueError as e:
        print(f"Entries must be between 0 - {rows - 1}")
        return False
    
    return True

def correct_input2(user_column1, rows):
    try:
        if int(user_column1) >= rows or int(user_column1) < 0:
            raise ValueError(
                f"Entries must be between 0 - {rows - 1}"
            )
    except ValueError as e:
        print(f"Entries must be between 0 - {rows - 1}")
        return False
    
    return True

def computer_choice(board_one, rows, columns, SCORE2):
    while True:
        user_row2 = int(random.randrange(rows))
        user_column2 = int(random.randrange(columns))

        if board_one[int(user_row2)][int(user_column2)] == ".":
            break
        elif board_one[int(user_row2)][int(user_column2)] == "#":
            break

    if board_one[user_row2][user_column2] == ".":
        board_one[user_row2][user_column2] = "~"
        
    elif board_one[user_row2][user_column2] == '#':
        board_one[user_row2][user_column2] = "X"
        SCORE2 = SCORE2 + 1
    return board_one, SCORE2, user_row2, user_column2

def print_board(board, rows):

    print(' ', end=" ")
    print(f'{nums_top(rows)}')
    
    for row, x in zip(board, range(rows)):
        print(f'{x}| ' + '   '.join(row) + ' |')

    print(' ' + ' ‾' * rows * 2)

def print_board2(board, rows): 

    print(' ', end=" ")
    print(f'{nums_top(rows)}')

    for row, x in zip(board, range(rows)):
        row_copy = [row_char.replace("#", ".") for row_char in row]
        print(f'{x}| ' + '   '.join(row_copy) + ' |')

    print(' ' + ' ‾' * rows * 2)

def nums_top(rows):
    for x in range(rows):
        print(f'_{rows - (rows - x)}_', end=" ")
    return ''

start_game()





