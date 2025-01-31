import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks
def clear_all():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Create the label
label = tk.Label(root, text="To-Do List", font=("Arial", 16))
label.pack(pady=10)

# Create the entry widget for entering tasks
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Create the button to add tasks
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), width=20, command=add_task)
add_button.pack(pady=5)

# Create the button to delete selected task
delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), width=20, command=delete_task)
delete_button.pack(pady=5)

# Create the button to clear all tasks
clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 14), width=20, command=clear_all)
clear_button.pack(pady=5)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=10)
task_listbox.pack(pady=10)

# Run the main event loop
root.mainloop()
