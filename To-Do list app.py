import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task from the list
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks from the list
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="#f0f0f0")  # Light grey background for the window
root.geometry("600x400")  # Set an initial size
root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
root.grid_columnconfigure(1, weight=1)  # Allow column 1 to expand
root.grid_rowconfigure(1, weight=1)  # Allow row 1 (listbox) to expand

# Task entry field
task_entry = tk.Entry(root, width=35, bg="#d9f9d9", fg="black")
task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Add task button
add_button = tk.Button(root, text="Add Task", width=12, command=add_task, bg="#4caf50", fg="white")
add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, height=10, width=45, selectmode=tk.SINGLE, bg="#fffacd", fg="black")
tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Delete task button
delete_button = tk.Button(root, text="Delete Task", width=12, command=delete_task, bg="#f44336", fg="white")
delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Clear tasks button
clear_button = tk.Button(root, text="Clear All", width=12, command=clear_tasks, bg="#2196f3", fg="white")
clear_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Start the application
root.mainloop()




