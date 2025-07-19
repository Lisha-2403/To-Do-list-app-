import tkinter as tk
from tkinter import messagebox

# --- Functions ---

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# --- GUI ---

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.resizable(False, False)

# Input field
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="Save Tasks", width=12, command=save_tasks)
save_button.grid(row=0, column=2, padx=5)

# Task list
tasks_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=15)
tasks_listbox.pack(pady=10)

# Load tasks at start
load_tasks()

root.mainloop()