board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_on = True

winner = None

current_player = "X"


def dis_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    dis_board()

    while(game_on):
        handle_turn(current_player)
        check_gameover()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    position = input("Choose from 1-9: ")
    position = int(position) - 1
    board[position] = "X"
    dis_board()


def check_gameover():
    check_if_win()
    check_if_tie()


def check_if_win():

    global winner

    row_winner = check_rows()
    col_winner = check_col()
    diagonal_winner = check_diagonals()

    if row_winner:
        # there is a win
        winner = row_winner
    elif col_winner:
        # there is a win
        winner = col_winner
    elif diagonal_winner:
        # there is a win
        winner = diagonal_winner
    else:
        # there is no win
        winner = None
    return


def check_rows():

    global game_on

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_col():

    global game_on

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_on = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():

    global game_on

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    return


def flip_player():
    return


play_game()
