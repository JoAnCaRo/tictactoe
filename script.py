def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Comprobando filas
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Comprobando columnas
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Comprobando diagonales
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Turno del jugador {current_player}")

        try:
            row = int(input("Ingrese la fila (1, 2, 3): "))
            col = int(input("Ingrese la columna (1, 2, 3): "))

            if board[row][col] != ' ':
                print("La celda ya está ocupada, intenta de nuevo.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida, intenta de nuevo.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"¡El jugador {current_player} ha ganado!")
            break

        if is_full(board):
            print_board(board)
            print("¡Es un empate!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
    
