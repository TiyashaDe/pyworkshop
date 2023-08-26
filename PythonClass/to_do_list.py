# Initialize an empty list to store tasks
tasks = []

while True:
    print("To-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added!")

    elif choice == '2':
        print("Tasks:")
        for index, task_info in enumerate(tasks, start=1):
            status = "✓" if task_info["completed"] else " "
            print(f"{index}. [{status}] {task_info['task']}")

    elif choice == '3':
        view_choice = input("Enter the number of the task to mark as complete: ")
        try:
            task_index = int(view_choice) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
