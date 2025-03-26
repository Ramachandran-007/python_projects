class Task:
    def __init__(self, id, title, description, priority, status):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority  # High, Medium, Low
        self.status = status     # Pending, In Progress, Completed

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, status):
        # Generate a new ID (simple increment based on list length)
        task_id = len(self.tasks) + 1
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Priority must be High, Medium, or Low")
        if status not in ["Pending", "In Progress", "Completed"]:
            raise ValueError("Status must be Pending, In Progress, or Completed")
        new_task = Task(task_id, title, description, priority, status)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully with ID {task_id}.")

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if priority:
                if priority not in ["High", "Medium", "Low"]:
                    raise ValueError("Priority must be High, Medium, or Low")
                task.priority = priority
            if status:
                if status not in ["Pending", "In Progress", "Completed"]:
                    raise ValueError("Status must be Pending, In Progress, or Completed")
                task.status = status
            print(f"Task ID {task_id} updated successfully.")
        else:
            raise ValueError(f"No task found with ID {task_id}")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task ID {task_id} deleted successfully.")
        else:
            raise ValueError(f"No task found with ID {task_id}")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def filter_tasks_by_priority(self, priority):
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Priority must be High, Medium, or Low")
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks found with priority '{priority}'.")
        else:
            for task in filtered_tasks:
                print(task)


def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                priority = input("Enter priority (High/Medium/Low): ")
                status = input("Enter status (Pending/In Progress/Completed): ")
                manager.add_task(title, description, priority, status)

            elif choice == "2":
                task_id = int(input("Enter task ID to edit: "))
                title = input("Enter new title (press Enter to skip): ") or None
                description = input("Enter new description (press Enter to skip): ") or None
                priority = input("Enter new priority (High/Medium/Low, press Enter to skip): ") or None
                status = input("Enter new status (Pending/In Progress/Completed, press Enter to skip): ") or None
                manager.edit_task(task_id, title, description, priority, status)

            elif choice == "3":
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)

            elif choice == "4":
                manager.view_all_tasks()

            elif choice == "5":
                priority = input("Enter priority to filter (High/Medium/Low): ")
                manager.filter_tasks_by_priority(priority)

            elif choice == "6":
                print("Exiting Task Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()