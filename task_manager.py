# Task Manager in Python

def display_tasks(tasks):
    """Prints all tasks in the task list."""
    if tasks:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nNo tasks to display.")

def add_task(tasks):
    """Adds a new task to the task list."""
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print(f"Task added: {new_task}")

def delete_task(tasks):
    """Deletes a task from the task list."""
    display_tasks(tasks)
    if tasks:
        task_index = int(input("Enter task number to delete: "))
        # Ensure the user input is valid
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

def main():
    """Main function to run the task manager application."""
    tasks = []  # List to store tasks
    
    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
