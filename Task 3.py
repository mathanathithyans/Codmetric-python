import os

FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                task, status = line.strip().split("||")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            status = "done" if t["done"] else "pending"
            f.write(f"{t['task']}||{status}\n")

def display_tasks(tasks):
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "🔲"
        print(f"{i}. {status} {t['task']}")

def add_task(tasks):
    task = input("Add task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Delete task number: "))
        tasks.pop(index - 1)
    except:
        print("Invalid number.")

def complete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Mark task number as done: "))
        tasks[index - 1]["done"] = True
    except:
        print("Invalid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View  2. Add  3. Delete  4. Complete  5. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break

main()
