import csv
import os

# --- To-Do List App ---
# A simple app to manage daily tasks with save/load functionality.

FILENAME = "todo_list.csv"  # Name of the file
tasks = []  # List to store tasks

# Load Funcation it is show the data into csv file
# It will only read the data from the CSV file
# if file is exists and it is stored in list
def load_tasks():
    # Heading of the funcation it tell us what the function is doing
    """Loads tasks from the CSV file into the tasks list."""
    # Checking the file is exists or not
    if os.path.exists(FILENAME):
        try:
            # Opening the file in read mode
            with open(FILENAME, mode="r", newline="") as file:
                # Reading the file
                reader = csv.DictReader(file)
                # Reading the file row by row
                for row in reader:
                    # Adding the row to the list
                    tasks.append(row)
            print(f"Loaded {len(tasks)} tasks from memory.")
        except Exception as e:
            print(f"Error loading tasks: {e}")


# This funcation help to save the task by python built in fun DictWriter()
def save_tasks():
    # Heading of the funcation it tell us what the function is doing
    """Saves the current tasks list to the CSV file.""" 
    try:
            # Checking the list is empty or not
        if not tasks:
            print(f"Error: List is empty! {str(e)}")
            return
            # Opening the file in write mode
        with open(FILENAME, mode="w", newline="") as file:
            fieldnames = ["name", "status"]
            # Creating a DictWriter object to write the data into the file
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Writing the header of the file for now we are writing the header because 
            # we are using DictWriter and it is required to write the header before writing the data
            writer.writeheader()
            # Writing the data into the file by using writerows() method 
            # and it takes a list of dictionaries as an argument and it will write the data into the file
            writer.writerows(tasks) 

        print("Tasks saved successfully!")
    except Exception as e: 
        print(f"Error saving tasks: {e}")


# This funcation help to add the task into the list by taking input from the user
def add_task():
    # Heading of the funcation it tell us what the function is doing
    """Adds a new pending task."""
    name = input("Enter the task name: ")
    # This condition is used to check the task name is empty or not 
    # if it is empty then it will show the error message and 
    # if it is not empty then it will add the task into the list with the status pending
    # strip() method is used to remove the leading and trailing whitespace from the string 
    if name.strip():
        tasks.append({"name": name, "status": "pending"})
        print("Task added!")
    else:
        print("Task name cannot be empty.")


#This funcation help to view the task by showing the index and status of the task
def view_tasks():
 # Heading of the funcation it tell us what the function is doing
    """Displays all tasks with their index and status."""
    # This condition is used to check the list is empty or not 
    # if it is empty then it will show the message that the list is empty and 
    # if it is not empty then it will show the task with the index and status of the task
    if not tasks:
        # \n is used to print the new line before the message
        print("\nYour to-do list is empty.")
        return

    print("\n--- Current Tasks ---")
    # enumerate() function is used to get the index of the task and
    # the task itself and start=1 is used to start the index from 1 instead of 0
    for index, task in enumerate(tasks, start=1):
        # status_icon is used to show the status of the task in a more visual way
        status_icon = "✔️" if task["status"] == "completed" else "❌"
        print(f"{index}. [{status_icon}] {task['name']} ({task['status']})")


# This funcation help to mark the task as complete by taking input
# from the user and changing the status of the task to completed
def mark_complete():
    # Heading of the funcation it tell us what the function is doing
    """Changes a task status to completed based on index."""
    # This condition is used to check the list is empty or not 
    ## view_tasks() funcation is used to show the task with the index and status of the task and
    view_tasks()
    if not tasks:
        return
    # This try block is used to handle the exception 
    # if the user enters the invalid input and it will show the error message
    # if the user enters the invalid input and it will not crash the program
    try:
        #int() function is used to convert the input from the user to an integer and
        # it will be used as the index of the task to mark as complete
        choice = int(input("\nEnter task number to mark as complete: "))
        # This condition is used to check the choice is valid or not
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["status"] = "completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# This funcation help to delete the task by taking input 
# from the user and removing the task from the list based on index
def delete_task():
    # Heading of the funcation it tell us what the function is doing
    """Removes a task from the list based on index."""
    view_tasks()
    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to delete: "))
       # This condition is used to check the choice is valid or not and 
       # if it is valid then it will remove the task from the list and 
       # show the message that the task is deleted and
       # if it is not valid then it will show the error message
        if 1 <= choice <= len(tasks):
            # pop() method is used to remove the task from the list based on index 
            # it will return the removed task and 
            # we can show the name of the removed task in the message
            removed = tasks.pop(choice - 1)
            print(f"Deleted task: {removed['name']}")
    except Exception as e: 
            print(f"Error: Invalid task number! {str(e)}")
    except ValueError:
        print("Error: Please enter a valid number!")


def main():
    # 1. Load data at startup
    load_tasks()

# 2. Main loop to show menu and handle user choices
    while True:
        print("\n" + "=" * 30)
        print("      TO-DO LIST APP")
        print("=" * 30)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")
# 3. Get user choice and call corresponding function
        choice = input("\nChoose an option (1-6): ")
# This condition is used to check the choice of the user and    
# call the corresponding funcation based on the choice and 

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            # Auto-save on exit is a good practice
            save_tasks()
            print("Goodbye!")
            break
# if the choice is invalid then it will show the error message
        else:
            print("Invalid choice.")


# This is the entry point of the program and
# it will call the main funcation to start the program
#  __name__ is a special variable in Python that represents the name of the current module.
if __name__ == "__main__":
    main()
