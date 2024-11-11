from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random

# Creation of the main window
master = Tk()
master.title("Tic Tac Toe")
master.geometry("800x600")  # Moderate size for centered layout
master.configure(bg="#F5F5F5")  # Very light grey background

# Center the window on the screen
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_cordinate = int((screen_width/2) - (800/2))
y_cordinate = int((screen_height/2) - (600/2))
master.geometry(f"800x600+{x_cordinate}+{y_cordinate}")

# Style configurations
s = ttk.Style()
s.theme_use('clam')
s.configure('mod0.TFrame', background="#F5F5F5")

frame1 = ttk.Frame(master, style='mod0.TFrame', padding=(20, 10))
frame1.pack(pady=(10, 5))  # Centered and spaced nicely
frame2 = ttk.Frame(master, style='mod0.TFrame', padding=(20, 10))
frame2.pack(pady=20)

# Label for "TIC TAC TOE" in Helvetica, greyish black color
s.configure('mod0.TLabel', font=("Helvetica", 32, "bold"), background="#F5F5F5", foreground="#2F2F2F")
ttk.Label(frame1, text='TIC TAC TOE', style="mod0.TLabel").pack(pady=10)

# Adding the "Easy," "Medium," and "Difficult" buttons in one line
s1 = ttk.Style()
s1.configure('mod1.TButton', background="#2F2F2F", foreground="#FFFFFF", borderwidth=3,
             font=("Arial", 14, "bold"), relief="raised", padding=10)  # Greyish black buttons

button_frame = Frame(frame1, bg="#F5F5F5")
button_frame.pack()

ttk.Button(button_frame, text='Easy', style="mod1.TButton", command=lambda: set_difficulty('easy')).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text='Medium', style="mod1.TButton", command=lambda: set_difficulty('medium')).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text='Difficult', style="mod1.TButton", command=lambda: set_difficulty('difficult')).grid(row=0, column=2, padx=5)

# Styling for game boxes to be dark grey
s2 = ttk.Style()
s2.configure('mod2.TButton', background="#2E2E2E", foreground="#FFFFFF", borderwidth=3,
             font=("Arial", 20), relief="ridge", padding=8)

# Functionality placeholders (ensure to replace with your actual logic)
def set_difficulty(level):
    global difficulty
    difficulty = level
    print(f"Difficulty set to: {level}")

# Displaying game buttons in a 3x3 grid
buttons = []
for i in range(3):
    for j in range(3):
        btn = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda i=i, j=j: buttonClick(i, j))
        btn.grid(row=i, column=j, ipadx=30, ipady=30, padx=5, pady=5)
        buttons.append(btn)

# Initialize the board
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
BOT_TURN = False
count = 0
someone_won = False
difficulty = 'medium'  # Default difficulty

# Functionality for "Try Again" and "Quit" buttons
def try_again():
    global board, count, BOT_TURN, someone_won
    for btn in buttons:
        btn.config(text=' ')
    board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    BOT_TURN = False
    count = 0
    someone_won = False
    print("Game reset")

def quit_game():
    master.quit()

# Function to check if someone won
def checkWin():
    for line in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]:
        if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != ' ':
            return True
    return False

# Function to check if the game ended in a draw
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

# Function to update the buttons on the interface
def updateButtons():
    for i, btn in enumerate(buttons, start=1):
        btn.config(text=board[i])

# Function to handle player's move
def buttonClick(i, j):
    global BOT_TURN, count, someone_won
    index = i * 3 + j + 1
    if board[index] != ' ' or someone_won:
        return

    # Player's move ('O')
    board[index] = 'O'
    updateButtons()
    count += 1

    if checkWin():
        ttk.Label(frame1, text='Player Wins!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=tk.N)
        return
    elif checkDraw():
        ttk.Label(frame1, text='Draw!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=tk.N)
        return

    # Now it's the bot's turn
    BOT_TURN = True
    comMove()

# Bot's move function (AI logic)
def comMove():
    global BOT_TURN, count, difficulty
    if not BOT_TURN:
        return

    available_moves = [i for i in range(1, 10) if board[i] == ' ']
    if available_moves:
        if difficulty == 'easy':
            move = random.choice(available_moves)
        elif difficulty == 'medium':
            move = minimax(available_moves)
        elif difficulty == 'difficult':
            move = minimax(available_moves, depth=5)  # Deeper search for hard mode

        board[move] = 'X'  # Bot plays 'X'
        updateButtons()
        count += 1

        if checkWin():
            ttk.Label(frame1, text='Bot Wins!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=tk.N)
        elif checkDraw():
            ttk.Label(frame1, text='Draw!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=tk.N)

        BOT_TURN = False

# Minimax Algorithm (medium/difficult AI)
def minimax(available_moves, depth=3):
    best_score = -float('inf')
    best_move = None

    for move in available_moves:
        board[move] = 'X'
        score = minimax_recursion(depth - 1, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def minimax_recursion(depth, is_maximizing):
    if checkWin():
        return 1 if is_maximizing else -1
    if checkDraw() or depth == 0:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in range(1, 10):
            if board[move] == ' ':
                board[move] = 'X'
                score = minimax_recursion(depth - 1, False)
                board[move] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in range(1, 10):
            if board[move] == ' ':
                board[move] = 'O'
                score = minimax_recursion(depth - 1, True)
                board[move] = ' '
                best_score = min(best_score, score)
        return best_score

# Add "Try Again" and "Quit" buttons below the game board
button_frame_bottom = Frame(master, bg="#F5F5F5")
button_frame_bottom.pack(pady=20)

ttk.Button(button_frame_bottom, text="Try Again", style="mod1.TButton", command=try_again).pack(side=LEFT, padx=10)
ttk.Button(button_frame_bottom, text="Quit", style="mod1.TButton", command=quit_game).pack(side=LEFT, padx=10)

# Run the application
master.mainloop()

