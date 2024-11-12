from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import bgcolor

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


#set difficulty buttons
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

#global variables for the programme
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
            # checkWhoWonTkinter("X")
            exit()
        else:
            print("Player Wins!")
            # checkWhoWonTkinter("O")
            exit()
    if checkDraw():
        print("Draw!")
        exit()
    return

def checkDraw():
    if ' ' in board.values():
        return False
    return True

def checkWin(): #tocheck if there is a win
    for row in range(0, 16, 4):  # Rows start at 1, 5, 9, and 13
        if board[row] == board[row+1] == board[row+2] == board[row+3] != ' ':
            return True
    for col in range(4):  # Columns start at 1, 2, 3, and 4
        if board[col] == board[col+4] == board[col+8] == board[col+12] != ' ':
            return True
    if board[0] == board[5] == board[10] == board[15] != ' ':
        return True
    if board[3] == board[6] == board[9] == board[12] != ' ':
        return True
    return False

def checkWhoWon(letter): #to check if this letter won
    for row in range(0, 16, 4):  
        if board[row] == board[row+1] == board[row+2] == board[row+3] == letter:
            return True
    for col in range(4):  # Columns start at 1, 2, 3, and 4
        if board[col] == board[col+4] == board[col+8] == board[col+12] == letter:
            return True
    if board[0] == board[5] == board[10] == board[15] == letter:
        return True
    if board[3] == board[6] == board[9] == board[12] == letter:
        return True
    return False

max_depth_levels = {
    "Easy": 2,
    "Medium": 3,
    "Hard": 4
}
def evaluate(board):
    # Check if someone has already won
    if checkWhoWon('X'):
        return 1
    elif checkWhoWon('O'):
        return -1
    
    x_score = 0
    o_score = 0

    # Check rows (0-3)
    for row in range(4):
        x_count = sum(1 for col in range(4) if board[row * 4 + col] == 'X')
        o_count = sum(1 for col in range(4) if board[row * 4 + col] == 'O')

        if x_count == 3 and o_count == 0:
            x_score += 10  # Close to winning
        elif o_count == 3 and x_count == 0:
            o_score += 10  # Close to losing
        elif x_count == 2 and o_count == 0:
            x_score += 3   # Favorable state for X
        elif o_count == 2 and x_count == 0:
            o_score += 3   # Favorable state for O

    # Check columns (0-3)
    for col in range(4):
        x_count = sum(1 for row in range(4) if board[row * 4 + col] == 'X')
        o_count = sum(1 for row in range(4) if board[row * 4 + col] == 'O')

        if x_count == 3 and o_count == 0:
            x_score += 10  # Close to winning
        elif o_count == 3 and x_count == 0:
            o_score += 10  # Close to losing
        elif x_count == 2 and o_count == 0:
            x_score += 3   # Favorable state for X
        elif o_count == 2 and x_count == 0:
            o_score += 3   # Favorable state for O

    # Check main diagonal (positions: 0, 5, 10, 15)
    x_count = sum(1 for i in range(4) if board[i * 4 + i] == 'X')
    o_count = sum(1 for i in range(4) if board[i * 4 + i] == 'O')

    if x_count == 3 and o_count == 0:
        x_score += 10  # Close to winning
    elif o_count == 3 and x_count == 0:
        o_score += 10  # Close to losing
    elif x_count == 2 and o_count == 0:
        x_score += 3   # Favorable state for X
    elif o_count == 2 and x_count == 0:
        o_score += 3   # Favorable state for O

    # Check anti-diagonal (positions: 3, 6, 9, 12)
    x_count = sum(1 for i in range(4) if board[i * 4 + (3 - i)] == 'X')
    o_count = sum(1 for i in range(4) if board[i * 4 + (3 - i)] == 'O')

    if x_count == 3 and o_count == 0:
        x_score += 10  # Close to winning
    elif o_count == 3 and x_count == 0:
        o_score += 10  # Close to losing
    elif x_count == 2 and o_count == 0:
        x_score += 3   # Favorable state for X
    elif o_count == 2 and x_count == 0:
        o_score += 3   # Favorable state for O

    # Return the score: positive score is better for X, negative for O
    return x_score - o_score
    


def minimax(board, isMaximizing,depth=0, alpha=-float('inf'), beta=float('inf')): #X is maximizing O is minimizing
    max_depth = max_depth_levels.get(difficulty)
    if checkWhoWon('X'):
        return 1
    elif checkWhoWon('O'):
        return -1
    elif checkDraw() or depth >= max_depth:
        return evaluate(board)
    if isMaximizing: #if its X's turn
        bestScore = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, False, depth + 1, alpha, beta)
                board[key] = ' '
                bestScore = max(bestScore, score)
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
        return bestScore
    else: #if its O's turn
        bestScore = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, True, depth + 1, alpha, beta)
                board[key] = ' '
                bestScore = min(bestScore, score)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
        return bestScore

def jouer(index):
    global BOT_TURN, count
    if board[index] != " ":
        print("Button is already clicked!")
        tkinter.messagebox.showwarning(title="Warning!", message="Button already Clicked!")

    elif board[index] == " " and BOT_TURN:
        comMove()

    elif board[index] == " " and BOT_TURN == False:
        board[index] = "O"
        updateButtons()
        playerMove()
        checkWhoWon("X")

def colorChecker(symbol, boutton):
    if (symbol == "X"):
        boutton['text'] = symbol

    if (symbol == "O"):
        boutton['text'] = symbol

    if (symbol == " "):
        boutton['text'] = symbol
        boutton['state'] = NORMAL

def updateButtons():
    colorChecker(board[0], b1)
    colorChecker(board[1], b2)
    colorChecker(board[2], b3)
    colorChecker(board[3], b4)
    colorChecker(board[4], b5)
    colorChecker(board[5], b6)
    colorChecker(board[6], b7)
    colorChecker(board[7], b8)
    colorChecker(board[8], b9)
    colorChecker(board[9], b10)
    colorChecker(board[10], b11)
    colorChecker(board[11], b12)
    colorChecker(board[12], b13)
    colorChecker(board[13], b14)
    colorChecker(board[14], b15)
    colorChecker(board[15], b16)

def disable_emptys():
    for index in board.keys():
        if liste_bouttons[index]['text'] == " ":
            liste_bouttons[index]["state"] = DISABLED

def updateStyles():
    for index in board.keys():
        liste_bouttons[index]["style"] = "mod2.TButton"

def playerMove():
    global BOT_TURN, someone_won, count
    BOT_TURN = True
    count += 1
    if checkWhoWon("O"):
        print("player win")
        checkWhoWonTkinter("O")
        # tkinter.messagebox.showwarning(title="Congrats!", message="Player Win!")
        ttk.Label(frame1, text='Player Win!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)
        someone_won = True
        return
    comMove()

def checkWhoWonTkinter(letter):
    # Rows check
    if board[0] == board[1] == board[2] == board[3] == letter:
        b1['style'] = b2['style'] = b3['style'] = b4['style'] = "mod3.TButton"
    elif board[4] == board[5] == board[6] == board[7] == letter:
        b5['style'] = b6['style'] = b7['style'] = b8['style'] = "mod3.TButton"
    elif board[8] == board[9] == board[10] == board[11] == letter:
        b9['style'] = b10['style'] = b11['style'] = b12['style'] = "mod3.TButton"
    elif board[12] == board[13] == board[14] == board[15] == letter:
        b13['style'] = b14['style'] = b15['style'] = b16['style'] = "mod3.TButton"

    # Columns check
    elif board[0] == board[4] == board[8] == board[12] == letter:
        b1['style'] = b5['style'] = b9['style'] = b13['style'] = "mod3.TButton"
    elif board[1] == board[5] == board[9] == board[13] == letter:
        b2['style'] = b6['style'] = b10['style'] = b14['style'] = "mod3.TButton"
    elif board[2] == board[6] == board[10] == board[14] == letter:
        b3['style'] = b7['style'] = b11['style'] = b15['style'] = "mod3.TButton"
    elif board[3] == board[7] == board[11] == board[15] == letter:
        b4['style'] = b8['style'] = b12['style'] = b16['style'] = "mod3.TButton"

    # Diagonals check
    elif board[0] == board[5] == board[10] == board[15] == letter:
        b1['style'] = b6['style'] = b11['style'] = b16['style'] = "mod3.TButton"
    elif board[3] == board[6] == board[9] == board[12] == letter:
        b4['style'] = b7['style'] = b10['style'] = b13['style'] = "mod3.TButton"


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

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
            
    board[bestMove] = "X"
    updateButtons()
    if checkWhoWon("X"):
        print("bot win")
        disable_emptys()
        checkWhoWonTkinter("X")
        ttk.Label(frame1, text='Bot Win!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)
        someone_won = True

    # print(count)
    if count == 16 and someone_won == False:
        disable_emptys()
        ttk.Label(frame1, text='Draw!', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)


def TryAgain(board=board):
    global BOT_TURN
    global someone_won
    global count
    ttk.Label(frame1, text='                             ', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)

    for index in board.keys():
        board[index] = " "
    BOT_TURN = False
    someone_won = False
    count = 0
    updateButtons()
    updateStyles()

b1 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(0))
b2 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(1))
b3 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(2))
b4 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(3))
b5 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(4))
b6 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(5))
b7 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(6))
b8 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(7))
b9 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(8))
b10 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(9))
b11 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(10))
b12 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(11))
b13 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(12))
b14 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(13))
b15 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(14))
b16 = ttk.Button(frame2, text=' ', style="mod2.TButton", command=lambda: jouer(15))

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
TryAgainBoutton.grid(row=5, column=1, pady=70)

quitterBoutton = ttk.Button(frame2, text="Quit", style="mod1.TButton", command=master.destroy)
quitterBoutton.grid(row=5, column=3, pady=70)

# PROG PRINCIPAL:
# ================
if __name__ == '__main__':
    master.mainloop()
