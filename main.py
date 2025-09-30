class ToDoList:
    def __init__(self):
        self.todoList = []


    def add_task(self, task):
        self.todoList.append({'name': task,'completed': False})


    def complete_task(self, task_name):
        for task in self.todoList:
            if task['name'] == task_name:
                task['completed'] = True

                return

        print("Таска нет в списке")


    def remove_task(self, task_name):
        for task in self.todoList:
            if task['name'] == task_name:
                self.todoList.remove(task)

                return

        print("Таска нет в списке")


    def list_tasks(self):
        if len(self.todoList) != 0:
            for task in self.todoList:
                print(f'{task["name"]} {"✅" if task["completed"] else "❌"}')
            print()
        else:
            print('Список пуст')


todo = ToDoList()

todo.list_tasks()

todo.add_task('Заняться пайтоном')

todo.add_task('Потрогать траву')

todo.list_tasks()

todo.complete_task('Заняться пайтоном')

todo.list_tasks()

todo.remove_task('Потрогать траву')

todo.list_tasks()