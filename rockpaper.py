#import required libraries
from tkinter import *
from tkinter import ttk
import random

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of the window
win.geometry("800x950")

#Set the title of the window
win.title("Rock Paper Scissors...")

#Default value for Computer
inbuiltchoice = {
   "0":"Rock",
   "1":"Paper",
   "2":"Scissor"
}

#Disable all the Buttons after first Match
def button_disable():
   rock.config(state= "disabled")
   paper.config(state= "disabled")
   Scissor.config(state= "disabled")

#Define function for Rock
def isrock():
   value = inbuiltchoice[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Yahh! You Won"
   else:
      match_result = "Computer Won"
   label.config(text = match_result)
   player1.config(text="Rock")
   comp.config(text=value)
   button_disable()


# Function for Paper
def ispaper():
    value = inbuiltchoice[str(random.randint(0, 2))]
    if value == "Paper":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Amazingg..You won"
    label.config(text=match_result)
    player1.config(text="Paper")
    comp.config(text=value)
    button_disable()


# Function for Scissor
def isscissor():
    value = inbuiltchoice[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Computer Win"
    elif value == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "You Win... :D"
    label.config(text=match_result)
    player1.config(text="Scissor")
    comp.config(text=value)
    button_disable()


# Reset the Game
def reset():
    rock.config(state="active")
    paper.config(state="active")
    Scissor.config(state="active")
    player1.config(text="Player")
    comp.config(text="Computer")
    label.config(text="")


# Create a LabelFrame
labelframe = LabelFrame(win, text="Rock Paper Scissor", font=('Century 20 bold'), labelanchor="n", bd=5, bg="white",width=600, height=450, cursor="target")
labelframe.pack(expand=True, fill=BOTH)
man= PhotoImage(file='man3.png')
# Label for Player
player1= Label(labelframe, text="You", font=('Helvetica 18 bold'))
player1.place(relx=.18, rely=.1)

rock_btn= PhotoImage(file='rockk.png')
paper_btn=PhotoImage(file='paper3.png')
scissor_btn=PhotoImage(file='scissing.png')
vrs=PhotoImage(file='')

# Label for VS
vs = Label(labelframe, image=vrs, font=('Helvetica 18 bold'), bg="white")
vs.place(relx=.45, rely=.1)

# Label for Computer
comp = Label(labelframe, text="Computer", font=('Helvetica 18 bold'))
comp.place(relx=.65, rely=.1)

# Create a label to display the Conditions
label = Label(labelframe, text="player", font=('Coveat', 25, 'bold'), bg="white")
label.pack(pady=150)

# Create Button Set for Rock, Paper and Scissor
rock= Button(labelframe, image=rock_btn, width=120,height=160,command=isrock)
rock.place(relx=.15, rely=.40)

paper = Button(labelframe,image=paper_btn, font=10, width=120,height=160,command=ispaper)
paper.place(relx=.40, rely=.40)

Scissor = Button(labelframe, image=scissor_btn, font=10, width=120,height=162,command=isscissor)
Scissor.place(relx=.60, rely=.40)

# Button to reset the Game
again= PhotoImage(file='playagian.png')
reset = Button(labelframe, image=again, fg="white", width=70,height=100, font=10,command=reset)
reset.place(relx=.8, rely=.45)
win.mainloop()