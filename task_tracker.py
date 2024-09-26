import argparse
import json
import os
from datetime import datetime
from tabulate import tabulate  # Import tabulate

# File where tasks will be stored
TASKS_FILE = "tasks.json"

# Initialize tasks file if it doesn't exist
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

# Function to load tasks from the file
def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks in a table format
def display_task_table(tasks):
    headers = ["Id", "Description", "Status", "Created At", "Updated At"]
    data = [[task["id"], task["description"], task["status"], task["createdAt"], task["updatedAt"]] for task in tasks]
    print(tabulate(data, headers, tablefmt="fancy_grid"))

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)

    # Print the newly added task in table format
    display_task_table([new_task])

# Update a task
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            save_tasks(tasks)
            # Print the updated task in table format
            display_task_table([task])
            return
    print(f"Task with ID {task_id} not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    task_to_delete = None
    tasks = [task for task in tasks if task["id"] != task_id or (task_to_delete := task)]
    save_tasks(tasks)

    if task_to_delete:
        # Print the deleted task in table format
        print(f"Task {task_id} deleted successfully:")
        display_task_table([task_to_delete])
    else:
        print(f"Task with ID {task_id} not found.")

# Mark a task as in-progress or done
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            save_tasks(tasks)
            # Print the marked task in table format
            display_task_table([task])
            return
    print(f"Task with ID {task_id} not found.")

# List tasks
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if not tasks:
        print("No tasks found.")
        return

    # Print all tasks in table format
    display_task_table(tasks)

# Main function to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # Update a task
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("description", type=str, help="New task description")

    # Delete a task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")

    # Mark task as in-progress or done
    parser_mark = subparsers.add_parser("mark", help="Mark a task as in-progress or done")
    parser_mark.add_argument("id", type=int, help="Task ID")
    parser_mark.add_argument("status", choices=["in-progress", "done"], help="Task status")

    # List tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", nargs='?', choices=["todo", "in-progress", "done"], help="Filter by status")

    args = parser.parse_args()

    # Map commands to functions
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark":
        mark_task(args.id, args.status)
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
