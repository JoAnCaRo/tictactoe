def print_board(board):             # Define a function to print the game board.
    for row in board:               # Loop through each row of the board.
        print(" | ".join(row))      # Print the row with cells separated by " | ".
        print("-" * 9)              # Print a separator line for clarity.


def check_winner(board, player):                    # Define a function to check if the current player won.
    # Check rows
    for row in board:                               # Loop through each row.
        if all([cell == player for cell in row]):   # If all cells in the row match the player's symbol.
            return True                             # The player has won.

    # Check columns
    for col in range(3):                                            # Loop through each column (0, 1, 2).
        if all([board[row][col] == player for row in range(3)]):    # If all cells in the column match.
            return True                                             # The player has won.

    # Check diagonals
    # Check the main diagonal (top-left to bottom-right)
    if all([board[i][i] == player for i in range(3)]) or \
    all([board[i][2 - i] == player for i in range(3)]):     # Check the anti-diagonal (top-right to bottom-left).
        return True                                         # The player has won.

    return False                                            # No win condition met.


def is_full(board):                                                # Define a function to check if the board is full.
    return all([cell != ' ' for row in board for cell in row])


def main():                                                 # Define the main function that handles the game flow.
    board = [[' ' for _ in range(3)] for _ in range(3)]     # Create a 3x3 empty board.
    current_player = 'X'                                    # The game starts with player 'X'.

    while True:                                             # Run the game loop until there's a winner or a tie.
        print_board(board)                                  # Print the current board state.
        print(f"Player: {current_player}")                  # Display whose turn it is.

        # Get the player's move
        try:
            row = int(input("Choose the row (0, 1, 2): "))      # Prompt for row input.
            col = int(input("Choose the column (0, 1, 2): "))   # Prompt for column input.

            if board[row][col] != ' ':                              # Check if the selected cell is already occupied.
                print("The cell is already occupied, try again.")
                continue                                            # Skip to the next iteration of the loop.
        except (ValueError, IndexError):                            # Handle invalid input (non-integer or out of range).
            print("Invalid entry, try again.")
            continue                                                # Ask for input again.

        board[row][col] = current_player  # Place the player's symbol on the board.

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)                          # Print the board one last time.
            print(f"Player {current_player} wins!")     # Announce the winner.
            break                                       # End the game loop.

        # Check for a tie (i.e., the board is full)
        if is_full(board):
            print_board(board)
            print("It's a tie!")     # Announce the tie.
            break                    # End the game loop.

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":   # If this script is run directly, call the main function.
    main()


