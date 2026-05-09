import csv
import os

# --- To-Do List App ---
# A simple app to manage daily tasks with save/load functionality.

FILENAME = "todo_list.csv"
tasks = []

def load_tasks():
    """Loads tasks from the CSV file into the tasks list."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(row)
            print(f"Loaded {len(tasks)} tasks from memory.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

def save_tasks():
    """Saves the current tasks list to the CSV file."""
    try:
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ["name", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(tasks)
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task():
    """Adds a new pending task."""
    name = input("Enter the task name: ")
    if name.strip():
        tasks.append({"name": name, "status": "pending"})
        print("Task added!")
    else:
        print("Task name cannot be empty.")

def view_tasks():
    """Displays all tasks with their index and status."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Current Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status_icon = "✔" if task['status'] == 'completed' else "❌"
        print(f"{index}. [{status_icon}] {task['name']} ({task['status']})")

def mark_complete():
    """Changes a task status to completed based on index."""
    view_tasks()
    if not tasks: return
    
    try:
        choice = int(input("\nEnter task number to mark as complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]['status'] = 'completed'
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Removes a task from the list based on index."""
    view_tasks()
    if not tasks: return

    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted task: {removed['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    # 1. Load data at startup
    load_tasks()

    while True:
        print("\n" + "="*30)
        print("      TO-DO LIST APP")
        print("="*30)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            # Auto-save on exit is a good practice
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
