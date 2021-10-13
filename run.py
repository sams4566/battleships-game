import random


def start_game():
    """
    Start the game by collecting the users name.
    """
    print("-" * 36)
    print("Welcome to Battleships!")
    print("-" * 36)
    user_name = input("Please enter your name:\n")
    run_game(user_name)


def run_game(user_name):
    """
    Once the number of rows is returned and the players boards are
    created, a 'for' loop is created to facilitate the user and
    computer's choices until all the ships are sunk.

    Once a winner is established a message is produced and the game
    restarts.
    """
    rows = no_of_rows()
    columns = rows
    board_one = user_board(rows, columns, user_name)
    board_two = computer_board(rows, columns)
    print("Key:")
    print("# = Ship")
    print("X = Hit")
    print("~ = Miss")
    print("Coordinate = (row, column)")
    print("-" * 36)
    SCORE1 = 0
    SCORE2 = 0
    user_row1 = 0
    user_column1 = 0
    user_row2 = 0
    user_column2 = 0

    for x in range(100):
        board_one, SCORE2, user_row2, user_column2 = computer_choice(
            board_one, rows, columns, SCORE2
        )
        board_two, SCORE1, user_row1, user_column1 = users_choice(
            board_two, rows, SCORE1
        )

        print("-" * 36)
        print(f"{user_name}'s board")
        print(f"Computer shot at ({user_row2}, {user_column2})")
        print_user_board(board_one, rows)

        print("Computer's board")
        print(f"{user_name} shot at ({user_row1}, {user_column1})")
        print_computer_board(board_two, rows)

        print("-" * 36)
        print(f"{user_name}'s Score: {SCORE1}/{rows * 2 - 2} ships sunk")
        print(f"Computer's score: {SCORE2}/{rows * 2 - 2} ships sunk")
        print("-" * 36)

        if SCORE1 == rows * 2 - 2 and SCORE2 == rows * 2 - 2:
            print("There is no winner, both have been defeated!")
            start_game()
        if SCORE1 == rows * 2 - 2:
            print("Congratulations, you have defeated the enemy!")
            start_game()
        if SCORE2 == rows * 2 - 2:
            print("Game over, you have lost the battle!")
            start_game()


def no_of_rows():
    """
    The while loop determines whether the users input is between the max
    and min board sizes of 3 and 5. The number of rows is then returned
    to the run_game function.
    """
    while True:
        rows1 = input("Board size: choose 3, 4 or 5:\n")

        if check_rows_input(rows1):
            break
    rows1 = int(rows1)
    return rows1


def check_rows_input(rows1):
    """
    Error messages are provided in the console if the inputed entries
    are not between 3 and 5.
    """
    try:
        if int(rows1) < 3 or int(rows1) > 5:
            raise ValueError(f"Invalid entry")
    except ValueError as e:
        print(f"Invalid entry")
        return False
    return True


def user_board(rows, columns, user_name):
    """
    The user's board is created using a 'for' loop and the
    ships are added to the board through the calculate_ships
    function. The user's board is then returned to the
    run_game function.
    """
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    for x in range(rows * 2 - 2):
        calculate_ships(game_board, rows, columns)
    print("-" * 36)
    print(f"{user_name}'s board")
    print_user_board(game_board, rows)
    return game_board


def computer_board(rows, columns):
    """
    The computer's board is created using a 'for' loop and the
    ships are added to the board through the calculate_ships
    function. The computer's board is then returned to the
    run_game function.
    """
    game_board = []
    for y in range(columns):
        game_board_row = []
        for x in range(rows):
            game_board_row.append(".")
        game_board.append(game_board_row)
    for x in range(rows * 2 - 2):
        calculate_ships(game_board, rows, columns)
    print("Computer's board")
    print_computer_board(game_board, rows)
    return game_board


def calculate_ships(game_board, rows, columns):
    """
    A ships ('#') is added to the game board and the new game board
    is returned
    """
    a = random.randrange(rows)
    b = random.randrange(columns)
    if game_board[a][b] == ".":
        game_board[a][b] = "#"
    elif game_board[a][b] == "#":
        calculate_ships(game_board, rows, columns)
    return game_board


def computer_choice(board_one, rows, columns, SCORE2):
    """
    The computer keeps choosing a random number until the coordinates
    haven't been entered before. Once the 'while' look is broken,
    a hit ('X') or miss ('~') is added to the users board and
    subsequently returned to the 'for' loop in the run_game function.

    If the computers choice is a hit ('X') the computers score is
    incremented by 1 and returned to the 'for' loop in the run_game
    function.
    """
    while True:
        user_row2 = int(random.randrange(rows))
        user_column2 = int(random.randrange(columns))

        if board_one[int(user_row2)][int(user_column2)] == ".":
            break
        elif board_one[int(user_row2)][int(user_column2)] == "#":
            break
    if board_one[user_row2][user_column2] == ".":
        board_one[user_row2][user_column2] = "~"
    elif board_one[user_row2][user_column2] == "#":
        board_one[user_row2][user_column2] = "X"
        SCORE2 = SCORE2 + 1
    return board_one, SCORE2, user_row2, user_column2


def users_choice(board_two, rows, SCORE1):
    """
    The user keeps choosing a number until the coordinates
    haven't been entered before. Once the 'while' look is broken,
    a hit ('X') or miss ('~') is added to the computers board and
    subsequently returned to the 'for' loop in the run_game function.

    If the users choice is a hit ('X') the users score is
    incremented by 1 and returned to the 'for' loop in the run_game
    function.
    """
    while True:
        user_row1 = input("Please choose a row:\n")
        user_column1 = input("Please choose a column:\n")

        if correct_input(user_row1, rows):
            if correct_input(user_column1, rows):
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
    elif board_two[user_row1][user_column1] == "#":
        board_two[user_row1][user_column1] = "X"
        SCORE1 = SCORE1 + 1
    return board_two, SCORE1, user_row1, user_column1


def correct_input(user_row, rows):
    """
    Error messages are provided if the user enters a value
    that is not between 0 and the number of rows - 1
    """
    try:
        if int(user_row) >= rows or int(user_row) < 0:
            raise ValueError(f"Entries must be between 0 - {rows - 1}")
    except ValueError as e:
        print(f"Entries must be between 0 - {rows - 1}")
        return False
    return True


def print_user_board(board, rows):
    """
    The users board is printed out in a readable way with spaces between the
    dots and numbers along the side.
    """
    print(" ", end=" ")
    print(f"{nums_top(rows)}")

    for row, x in zip(board, range(rows)):
        print(f"{x}| " + "   ".join(row) + " |")
    print(" " + " ‾" * rows * 2)


def print_computer_board(board, rows):
    """
    The computers board is printed out in a readable way with spaces between
    the dots and numbers along the side. The ships are hidden by replacing
    the '#' with a '.'.
    """
    print(" ", end=" ")
    print(f"{nums_top(rows)}")

    for row, x in zip(board, range(rows)):
        row_copy = [row_char.replace("#", ".") for row_char in row]
        print(f"{x}| " + "   ".join(row_copy) + " |")
    print(" " + " ‾" * rows * 2)


def nums_top(rows):
    """
    The numbers along the top of the board are evenly spaced with underscores
    between them.
    """
    for x in range(rows):
        print(f"_{rows - (rows - x)}_", end=" ")
    return ""


start_game()
