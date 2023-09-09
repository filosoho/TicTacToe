# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]


# Function to print the Tic Tac Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


# Function to check if the board is full (a tie)
def check_tie(board):
    return " " not in board


# Main game loop
current_player = "X"
game_over = False

while not game_over:
    print_board(board)
    print(f"Player {current_player}'s turn")

    # Get the player's move
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

    # Make the move
    board[move] = current_player

    # Check for a win or a tie
    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        game_over = True
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        game_over = True
    else:
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"
