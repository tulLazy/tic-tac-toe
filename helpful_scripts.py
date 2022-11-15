# Prints the board
def draw_board(hits):
    playing_board = (
        f"|{hits[1]}|{hits[2]}|{hits[3]}|\n"
        f"|{hits[4]}|{hits[5]}|{hits[6]}|\n"
        f"|{hits[7]}|{hits[8]}|{hits[9]}|"
    )
    print(playing_board)


# Checks whose turn is it.
def player_turn(turn):
    if turn % 2 == 1:
        return "X"
    else:
        return "O"


# Check if there's a winner
def check_for_wins(hits, turn, first_player_name, second_player_name):
    # Horizontal checking
    if (
        hits[1] == hits[2] == hits[3]
        or hits[4] == hits[5] == hits[6]
        or hits[7] == hits[8] == hits[9]
    ):
        if player_turn(turn) == "X":
            print(f"{first_player_name} is the winner")
        if player_turn(turn) == "O":
            print(f"{second_player_name} is the winner")
        return True

    # Vertical checking
    if (
        hits[1] == hits[4] == hits[7]
        or hits[2] == hits[5] == hits[8]
        or hits[3] == hits[6] == hits[9]
    ):
        if player_turn(turn) == "X":
            print(f"{first_player_name} is the winner")
        if player_turn(turn) == "O":
            print(f"{second_player_name} is the winner")
        return True
    # Diagonal checking
    if hits[1] == hits[5] == hits[9] or hits[3] == hits[5] == hits[7]:
        if player_turn(turn) == "X":
            print(f"{first_player_name} is the winner")
        if player_turn(turn) == "O":
            print(f"{second_player_name} is the winner")
        return True
    else:
        return False
