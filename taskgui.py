import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TaskManager:
    def __init__(self, root):
        self.tasks = []

        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x500")
        self.root.config(bg="#e1f5fe")

        # Style configurations
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        self.button_bg = "#0288d1"
        self.button_fg = "#ffffff"

        # Task input frame
        self.input_frame = tk.Frame(root, bg="#e1f5fe")
        self.input_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.task_label = tk.Label(self.input_frame, text="Task:", font=self.label_font, bg="#e1f5fe")
        self.task_label.grid(row=0, column=0, pady=5, sticky="w")
        self.task_entry = tk.Entry(self.input_frame, font=self.entry_font)
        self.task_entry.grid(row=0, column=1, pady=5)

        self.start_date_label = tk.Label(self.input_frame, text="Start Date (YYYY-MM-DD):", font=self.label_font, bg="#e1f5fe")
        self.start_date_label.grid(row=1, column=0, pady=5, sticky="w")
        self.start_date_entry = tk.Entry(self.input_frame, font=self.entry_font)
        self.start_date_entry.grid(row=1, column=1, pady=5)

        self.end_date_label = tk.Label(self.input_frame, text="End Date (YYYY-MM-DD):", font=self.label_font, bg="#e1f5fe")
        self.end_date_label.grid(row=2, column=0, pady=5, sticky="w")
        self.end_date_entry = tk.Entry(self.input_frame, font=self.entry_font)
        self.end_date_entry.grid(row=2, column=1, pady=5)

        self.add_task_button = tk.Button(self.input_frame, text="Add Task", font=self.button_font, bg=self.button_bg, fg=self.button_fg, command=self.add_task)
        self.add_task_button.grid(row=3, columnspan=2, pady=10)

        # Task list frame
        self.list_frame = tk.Frame(root, bg="#e1f5fe")
        self.list_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.tasks_listbox = tk.Listbox(self.list_frame, font=self.entry_font)
        self.tasks_listbox.pack(pady=5, fill="both", expand=True)

        self.view_tasks()

        # Task actions frame
        self.actions_frame = tk.Frame(root, bg="#e1f5fe")
        self.actions_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.complete_task_button = tk.Button(self.actions_frame, text="Complete Task", font=self.button_font, bg=self.button_bg, fg=self.button_fg, command=self.mark_task_completed)
        self.complete_task_button.grid(row=0, column=0, pady=10)

        self.delete_task_button = tk.Button(self.actions_frame, text="Delete Task", font=self.button_font, bg=self.button_bg, fg=self.button_fg, command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        start_date = self.start_date_entry.get().strip()
        end_date = self.end_date_entry.get().strip()

        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        if task and start_date and end_date:
            self.tasks.append({"task": task, "start_date": start_date, "end_date": end_date, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.start_date_entry.delete(0, tk.END)
            self.end_date_entry.delete(0, tk.END)
            self.view_tasks()
        else:
            messagebox.showwarning("Error", "Task and dates cannot be empty!")

    def delete_task(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            removed_task = self.tasks.pop(task_index)
            self.view_tasks()
            messagebox.showinfo("Success", f"Deleted task: {removed_task['task']}")
        except IndexError:
            messagebox.showwarning("Error", "Please select a task to delete")

    def view_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        if not self.tasks:
            self.tasks_listbox.insert(tk.END, "No tasks available")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                self.tasks_listbox.insert(tk.END, f'{i + 1}. {task["task"]} [{task["start_date"]} to {task["end_date"]}] [{status}]')

    def mark_task_completed(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            self.tasks[task_index]["completed"] = True
            self.view_tasks()
            messagebox.showinfo("Success", f"Marked task as completed: {self.tasks[task_index]["task"]}")
        except IndexError:
            messagebox.showwarning("Error", "Please select a task to mark as completed")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
