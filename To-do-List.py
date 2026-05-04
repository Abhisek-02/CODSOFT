import tkinter as tk
from tkinter import messagebox

# Creating window using tkinter
root = tk.Tk()
root.title("To-Do List")

# Enter task (text box)
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Display tasks
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def update_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
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
