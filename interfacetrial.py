from tkinter import *
from tkinter import ttk

# Creation of the main window
master = Tk()
master.title("Tic Tac Toe")
master.geometry("800x700")  # Adjusted size for 4x4 grid
master.configure(bg="#F5F5F5")  # Very light grey background

# Center the window on the screen
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (800 / 2))
y_cordinate = int((screen_height / 2) - (700 / 2))
master.geometry(f"800x700+{x_cordinate}+{y_cordinate}")

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

# Difficulty button that toggles between Easy, Medium, and Hard
difficulty = StringVar()
difficulty.set("Easy")  # Initial difficulty is Easy

def toggle_difficulty():
    current_difficulty = difficulty.get()
    if current_difficulty == "Easy":
        difficulty.set("Medium")
    elif current_difficulty == "Medium":
        difficulty.set("Hard")
    else:
        difficulty.set("Easy")
    difficulty_button.config(text=f"Difficulty: {difficulty.get()}")

# # Difficulty button
# difficulty_button = ttk.Button(frame1, text=f"Difficulty: {difficulty.get()}", style="mod1.TButton", command=toggle_difficulty)
# difficulty_button.pack(pady=10)

# Styling for game boxes to be dark grey
s2 = ttk.Style()
s2.configure('mod2.TButton', background="#2E2E2E", foreground="#FFFFFF", borderwidth=3,
             font=("Arial", 20), relief="ridge", padding=8)

# Functionality placeholders (ensure to replace with your actual logic)
def set_difficulty(level):
    print(f"Difficulty set to: {level}")
    # Adjust the depth of AI search based on difficulty here

# Displaying game buttons in a 4x4 grid
buttons = []
for i in range(4):
    for j in range(4):
        btn = ttk.Button(frame2, text=' ', style="mod2.TButton")
        btn.grid(row=i, column=j, ipadx=30, ipady=30, padx=5, pady=5)
        buttons.append(btn)

# Functionality for "Try Again" and "Quit" buttons
def try_again():
    # Reset game logic goes here (clear the buttons, etc.)
    for btn in buttons:
        btn.config(text=' ')
    print("Game reset")

def quit_game():
    master.quit()

# Add "Try Again" and "Quit" buttons below the game board
button_frame_bottom = Frame(master, bg="#F5F5F5")
button_frame_bottom.pack(pady=20)

ttk.Button(button_frame_bottom, text="Try Again", style="mod1.TButton", command=try_again).pack(side=LEFT, padx=10)
ttk.Button(button_frame_bottom, text="Quit", style="mod1.TButton", command=quit_game).pack(side=LEFT, padx=10)





master.mainloop()









# Run the application
master.mainloop()
