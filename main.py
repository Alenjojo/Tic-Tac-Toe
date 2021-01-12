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
        winner = row_winner()
    elif col_winner:
        # there is a win
        winner = col_winner()
    elif diagonal_winner:
        # there is a win
        winner = diagonal_winner()
    else:
        # there is no win
        winner = None
    return


def check_rows():
    row_1 = board[0] == board[1] == board[2] != "-"
    return


def check_col():
    return


def check_diagonals():
    return


def check_if_tie():
    return


def flip_player():
    return


play_game()
