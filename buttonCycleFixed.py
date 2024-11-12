from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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

# Initial Difficulty Text
difficulty = 'Easy'
difficulty_label = ttk.Label(frame1, text=difficulty, style="mod1.TLabel")
difficulty_label.grid(row=1, column=1, columnspan=3, sticky=N)

ttk.Button(frame1, text='Change Game Difficulty', style="mod1.TButton", command=lambda: button_type()).grid(
    row=2, column=1, columnspan=3, sticky=N)
ttk.Label(frame1, text='', style="mod1.TLabel").grid(row=3, column=1, columnspan=3, sticky=N)

# Button Style for changing difficulty
s1 = ttk.Style()
s1.configure('mod1.TButton', background="LightBlue4", foreground="indian red", borderwidth=5,
             font=("Bold", 25))  # TryAgain & Quit buttons

s2 = ttk.Style()
s2.configure('mod2.TButton', background="LightBlue3", foreground="LightBlue4", borderwidth=5,
             font=("Bold", 25))  # 16 buttons for 4x4 grid

s3 = ttk.Style()
s3.configure('mod3.TButton', background="LightBlue3", foreground="indian red", borderwidth=5,
             font=("Bold", 25))  # Winning buttons

# Function to change difficulty
def button_type():
    global difficulty
    # Update difficulty and change label text directly
    if difficulty == "Easy":
        difficulty_label.config(text="Medium")
        difficulty = "Medium"
    elif difficulty == "Medium":
        difficulty_label.config(text="Hard")
        difficulty = "Hard"
    elif difficulty == "Hard":
        difficulty_label.config(text="Easy")
        difficulty = "Easy"

if __name__ == '__main__':
    master.mainloop()
