def print_board(board):             # This function prints the game board.
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print_board(board)