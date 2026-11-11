
tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["done"] else "Pending"
            print(i, task["task"], "-", status)

def complete_task():
    view_tasks()
    num = int(input("Enter task number: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        print("Task completed!")
    else:
        print("Invalid task number")

def delete_task():
    view_tasks()
    num = int(input("Enter task number: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!")
    else:
        print("Invalid task number")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
      
