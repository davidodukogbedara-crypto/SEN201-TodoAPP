tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted")
    else:
        print("Invalid task number")

def main_menu():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

main_menu()