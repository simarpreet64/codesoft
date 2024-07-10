class My_ToDoList:
    def __init__(self):
        self.tasks = []

    def add_newtask(self, task):
        self.tasks.append(task)

    def remove_anytask(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")

    def update_anytask(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
        else:
            print("Task not found!")

    def display_thetasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")


def main():
    todo_list = My_ToDoList()

    while True:
        print("\n1. Add The New Task Which You Want:")
        print("2. Remove The Task:")
        print("3. Update The Task:")
        print("4. Display The Tasks:")
        print("5. Exit!!!!")

        choice = input("Please Enter your choice: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            todo_list.add_newtask(task)
            print("Congratulations!!,Task added successfully!")
        elif choice == "2":
            task = input("Enter which task to remove: ")
            todo_list.remove_anytask(task)
            print("Congratulations!!,Task removed successfully!")
        elif choice == "3":
            old_task = input("Enter which task to update: ")
            new_task = input("Enter new task: ")
            todo_list.update_anytask(old_task, new_task)
            print("Congratulations!!,Task updated successfully!")
        elif choice == "4":
            todo_list.display_thetasks()
        elif choice == "5":
            print("Exiting program........")
            break
        else:
            print("Error occurs??????")


if __name__ == "__main__":
    main()
