from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
import sys
from turtle import bgcolor

# Creation de la fenetre d'Accueil

master = Tk()
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
master.minsize(screen_width, screen_height)
master.title("Tic Tac Toe")

# Style Creation
bgcolor = "#E2FFDE"
master['background'] = bgcolor

s = ttk.Style()
s.theme_use('clam')
s.configure('mod0.TFrame', background=bgcolor)

frame1 = ttk.Frame(master, style='mod0.TFrame')
frame1.grid(row=0, column=0, padx=570, pady=2)
frame2 = ttk.Frame(master, style='mod0.TFrame')
frame2.grid(row=1, column=0, pady=2)


s.configure('mod0.TLabel', font=("Bold", 42), background=bgcolor, foreground="LightBlue4")
s.configure('mod1.TLabel', font=("Silkscreen", 18), background=bgcolor, foreground="LightBlue4")
ttk.Label(frame1, text='TIC TAC TOE', style="mod0.TLabel").grid(row=0, column=1, columnspan=4, sticky=(N))
# difficulty = 'Easy'


ttk.Button(frame1, text='Easy', style="mod1.TButton", command=lambda: button_type("Easy")).grid(
    row=2, column=0, padx=5, pady=5, sticky=N)  # padx and pady add space around the button

ttk.Button(frame1, text='Medium', style="mod1.TButton", command=lambda: button_type("Medium")).grid(
    row=2, column=1, padx=5, pady=5, sticky=N)

ttk.Button(frame1, text='Hard', style="mod1.TButton", command=lambda: button_type("Hard")).grid(
    row=2, column=2, padx=5, pady=5, sticky=N)



s1 = ttk.Style()
s1.configure('mod1.TButton', background="LightBlue4", foreground="indian red", borderwidth=5,
             font=("Bold", 25))  # TryAgain & Quit buttons

s2 = ttk.Style()
s2.configure('mod2.TButton', background="LightBlue3", foreground="LightBlue4", borderwidth=5,
             font=("Bold", 25))  # 16 buttons for 4x4 grid

s3 = ttk.Style()
s3.configure('mod3.TButton', background="LightBlue3", foreground="indian red", borderwidth=5,
             font=("Bold", 25))  # Winning buttons
BOT_TURN = False
difficulty = 'Easy'
someone_won = False
count = 0

def create_board(board):
    return {i: " " for i in range(16)}  # Ensure dictionary has keys 0 to 15


board = create_board({}) #a dictionary as a parameter


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def checker(letter): #check the game state after each move
    if checkWin():
        if letter == 'X':
            print("Bot Win !")
            checkWhoWonTkinter("X")
            exit()
        else:
            print("Player Wins!")
            checkWhoWonTkinter("O")
            exit()
    if checkDraw():
        print("Draw!")
        exit()
    return


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkWin(): #tocheck if there is a win
    for row in range(1, 16, 4):  # Rows start at 1, 5, 9, and 13
        if board[row] == board[row+1] == board[row+2] == board[row+3] != ' ':
            return True
    for col in range(1, 5):  # Columns start at 1, 2, 3, and 4
        if board[col] == board[col+4] == board[col+8] == board[col+12] != ' ':
            return True
    if board[1] == board[6] == board[11] == board[16] != ' ':
        return True
    if board[4] == board[7] == board[10] == board[13] != ' ':
        return True
    return False


def checkWhoWon(letter): #to check if this letter won
    for row in range(1, 16, 4):  # Rows start at 1, 5, 9, and 13
        if board[row] == board[row+1] == board[row+2] == board[row+3] == letter:
            return True
    for col in range(1, 5):  # Columns start at 1, 2, 3, and 4
        if board[col] == board[col+4] == board[col+8] == board[col+12] == letter:
            return True
    if board[1] == board[6] == board[11] == board[16] == letter:
        return True
    if board[4] == board[7] == board[10] == board[13] == letter:
        return True
    return False

max_depth_levels = {
    "Easy": 2,
    "Medium": 4,
    "Hard": 6
}

# Set difficulty levels with maximum depths
max_depth_levels = {
    "Easy": 2,
    "Medium": 4,
    "Hard": 6
}

def minimax(board, isMaximizing, depth=0):
    # Get the maximum depth based on difficulty level
    max_depth = max_depth_levels.get(difficulty, 6)  # Default to depth 6 if not defined

    # Check if the game has been won or if it's a draw
    if checkWhoWon('X'):
        return 1
    elif checkWhoWon('O'):
        return -1
    elif checkDraw() or depth >= max_depth:
        return 0  # Return 0 if it's a draw or we've reached the maximum depth

    # Maximizing player (bot 'X')
    if isMaximizing:
        bestScore = -float('inf')  # Start with the lowest possible score
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'  # Try the bot's move
                score = minimax(board, False, depth + 1)  # Recursively call minimax for the opponent's turn
                board[key] = ' '  # Undo the move
                bestScore = max(score, bestScore)  # Keep the maximum score
        return bestScore
    # Minimizing player (opponent 'O')
    else:
        bestScore = float('inf')  # Start with the highest possible score
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'  # Try the opponent's move
                score = minimax(board, True, depth + 1)  # Recursively call minimax for the bot's turn
                board[key] = ' '  # Undo the move
                bestScore = min(score, bestScore)  # Keep the minimum score
        return bestScore


def jouer(index):
    global BOT_TURN, count
    if board[index] != " ":
        print("Button is already clicked!")
        tkinter.messagebox.showwarning(title="Warning!", message="Button already Clicked!")

    elif board[index] == " " and BOT_TURN:
        comMove()

    elif board[index] == " " and not BOT_TURN:
        # Player's move
        board[index] = "O"
        updateButtons()  
        playerMove() 
        checkWhoWon("X")

def colorChecker(symbol, button):
    if symbol == "X":
        button['text'] = symbol
        button['state'] = DISABLED 

    elif symbol == "O":
        button['text'] = symbol
        button['state'] = DISABLED 

    elif symbol == " ":
        button['text'] = symbol
        button['state'] = NORMAL  

def updateButtons():
    colorChecker(board[1], b1)
    colorChecker(board[2], b2)
    colorChecker(board[3], b3)
    colorChecker(board[4], b4)
    colorChecker(board[5], b5)
    colorChecker(board[6], b6)
    colorChecker(board[7], b7)
    colorChecker(board[8], b8)
    colorChecker(board[9], b9)
    colorChecker(board[10], b10)
    colorChecker(board[11], b11)
    colorChecker(board[12], b12)
    colorChecker(board[13], b13)
    colorChecker(board[14], b14)
    colorChecker(board[15], b15)
    colorChecker(board[16], b16)


def disable_emptys():
    # for index in range(1, 17):  # Loop through the 16 positions (1 to 16)
    for index in range(16):
        if board[index] == " ":  # Check if the position is empty
            liste_bouttons[index]["state"] = DISABLED  # Disable the corresponding button


def updateStyles():
    # for index in range(1, 17): # Loop through positions 1 to 16 for the 4x4 grid
    for index in range(16):  
        liste_bouttons[index]["style"] = "mod2.TButton"  # Apply the style to the button


def playerMove():
    global BOT_TURN, someone_won, count
    BOT_TURN = True  # Set the bot's turn to True, signaling that the bot will make a move
    count += 1

    # Check if the player has won after their move
    if checkWhoWon("O"):
        print("Player wins!")
        checkWhoWonTkinter("O")  # Update the UI for player win
        ttk.Label(frame1, text='Player Win!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)
        someone_won = True  # Set the flag to True, indicating that someone won
        return  # Exit the function, no need to continue if the player won

    comMove()  # Bot makes its move

def checkWhoWonTkinter(letter):
    # Horizontal Win Conditions
    if board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == letter:
        b1['style'] = b2['style'] = b3['style'] = b4['style'] = "mod3.TButton"
    elif board[5] == board[6] and board[5] == board[7] and board[5] == board[8] and board[5] == letter:
        b5['style'] = b6['style'] = b7['style'] = b8['style'] = "mod3.TButton"
    elif board[9] == board[10] and board[9] == board[11] and board[9] == board[12] and board[9] == letter:
        b9['style'] = b10['style'] = b11['style'] = b12['style'] = "mod3.TButton"
    elif board[13] == board[14] and board[13] == board[15] and board[13] == board[16] and board[13] == letter:
        b13['style'] = b14['style'] = b15['style'] = b16['style'] = "mod3.TButton"

    # Vertical Win Conditions
    elif board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] == letter:
        b1['style'] = b5['style'] = b9['style'] = b13['style'] = "mod3.TButton"
    elif board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] == letter:
        b2['style'] = b6['style'] = b10['style'] = b14['style'] = "mod3.TButton"
    elif board[3] == board[7] and board[3] == board[11] and board[3] == board[15] and board[3] == letter:
        b3['style'] = b7['style'] = b11['style'] = b15['style'] = "mod3.TButton"
    elif board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] == letter:
        b4['style'] = b8['style'] = b12['style'] = b16['style'] = "mod3.TButton"

    # Diagonal Win Conditions
    elif board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == letter:
        b1['style'] = b6['style'] = b11['style'] = b16['style'] = "mod3.TButton"
    elif board[4] == board[7] and board[4] == board[10] and board[4] == board[13] and board[4] == letter:
        b4['style'] = b7['style'] = b10['style'] = b13['style'] = "mod3.TButton"


# difficulty_label = ttk.Label(frame1, text=difficulty, style="mod1.TLabel")
# difficulty_label.grid(row=1, column=1, columnspan=3, sticky=N)

difficulty = "Easy"

def button_type(level):
    global difficulty
    TryAgain() 
    difficulty = level
    print(f"Difficulty set to: {difficulty}")  # Optional: print to confirm


def comMove():
    global BOT_TURN, someone_won, count
    BOT_TURN = False
    count += 1

    bestScore = -1
    bestMove = 0  # will be changed

    # Adjust the depth based on difficulty level
    depth = 2 if difficulty == "Easy" else 4 if difficulty == "Medium" else 6

    # Loop through all the cells of the 4x4 board
    for key in range(1, 17):  # since we have a 4x4 board, 1 to 16
        if board[key] == ' ':
            board[key] = 'X'  # Simulate the bot's move

            # Use Minimax for decision making
            score = minimax(board, False, depth)  # Pass depth here for difficulty level

            board[key] = ' '  # Undo the simulated move

            # Check if this move is the best move
            if score > bestScore:
                bestScore = score
                bestMove = key

    # Make the best move
    board[bestMove] = "X"
    updateButtons()

    # Check if the bot has won
    if checkWhoWon("X"):
        print("Bot wins!")
        disable_emptys()
        checkWhoWonTkinter("X")
        ttk.Label(frame1, text='Bot Win!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)
        someone_won = True

    print(count)
    # Check for draw condition
    if count == 16 and not someone_won:  # 16 moves for a 4x4 grid
        disable_emptys()
        ttk.Label(frame1, text='Draw!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)

def TryAgain(board=board):
    global BOT_TURN
    global someone_won
    global count
    
    ttk.Label(frame1, text='                             ', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)

    for index in board.keys():
        board[index] = ' '  

    BOT_TURN = False  
    someone_won = False  
    count = 0  
    updateButtons()
    updateStyles()


b1 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(1))
b2 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(2))
b3 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(3))
b4 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(4))
b5 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(5))
b6 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(6))
b7 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(7))
b8 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(8))
b9 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(9))
b10 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(10))
b11 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(11))
b12 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(12))
b13 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(13))
b14 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(14))
b15 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(15))
b16 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(16))

liste_bouttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
b1.grid(row=1, column=1, ipady=45)
b2.grid(row=1, column=2, ipady=45)
b3.grid(row=1, column=3, ipady=45)
b4.grid(row=1, column=4, ipady=45)
b5.grid(row=2, column=1, ipady=45)
b6.grid(row=2, column=2, ipady=45)
b7.grid(row=2, column=3, ipady=45)
b8.grid(row=2, column=4, ipady=45)
b9.grid(row=3, column=1, ipady=45)
b10.grid(row=3, column=2, ipady=45)
b11.grid(row=3, column=3, ipady=45)
b12.grid(row=3, column=4, ipady=45)
b13.grid(row=4, column=1, ipady=45)
b14.grid(row=4, column=2, ipady=45)
b15.grid(row=4, column=3, ipady=45)
b16.grid(row=4, column=4, ipady=45)

TryAgainBoutton = ttk.Button(frame2, text="Try Again", style="mod1.TButton", command=TryAgain)
TryAgainBoutton.grid(row=5, column=1, columnspan=2, pady=20)

quitterBoutton = ttk.Button(frame2, text="Quit", style="mod1.TButton", command=master.destroy)
quitterBoutton.grid(row=5, column=3, columnspan=2, pady=20)


# PROG PRINCIPAL:
# ================
if __name__ == '__main__':
    master.mainloop()
