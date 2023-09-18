# importing packages
from tkinter import *
import tkinter.messagebox
import TASKS as Methods

# function to enter the task in the Listbox

# creating the initial window



window = Tk()
# giving a title
window.title("TO LIST APP")
logo = PhotoImage(file="cropped.png")

w1 = Label(window, image=logo).pack(side="left")
add = Button(window,bg="lightgreen", text="Add task", width=50, command=Methods.addtask)
add.pack(pady=3)

delete = Button(window, bg="lightgreen",text="Delete selected task", width=50, command=Methods.deletetask)
delete.pack(pady=3)

completion = Button(window,bg="lightgreen", text="Completed and Mark ", width=50, command=Methods.markcompleted)
completion.pack(pady=3)
# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()


# to hold items in a listbox
listbox_task = Listbox(frame_task, bg="white", fg="blue", height=15, width=30, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)





window.mainloop()


