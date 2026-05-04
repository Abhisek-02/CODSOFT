import tkinter as tk
from tkinter import messagebox

# Creating window using tkinter
root = tk.Tk()
root.title("To-Do List")

# Enter task (text box)
entry_task = tk.Entry(root, width=60)
entry_task.pack(pady=15)

# Display tasks
listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=15)

# Functions
def add_task():
    task = entry_task.get()
    if task:
        listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def update_task():
    try:
        selected_index = listbox.curselection()[0]
        new_task = entry_task.get()
        if new_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run 
root.mainloop()
