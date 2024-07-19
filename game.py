import tkinter as tk
import random

def comp_choice():
    global a
    a = random.randint(1, 3)
    
player = 0
comp = 0

def Tie():
    append_output("Tie\n")

def Compwin():
    global comp
    comp += 1
    append_output("+1 for Comp\n")

def Playerwin():
    global player
    player += 1
    append_output("+1 for player\n")

def whowon():
    if player > comp:
        append_output('Player Won\n')
    elif player == comp:
        append_output('Its a Tie LEL\n')
    else:
        append_output('Computer Won~ GET GOOD NUB\n')

def start_game():
    global rounds, counter
    rounds = int(entry_rounds.get())
    counter = 0
    entry_rounds.delete(0, tk.END)
    append_output(f"Starting game with {rounds} rounds.\n")
    next_round()
def fun():
    comments=["maybe try rock this time","try your luck with paper ig","how about i beat you this time","maybe im just better","Rock,Paper or um Scissors","hah im better"]
    fun_string=random.choice(comments)
    return fun_string

def next_round():
    global rounds, counter
    if rounds > 0:
        rounds -= 1
        comp_choice()
        counter += 1
        comm=fun()
        append_output(f"Round {counter}\n{comm}\n")
        entry_user_input.config(state=tk.NORMAL)
        entry_user_input.focus()
    else:
        whowon()
        append_output("Game Over. Do you want to play again? (yes/no):\n")
        entry_user_input.config(state=tk.NORMAL)

def process_input(event=None):
    userinput = entry_user_input.get()
    entry_user_input.delete(0, tk.END)
    loweruserinput = str.lower(userinput)
    
    if userinput in ['yes', 'no']:
        if userinput == 'yes':
            reset_game()
        else:
            append_output("Thanks for playing!\n")
            entry_user_input.config(state=tk.DISABLED)
        return

    if loweruserinput not in ['rock', 'paper', 'scissors']:
        append_output("Invalid input! Please enter rock, paper, or scissors.\n")
        return

    entry_user_input.config(state=tk.DISABLED)
    if loweruserinput == 'rock':
        if a == 1:
            append_output("Comp Shows Rock🗿\n")
            Tie()
        elif a == 2:
            append_output("Comp Shows Paper📝\n")
            Compwin()
        else:
            append_output("Comp Shows Scissors✂️\n")
            Playerwin()
    elif loweruserinput == 'paper':
        if a == 1:
            append_output("Comp Shows Rock🗿\n")
            Playerwin()
        elif a == 2:
            append_output("Comp Shows Paper📝\n")
            Tie()
        else:
            append_output("Comp Shows Scissors✂️\n")
            Compwin()
    else:  # scissors
        if a == 1:
            append_output("Comp Shows Rock🗿\n")
            Compwin()
        elif a == 2:
            append_output("Comp Shows Paper📝\n")
            Playerwin()
        else:
            append_output("Comp Shows Scissors✂️\n")
            Tie()

    append_output(f"Player Score: {player}\n")
    append_output(f"Computer Score: {comp}\n")
    
    next_round()

def reset_game():
    global player, comp
    player = 0
    comp = 0
    append_output("Enter the number of rounds you want to play:\n")
    entry_rounds.config(state=tk.NORMAL)
    entry_rounds.focus()

# ~~GUI~~
def append_output(text):
    output_text.insert(tk.END, text)
    output_text.see(tk.END)

root = tk.Tk()
root.title("Rock Paper Scissors GUI")
custom_font=("Brownie Stencil",16)
output_text = tk.Text(root, wrap=tk.WORD, height=20, width=50,font=custom_font)
output_text.pack(pady=10)
entry_rounds = tk.Entry(root, width=50)
entry_rounds.pack()
entry_rounds.bind("<Return>", lambda event: start_game())
append_output("Enter the number of rounds you want to play:\n")

entry_user_input = tk.Entry(root, width=50)
entry_user_input.pack()
entry_user_input.bind("<Return>", process_input)
entry_user_input.config(state=tk.DISABLED)

root.mainloop()
