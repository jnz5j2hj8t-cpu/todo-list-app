tasks = []

def add_task(tasks):
    task_name = input("Enter task: ")
    task = {
    "title" : task_name,
    "completed" : False
    }
    tasks.append(task)
    print("Task added!")

def show_tasks(tasks):
    print()
    print("===== To-Do List =====")
    print()

    if tasks:
        for i, task in enumerate(tasks):
            if task["completed"]:
                print(f"{i + 1}. [✔︎]{task['title']}")
            else:
                print(f"{i + 1}. [ ]{task['title']}")
    else:
        print("No tasks found.")

def complete_task(tasks):
    show_tasks(tasks)
    print()
    task_number = int(input("Enter task number: "))

    if task_number >= 1 and task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid number.")

def remove_task(tasks):
    show_tasks(tasks)
    task_number = int(input("Enter task number: "))
    if task_number >= 1 and task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task removed!")
        print()
        show_tasks(tasks)
    else:
        print("Invalid number.")

def save_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']}, {task['completed']}\n")

    print("Data saved successfully!")

def load_from_file(tasks):
    tasks.clear()
    with open("tasks.txt", "r") as file:
        for line in file:
            parts = line.split(",")
            completed = parts[1].strip()== "True"
            task = {
                "title" : parts[0],
                "completed" : completed
            }
            tasks.append(task)
            
    print("Data loaded successfully!")

choice = 0

while choice != 7:
    print()
    print("===== To-Do List =====")
    print()
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Complete task")
    print("5. Save to file")
    print("6. Load from file")
    print("7. Exit")
    print()
    choice = int(input("Choose: "))

    if choice == 1:
        add_task(tasks)

    elif choice == 2:
        show_tasks(tasks)

    elif choice == 3:
        remove_task(tasks)

    elif choice == 4:
        complete_task(tasks)

    elif choice == 5:
        save_to_file(tasks)

    elif choice == 6:
        load_from_file(tasks)

    elif choice == 7:
        print("Goodbye!")

    else:
        print("Invalid choice.")