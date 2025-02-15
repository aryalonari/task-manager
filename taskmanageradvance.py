import sys
import json
from datetime import datetime

tasks = []

def add_task(task, start_date, end_date, priority):
    tasks.append({
        "task": task,
        "start_date": start_date,
        "end_date": end_date,
        "priority": priority,
        "completed": False
    })
    print(f'Added task: {task}')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f'Deleted task: {removed_task["task"]}')
    except IndexError:
        print("Invalid task number")

def edit_task(task_index, task, start_date, end_date, priority):
    try:
        tasks[task_index] = {
            "task": task,
            "start_date": start_date,
            "end_date": end_date,
            "priority": priority,
            "completed": tasks[task_index]["completed"]
        }
        print(f'Edited task: {task}')
    except IndexError:
        print("Invalid task number")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f'{i + 1}. {task["task"]} [{task["start_date"]} to {task["end_date"]}] Priority: {task["priority"]} [{status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        print(f'Marked task as completed: {tasks[task_index]["task"]}')
    except IndexError:
        print("Invalid task number")

def show_help():
    print("""
    Available commands:
    - add <task> <start_date YYYY-MM-DD> <end_date YYYY-MM-DD> <priority>: Add a new task
    - delete <task_number>: Delete a task by its number
    - edit <task_number> <task> <start_date YYYY-MM-DD> <end_date YYYY-MM-DD> <priority>: Edit a task
    - view: View all tasks
    - complete <task_number>: Mark a task as completed
    - save <file_name>: Save tasks to a file
    - load <file_name>: Load tasks from a file
    - help: Show this help message
    - exit: Exit the application
    """)

def save_tasks(file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file)
    print(f'Tasks saved to {file_name}')

def load_tasks(file_name):
    global tasks
    try:
        with open(file_name, 'r') as file:
            tasks = json.load(file)
        print(f'Tasks loaded from {file_name}')
    except FileNotFoundError:
        print(f'File {file_name} not found')

def main():
    print("Task Manager Application")
    show_help()
    while True:
        command = input("Enter command: ").strip().split()
        if not command:
            continue
        if command[0] == "add":
            if len(command) >= 5:
                add_task(" ".join(command[1:-3]), command[-3], command[-2], command[-1])
            else:
                print("Invalid command. Usage: add <task> <start_date YYYY-MM-DD> <end_date YYYY-MM-DD> <priority>")
        elif command[0] == "delete":
            if len(command) > 1 and command[1].isdigit():
                delete_task(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif command[0] == "edit":
            if len(command) >= 6 and command[1].isdigit():
                edit_task(int(command[1]) - 1, " ".join(command[2:-3]), command[-3], command[-2], command[-1])
            else:
                print("Invalid command. Usage: edit <task_number> <task> <start_date YYYY-MM-DD> <end_date YYYY-MM-DD> <priority>")
        elif command[0] == "view":
            view_tasks()
        elif command[0] == "complete":
            if len(command) > 1 and command[1].isdigit():
                mark_task_completed(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif command[0] == "save":
            if len(command) > 1:
                save_tasks(command[1])
            else:
                print("Invalid command. Usage: save <file_name>")
        elif command[0] == "load":
            if len(command) > 1:
                load_tasks(command[1])
            else:
                print("Invalid command. Usage: load <file_name>")
        elif command[0] == "help":
            show_help()
        elif command[0] == "exit":
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
