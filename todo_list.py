tasks = []
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        try:
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed}")
        except:
            print("Invalid task number!")
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")