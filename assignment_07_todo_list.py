# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def display_menu():
    """Prints the interactive to-do list menu."""
    print("============================")
    print("      TO-DO LIST MENU       ")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompts for a new task description and appends it to the tasks list."""
    description = input("Enter task: ").strip()
    if description:
        tasks.append(description)
        print(f'Task added: "{description}"')
    else:
        print("Error: Task description cannot be empty.")


def view_tasks(tasks):
    """Displays all current tasks with 1-based index numbers."""
    if not tasks:
        print("Your to-do list is currently empty.")
        return

    print("Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    """
    Shows tasks and prompts the user for a 1-based index number to delete.
    Validates choice bounds and handles non-numeric input gracefully.
    """
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        # Convert 1-based user input to 0-based Python list index
        index = task_num - 1

        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number. Please try again.")
    except ValueError:
        print("Error: Please enter a valid number.")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        print()  # Spacer line for clean UI formatting

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 4.")

        print()  # Spacer line before repeating the menu cycle


if __name__ == "__main__":
    main()