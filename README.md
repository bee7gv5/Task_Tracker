# Task Tracker CLI

A simple command-line interface (CLI) application for tracking tasks. You can add, update, delete, and mark tasks as "in-progress" or "done." This application also supports listing tasks based on their status.

## Features:
- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as "in-progress" or "done"
- List all tasks or filter by status

## Task Properties:
- `id`: Unique identifier for the task
- `description`: Short description of the task
- `status`: The current status (todo, in-progress, done)
- `createdAt`: Timestamp of when the task was created
- `updatedAt`: Timestamp of the most recent update

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/bee7gv5/Task_Tracker.git

2. Navigate to the project directory:
   ```bash
   cd TaskTrackerCLI
3. Run the Task Tracker CLI:
   ```bash
   python task_tracker.py

## Usage Examples

1. Adding a Task
   ```bash
   python task_tracker.py add "Visit grandma"

2. Updating a Task
   ```bash
   python task_tracker.py update 1 "Visit grandma and bring flowers"

3. Deleting a Task
   ```bash
    python task_tracker.py delete 1

4. Listing Tasks
   ```bash
   python task_tracker.py list

5. Marking a Task as In-Progress or Done
   ```bash
   python task_tracker.py mark 1 in-progress
   ```
   
   ```bash
   python task_tracker.py mark 1 done

## Data Storage
Tasks are stored in a JSON file (tasks.json) in the project directory. This file will be automatically created when you add your first task.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Sample solution for the [Task Tracker CLI](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.s).
