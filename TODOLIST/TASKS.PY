import todolisting as todo


def addtask():
    # A new window to pop up to take input
    input_text = ""

    def add():
        input_text = adding.get(1.0, "end-1c")
        if input_text == "":
            todo.tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            todo.listbox_task.insert(todo.END, input_text)
            # close the root1 window
            root1.destroy()

    root1 = todo.Tk()
    root1.title("Add task")
    adding = todo.Text(root1, width=40, height=20)
    adding.pack()
    button_temp = todo.Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()


# function to facilitate the delete task from the Listbox
def deletetask():
    # selects the slected item and then deletes it
    selected = todo.listbox_task.curselection()
    todo.listbox_task.delete(selected[0])


# Executes this to mark completed

def markcompleted():
    marked = todo.listbox_task.curselection()
    temp = marked[0]
    # store the text of selected item in a string
    temp_marked = todo.listbox_task.get(marked)
    # update it
    temp_marked = temp_marked + " Completed"
    # delete it then insert it
    todo.listbox_task.delete(temp)
    todo.listbox_task.insert(temp, temp_marked)

