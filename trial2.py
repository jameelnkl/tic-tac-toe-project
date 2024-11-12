import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("4x4 Tic-Tac-Toe")

# Initialize the game variables
board = [['-' for _ in range(4)] for _ in range(4)]
player = 'O'  # Human player
ai = 'X'  # AI player
game_over = False

# Function to check if a player has won
def is_winner(player):
    for i in range(4):
        if all([board[i][j] == player for j in range(4)]):  # Check row
            return True
        if all([board[j][i] == player for j in range(4)]):  # Check column
            return True
    if all([board[i][i] == player for i in range(4)]):  # Check main diagonal
        return True
    if all([board[i][3 - i] == player for i in range(4)]):  # Check anti-diagonal
        return True
    return False

# Check if the board is full
def is_board_full():
    return all([board[i][j] != '-' for i in range(4) for j in range(4)])

# Evaluate the board (Minimax scoring)
def evaluate():
    if is_winner('X'):  # AI wins
        return 1
    if is_winner('O'):  # Player wins
        return -1
    return 0  # No winner

# Minimax algorithm to choose the best move
def minimax(depth, is_maximizing):
    score = evaluate()
    if score == 1:  # AI wins
        return score
    if score == -1:  # Player wins
        return score
    if is_board_full():
        return 0  # Draw

    if is_maximizing:
        best = -float('inf')
        for i in range(4):
            for j in range(4):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = max(best, minimax(depth + 1, False))
                    board[i][j] = '-'
        return best
    else:
        best = float('inf')
        for i in range(4):
            for j in range(4):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, minimax(depth + 1, True))
                    board[i][j] = '-'
        return best

# Find the best move for AI
def ai_move():
    global game_over
    if not game_over:
        best_val = -float('inf')
        best_move = (-1, -1)
        for i in range(4):
            for j in range(4):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    move_val = minimax(0, False)
                    board[i][j] = '-'
                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
        # Apply the best move
        row, col = best_move
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state="disabled")
        if is_winner('X'):
            result_label.config(text="AI wins!")
            game_over = True
        elif is_board_full():
            result_label.config(text="It's a draw!")
            game_over = True

# Handle the player's move
def player_move(row, col):
    global game_over
    if not game_over and board[row][col] == '-':
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state="disabled")
        if is_winner('O'):
            result_label.config(text="You win!")
            game_over = True
        elif is_board_full():
            result_label.config(text="It's a draw!")
            game_over = True
        else:
            ai_move()

# Reset the game
def reset_game():
    global game_over, board
    game_over = False
    board = [['-' for _ in range(4)] for _ in range(4)]
    result_label.config(text="")
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(text='-', state="normal")

# Create buttons for the 4x4 Tic-Tac-Toe grid
buttons = [[None for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        buttons[i][j] = tk.Button(root, text='-', width=5, height=2,
                                  command=lambda i=i, j=j: player_move(i, j))
        buttons[i][j].grid(row=i, column=j)

# Label to show the result
result_label = tk.Label(root, text="", font=('Arial', 16))
result_label.grid(row=4, column=0, columnspan=4)

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=5, column=0, columnspan=4)

# Start the main loop of the Tkinter window
root.mainloop()

