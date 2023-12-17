# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Join each cell in the row with " | " and print
        print("-" * 9)  # Print a separator line after each row

# Function to check if the current player has won
def check_win(board, player):
    # Define all possible winning conditions
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Middle column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal from top-left
        [board[0][2], board[1][1], board[2][0]]   # Diagonal from top-right
    ]
    # Check if any win condition is met
    return [player, player, player] in win_conditions

# Function to get the current player's move
def get_move(player):
    while True:  # Loop until a valid move is entered
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1  # Convert input to zero-based index
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2:  # Check if input is within the board range
                return row, col
            else:
                print("Invalid input. Please enter row and column between 1 and 3.")
        except ValueError:  # Handle non-integer inputs
            print("Invalid input. Please enter a number.")

# Main function to run the game
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 board with empty spaces
    player = "X"  # Start with player X
    moves_count = 0  # Track the number of moves made

    while True:  # Main game loop
        print_board(board)  # Print the current state of the board
        row, col = get_move(player)  # Get the current player's move

        if board[row][col] == " ":  # Check if the chosen cell is empty
            board[row][col] = player  # Place the player's mark on the board
            moves_count += 1  # Increment the move counter

            if check_win(board, player):  # Check for a win
                print_board(board)
                print(f"Player {player} wins!")
                break

            if moves_count == 9:  # Check for a tie
                print_board(board)
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"  # Switch players
        else:
            print("This cell is already taken. Please choose another cell.")  # Handle case where cell is already taken

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    main()
