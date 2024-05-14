class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = '[x]' if self.completed else '[ ]'
        return f'{status} {self.description}'

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_completed(self, task_number):
        try:
            self.tasks[task_number - 1].completed = True
        except IndexError:
            print('Invalid task number.')

def main():
    todo_list = ToDoList()
    while True:
        print('\n1. Add task\n2. View tasks\n3. Mark completed\n4. Quit')
        option = input('Choose an option: ')
        if option == '1':
            task = input('Enter a task: ')
            todo_list.add_task(Task(task))
        elif option == '2':
            todo_list.view_tasks()
        elif option == '3':
            task_number = int(input('Enter the task number to mark as completed: '))
            todo_list.mark_completed(task_number)
        elif option == '4':
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()