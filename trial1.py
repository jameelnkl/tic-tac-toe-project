from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# Creation of the main window
master = Tk()
master.title("Tic Tac Toe")
master.geometry("800x800")  # Moderate size for centered layout
master.configure(bg="#F5F5F5")  # Very light grey background

# Center the window on the screen
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_cordinate = int((screen_width/2) - (800/2))
y_cordinate = int((screen_height/2) - (800/2))
master.geometry(f"800x800+{x_cordinate}+{y_cordinate}")

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

# Difficulty levels
difficulty_level = "medium"  # Default to medium
def set_difficulty(level):
    global difficulty_level
    difficulty_level = level
    print(f"Difficulty set to: {level}")

ttk.Button(button_frame, text='Easy', style="mod1.TButton", command=lambda: set_difficulty('easy')).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text='Medium', style="mod1.TButton", command=lambda: set_difficulty('medium')).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text='Difficult', style="mod1.TButton", command=lambda: set_difficulty('difficult')).grid(row=0, column=2, padx=5)

# Styling for game boxes to be dark grey
s2 = ttk.Style()
s2.configure('mod2.TButton', background="#2E2E2E", foreground="#FFFFFF", borderwidth=3,
             font=("Arial", 20), relief="ridge", padding=8)

# Initialize board
board = {i: ' ' for i in range(1, 17)}

def create_board():
    global board
    board = {i: ' ' for i in range(1, 17)}

def spaceIsFree(position):
    return board[position] == ' '

# Update the checkWin and checkDraw for 4x4 grid
def checkDraw():
    return all(board[i] != ' ' for i in board)

def checkWin():
    # Check rows, columns, and diagonals for a 4x4 grid
    for i in range(1, 17, 4):
        if board[i] == board[i+1] == board[i+2] == board[i+3] and board[i] != ' ':
            return True
    for i in range(1, 5):
        if board[i] == board[i+4] == board[i+8] == board[i+12] and board[i] != ' ':
            return True
    if board[1] == board[6] == board[11] == board[16] and board[1] != ' ':
        return True
    if board[4] == board[7] == board[10] == board[13] and board[4] != ' ':
        return True
    return False

def minimax(board, depth, isMaximizing):
    if checkWin():
        return 1 if isMaximizing else -1
    if checkDraw():
        return 0
    if depth == 0:
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for i in board:
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth-1, False)
                board[i] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for i in board:
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth-1, True)
                board[i] = ' '
                bestScore = min(score, bestScore)
        return bestScore

# Function to update the board display
def updateButtons():
    for i in range(1, 17):
        buttons[i-1]['text'] = board[i]

def disable_emptys():
    for i in range(1, 17):
        if board[i] == ' ':
            buttons[i-1]['state'] = DISABLED

# Function for AI move
def comMove():
    bestScore = -float('inf')
    bestMove = None
    max_depth = 1 if difficulty_level == 'easy' else 3 if difficulty_level == 'medium' else 5

    for i in range(1, 17):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, max_depth, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i

    board[bestMove] = 'X'
    updateButtons()

    if checkWin():
        disable_emptys()
        tkinter.messagebox.showinfo("Bot Wins!", "The Bot has won!")
    elif checkDraw():
        tkinter.messagebox.showinfo("Draw", "It's a draw!")

# Function for player move
def playerMove(index):
    if board[index] != ' ':
        tkinter.messagebox.showwarning("Invalid Move", "That space is already occupied!")
        return
    board[index] = 'O'
    updateButtons()

    if checkWin():
        disable_emptys()
        tkinter.messagebox.showinfo("Player Wins!", "You win!")
    elif checkDraw():
        tkinter.messagebox.showinfo("Draw", "It's a draw!")

    comMove()

# Create buttons for the 4x4 grid
buttons = []
for i in range(1, 17):
    btn = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda i=i: playerMove(i))
    row = (i-1) // 4 + 1
    col = (i-1) % 4 + 1
    btn.grid(row=row, column=col, ipadx=30, ipady=30, padx=5, pady=5)
    buttons.append(btn)

# Try again and Quit buttons
def try_again():
    create_board()
    updateButtons()

ttk.Button(frame2, text="Try Again", style="mod1.TButton", command=try_again).grid(row=5, column=1, pady=20)
ttk.Button(frame2, text="Quit", style="mod1.TButton", command=master.quit).grid(row=5, column=4, pady=20)

# Run the application
master.mainloop()