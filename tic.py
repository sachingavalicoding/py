def print_board(board):
    # Print the current state of the board
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")


def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    # Check if the board is full (no more moves possible)
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"  # Player X starts

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            # Get player input
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))

            # Check if the move is valid
            if board[row][col] == " ":
                board[row][col] = player
                print_board(board)

                # Check if the current player has won
                winner = check_winner(board)
                if winner:
                    print(f"Player {winner} wins!")
                    break

                # Check if the board is full
                if is_full(board):
                    print("It's a tie!")
                    break

                # Switch players
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move. The cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
