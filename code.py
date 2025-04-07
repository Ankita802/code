# code.py

todo_list = {}

def add_task(task_id, description):
    todo_list[task_id] = {"description": description, "completed": False}
    print(f"Added task: {description}")

def complete_task(task_id):
    if task_id in todo_list:
        todo_list[task_id]["completed"] = True
        print(f"Task {task_id} marked as completed.")
    else:
        print("Task ID not found.")

def list_tasks():
    print("\nTo-Do List:")
    for task_id, task in todo_list.items():
        status = "Done" if task["completed"] else "Pending"
        print(f"{task_id}: {task['description']} - {status}")

# Example usage
add_task(1, "Buy groceries")
add_task(2, "Complete Python project")
list_tasks()
complete_task(1)
list_tasks()
