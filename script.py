def print_board(board):             # This function prints the game board.
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):    # This function checks if the actual player won.
    # check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):                 # This function checks if the board is full.
    return all([cell != ' ' for row in board for cell in row])

def main():                         # This is the main function that handles the flow of the game.
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player: {current_player}")

        try:
            row = int(input("Choose the row (0, 1, 2): "))
            col = int(input("Choose the column (0, 1, 2): "))

            if board[row][col] != ' ':
                print("The cell is already occupied, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid entry, try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()

    

