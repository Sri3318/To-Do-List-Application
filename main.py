import tkinter as tk
from tkinter import messagebox
import pickle

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        if index < len(task_list):  # Ensure index exists
            del task_list[index]  # Remove from list
            listbox.delete(index)  # Remove from Listbox
    else:
        messagebox.showwarning("Warning", "Select a task to remove!")

def mark_done():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        if index < len(task_list):  # Ensure index exists
            item = task_list[index]

            # Toggle checkmark
            if item.startswith("✅"):
                task_list[index] = item[1:]  # Remove checkmark
            else:
                task_list[index] = "✅" + item  # Add checkmark

            # Update Listbox
            listbox.delete(index)
            listbox.insert(index, task_list[index])
    else:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

def save_tasks():
    with open("tasks.pkl", "wb") as f:
        pickle.dump(task_list, f)
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    global task_list
    try:
        with open("tasks.pkl", "rb") as f:
            task_list = pickle.load(f)
            listbox.delete(0, tk.END)  # Clear Listbox before loading
            for task in task_list:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        task_list = []
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load tasks: {e}")

# Main Application Window
app = tk.Tk()
app.title("To-Do List")
app.geometry("500x500")
app.config(bg="#242424")

# Task List Storage
task_list = []

# Title Label
title = tk.Label(app, text="To-Do List", font=("Consolas", 18), bg="#242424", fg="#fff")
title.pack(pady=10)

# Task Entry
task_entry = tk.Entry(app, width=40, font=("Consolas", 12))
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(app, bg="#242424")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add", width=10, font=("Consolas", 12), command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove", width=10, font=("Consolas", 12), command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

mark_button = tk.Button(button_frame, text="Mark Done", width=12, font=("Consolas", 12), command=mark_done)
mark_button.grid(row=1, column=0, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", width=10, font=("Consolas", 12), command=save_tasks)
save_button.grid(row=1, column=1, padx=5, pady=5)

load_button = tk.Button(button_frame, text="Load", width=10, font=("Consolas", 12), command=load_tasks)
load_button.grid(row=1, column=2, padx=5, pady=5)

# Task Listbox
listbox = tk.Listbox(app, height=15, width=50, font=("Consolas", 12))
listbox.pack(pady=10)

# Run App
app.mainloop()
