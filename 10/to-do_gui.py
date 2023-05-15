import tkinter as tk
from tkinter import StringVar

def add_task():
    task = task_var.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_var.set("")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")

task_var = StringVar()

task_entry = tk.Entry(root, textvariable=task_var, width=40)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

root.mainloop()
