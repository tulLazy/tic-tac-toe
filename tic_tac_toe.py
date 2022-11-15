from helpful_scripts import draw_board, player_turn, check_for_wins
import os

# Dictionary that will help us later to play tic tac toe
hits = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}


def main():
    print("Welcome in tic tac toe")
    # Players names or nicknames
    first_player = input("Insert first player's name or nickname: ")
    second_player = input("Insert second player's name or nickname: ")
    # This variable is set True and as long as it stays True the while loop will keep looping 
    playing = True
    # This keeps track of whose turn is it 
    turn = 0
    # We need this variable to send an error message when a value that the player sent is not valid
    previous_turn = -1
    while playing:
        # Resets the terminal so that we do not have to print the playing board every time
        os.system("cls" if os.name == "nt" else "clear")
        # Draw the current board game
        draw_board(hits)
        # Checking for a winner
        if check_for_wins(hits, turn, first_player, second_player):
            playing = False
        # Checking for a tie
        elif (
            turn > 8
            and check_for_wins(hits, turn, first_player, second_player) == False
        ):
            print("The game is a tie")
            playing = False
        # if there's not a winner and the game is not a tie, go on with the program
        else:
            # Checking wich player's turn is it
            if player_turn(turn + 1) == "X":
                print(
                    f"It's {first_player}'s turn. Type q or Q if you want to quit, otherwise choose what spot you'd like to hit: "
                )
            elif player_turn(turn + 1) == "O":
                print(
                    f"It's {second_player}'s turn. Type q or Q if you want to quit, otherwise choose what spot you'd like to hit: "
                )
            # If there's an invalid input try again
            if previous_turn == turn:
                print("Invalid input try again")
            previous_turn = turn
            # Input the spot to hit
            choice = input()
            # Checking if the player wants to quit
            if choice == "q" or choice == "Q":
                playing = False
            # Checking if the input is a digit and if the input is inside our hits
            elif str.isdigit(choice) and int(choice) in hits:
                # Check if the spot has already been taken
                if not hits[int(choice)] in {"X", "O"}:
                    turn += 1
                    hits[int(choice)] = player_turn(turn)
    print("Thanks for playing!")


# Built in variable which value is "__main__", therefore it's going to run the main function always
if __name__ == "__main__":
    main()
