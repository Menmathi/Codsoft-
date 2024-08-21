import tkinter as tk
from tkinter import messagebox
tasks = []
task_id = 1
def add_task():
    global task_id
    task_description = task_entry.get()
    if not task_description:
        messagebox.showwarning("Input Error", "Please enter a task description.")
        return
    task = {
        'id': task_id,
        'description': task_description,
        'status': 'Pending'
    }
    tasks.append(task)
    task_listbox.insert(tk.END, f"{task_id}. {task_description} (Pending)")
    task_id += 1
    task_entry.delete(0, tk.END)

def update_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Selection Error", "Please select a task to update.")
        return

    task_description = task_entry.get()
    if not task_description:
        messagebox.showwarning("Input Error", "Please enter a new task description.")
        return

    selected_task_id = int(task_listbox.get(selected_task_index).split('.')[0])
    for task in tasks:
        if task['id'] == selected_task_id:
            task['description'] = task_description
            task['status'] = 'Pending'
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, f"{task['id']}. {task_description} (Pending)")
            break

def delete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return

    selected_task_id = int(task_listbox.get(selected_task_index).split('.')[0])
    global tasks
    tasks = [task for task in tasks if task['id'] != selected_task_id]
    task_listbox.delete(selected_task_index)

def mark_as_completed():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
        return

    selected_task_id = int(task_listbox.get(selected_task_index).split('.')[0])
    for task in tasks:
        if task['id'] == selected_task_id:
            task['status'] = 'Completed'
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, f"{task['id']}. {task['description']} (Completed)")
            break

root = tk.Tk()
root.title("To-Do List Application")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", width=15, command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", width=15, command=mark_as_completed)
complete_button.pack(pady=5)

root.mainloop()
