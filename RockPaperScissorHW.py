from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
window = Tk()
window.title("Rock Paper Scissor")
window.configure(bg="light yellow")
window.geometry("400x400")

title = Label(window, text="ROCK PAPER SCISSORS!!!!", bg="blue", fg="white", padx=10, pady=10, width=30)
title.pack(pady=5)

global choice1
choice1 = random.randint(1, 3)
if choice1 == 1:
    choice1="rock"
elif choice1==2:
    choice1="paper"
else:
    choice1="scissors"

rock = Image.open("rock.jpg")
paper = Image.open("paper.jpg")
scissors = Image.open("scissors.avif")
rock = rock.resize((100, 100))
paper = paper.resize((100, 100))
scissors = scissors.resize((100, 100))
rock1 = ImageTk.PhotoImage(rock)
paper1 = ImageTk.PhotoImage(paper)
scissors1 = ImageTk.PhotoImage(scissors)
rockIMG=Label(window, image=rock1)
paperIMG=Label(window, image=paper1)
scissorsIMG=Label(window, image=scissors1)
rockIMG.pack(pady=5)
paperIMG.pack(pady=5)
scissorsIMG.pack(pady=5)

paperIMG.place(x=25, y=54)
scissorsIMG.place(x=275, y=54)

def pick_rock():
    global choice
    choice = "rock"
    messagebox.showinfo("Choice", "Your pick is now Rock")
def pick_paper():
    global choice
    choice = "paper"
    messagebox.showinfo("Choice", "Your pick is now Paper")
def pick_scissors():
    global choice
    choice = "scissors"
    messagebox.showinfo("Choice", "Your pick is now Scissors")
pickRock=Button(window, text= "Pick Rock!", bg="light blue", fg="black", command=pick_rock)
pickPaper=Button(window, text= "Pick Paper!", bg="light blue", fg="black", command=pick_paper)
pickScissors=Button(window, text= "Pick Scissors!", bg="light blue", fg="black", command=pick_scissors)
pickRock.pack(pady=5)
pickPaper.pack(pady=5)
pickScissors.pack(pady=5)
def results():
    if choice == choice1:
        messagebox.showinfo("Results", "It's a tie! Opponent's pick was: " + choice1)
    elif (choice == "rock" and choice1 == "scissors") or (choice == "paper" and choice1 == "rock") or (choice == "scissors" and choice1 == "paper"):
        messagebox.showinfo("Results", "You win! Opponent's pick was: " + choice1)
    else:
        messagebox.showinfo("Results", "You lose! Opponent's pick was: " + choice1)
def topwin():
    top = Toplevel()
    top.title("Game")
    top.configure(bg="light yellow")
    top.geometry("400x400")
    yourPick=Label(top, text=f"Your pick is: {choice}")
    opponentPick=Label(top, text="Opponent's pick is: ?")
    yourPick.pack(pady=5)
    opponentPick.pack(pady=5)
    end = Button(top, text="Get Results!", bg="green", fg="black", command=results)
    end.pack(pady=5)

play = Button(window, text="Play Game!", bg="red", fg="black", command=topwin)
play.pack(pady=5)

window.mainloop()