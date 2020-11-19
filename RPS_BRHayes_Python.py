''' Rock Paper Scissors for BMO Cap. Markets by BRHayes '''

from random import randint as r
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox as mb
from tkinter import Label
from tkinter import Text
from tkinter import Frame

#GLOBAL VARS
winStreak = 0 # initalize global var winstreak
highScore = 0

class RPS:
    def __init__(self, master):

        # CHANGE MASTER WINDOW TITLE, PREVENT RESIZING AND CHANGE BG COLOUR
        master.title('SIMPLE ROCK, PAPER, SCISSORS')
        master.resizable(False, False)
        master.configure(background='#00ff15')

        # CREATE A STYLE OBJECT AND CHANGE THE STYLE OF ALL WIDGETS
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#00ff15')  # Frame Style
        self.style.configure('TButton', background='#00ff15')  # Button Style
        # Label Style
        self.style.configure(
            'TLabel', background='#00ff15', font=('Arial', 11))
        # Header style
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        # CREATE FRAME TO WORK IN
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # HEADING
        ttk.Label(self.frame_header, text='Super Rock, Paper, Scissors!',
                  style='Header.TLabel').grid(row=0, column=1)
        # HEADING DESCRIPTION
        ttk.Label(self.frame_header, wraplength=300,
                  text=("I'm glad to see you want to play Rock, Paper, Scissors with me.\n\n"
                        "To play, make a choice using one of action buttons below.\n")).grid(row=1, column=1)

         # CREATE A SECOND FRAME FOR THE CHOICE BY USER
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Button(self.frame_content, text = "Rock", command = lambda: self.game('R')).grid(
            row=0, column=0, padx=5, sticky='sw')
        ttk.Button(self.frame_content, text='Paper', command = lambda: self.game('P')).grid(
            row=0, column=1, padx=5, sticky='sw')
        ttk.Button(self.frame_content, text='Scissors', command = lambda: self.game('S')).grid(
            row=0, column=2, padx=5, sticky='sw')
        
        #EXIT
        self.style.configure('E.TButton', font =
               ('calibri', 10, 'bold', 'underline'), 
                foreground = 'red') 
        ttk.Button(self.frame_content, text='EXIT GAME', style = 'E.TButton',
                   command=lambda: self.quitt(master)).grid(row=4, column=1, padx=5, pady=5, sticky='n')
        
    # FUNCTION TO QUIT 
    def quitt(self, master):
        global highScore
        msgResult = mb.askokcancel(title = 'Quit', message = 'Are you sure you want to quit?')
        if msgResult == True:
            print(f"Thank you for playing with us today!  Your best winning streak was: {highScore}")
            master.destroy()
    
    # FUNCTION TO PLAY COMP AGAINST PERSON
    def game(self, playerChoice):
        global winStreak
        global highScore

        #REQUIRED VARS
        options = ["R", "P", "S"]
        fullname = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    

        #Computer Choice of Play
        compChoice = options[r(0, 2)] # 1/3 chance picking rock = r, paper = p, or scissors = s.

        if playerChoice == compChoice:
            print(f"Unfortunately you tied. You both picked {playerChoice}. This still resets your streak.")
            winStreak = 0
        elif playerChoice == "R": # player chose rock & comp didnt
            if compChoice == "S":
                print(f"You won this battle! {fullname.get(playerChoice)} breaks {fullname.get(compChoice)}.")
                winStreak += 1
            else:
                print(f"Oh no!  You lost this one. {fullname.get(compChoice)} covers {fullname.get(playerChoice)}.")
                winStreak = 0
        elif playerChoice == "P": # player chose paper and comp didnt
            if compChoice == "R":
                     print(f"You won this battle! {fullname.get(playerChoice)} covers {fullname.get(compChoice)}.")
                     winStreak += 1
            else:
                print(f"Oh no!  You lost this one. {fullname.get(compChoice)} cuts {fullname.get(playerChoice)}.")
                winStreak = 0

        elif playerChoice == "S":
            if compChoice == "P":
                     print(f"You won this battle! {fullname.get(playerChoice)} cuts {fullname.get(compChoice)}.")
                     winStreak += 1
            else:
                print(f"Oh no!  You lost this one. {fullname.get(compChoice)} breaks {fullname.get(playerChoice)}.")
                winStreak = 0
        else:
            print("IDK how, but you broke my game... This is not a valid play.")

        #PRINT SCORE DETAILS AND SPACING
        if winStreak > highScore:
            highScore = winStreak
        
        if winStreak > 0:
            print(f"Congratulations, you're making progress. You are on a {winStreak} time win streak!")

        print(f"The best win streak during this runtime is: {highScore}")
        print("\n")



            

# MAIN FUNCTION & LOOP
def main():
    
    root = Tk()  # DEFINE ROOT NODE WINDOW
    rps = RPS(root)  # STORE OUTCOME
    root.mainloop()  # RUN LOOP ON ROOT


# FORCE READ OF ENTIRE PROGRAM BEFORE COMPILE
if __name__ == "__main__":
    main()
