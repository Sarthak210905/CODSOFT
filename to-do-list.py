class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({"task": task, "done": False})

    def update(self, N, new):
        if 0 <= N < len(self.tasks):
            self.tasks[N]["task"] = new

    def complete(self, N):
        if 0 <= N < len(self.tasks):
            self.tasks[N]["done"] = True

    def delete(self, N):
        if 0 <= N < len(self.tasks):
            self.tasks.pop(N)

    def list(self):
        for i, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i + 1}. {task['task']} - {status}")


todo = ToDoList()
while True:
        print("\n1. Add Task\n2. Update Task\n3. Complete Task\n4. Delete Task\n5. List Tasks\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            todo.add(task)
        elif choice == "2":
            N = int(input("Enter the task number to update: ")) - 1
            new = input("Enter the new task: ")
            todo.update(N, new)
        elif choice == "3":
            if not todo.tasks:
                print("No tasks to complete.")
                continue
            else:
             N = int(input("Enter the task number to complete: ")) - 1
             todo.complete(N)
        elif choice == "4":
            if not todo.tasks:
                print("No tasks to delete.")
                continue
            else:
             N = int(input("Enter the task number to delete: ")) - 1
             todo.delete(N)
        elif choice == "5":
            todo.list()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
