task=[]

def add_task():
    task_name = input("enter task name ")
    task.append(task_name)
    print("Task added successfully")

def remove_task():
    task_name = input("Enter task to be removed ")
    if task_name in task:
        task.remove(task_name)
        print("Task removed successfully")
    else:
        print("Task not found")

def view_task():
    if task:
        print("Task: ")
        for t in task:
            print(f"- {t}")
    else:
        print("No tasks available.")

def mark_task_completed():
    task_name = input("Enter task to mark as completed: ")
    if task_name in task:
        print(f"Task '{task_name}' marked as completed.")
        task.remove(task_name)
    else:
        print("Task not found")

def count_tasks():
    print(f"Total Tasks: {len(task)}")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task Completed")
        print("5. Count Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_task()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            count_tasks()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice")
main()
