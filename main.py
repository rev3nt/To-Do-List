class ToDoList:
    def __init__(self):
        self.todoList = {}


    def add_task(self, task):
        self.todoList[task] = {'completed': False}


    def complete_task(self, task):
        self.todoList[task]['completed'] = True


    def remove_task(self, task):
        del self.todoList[task]


    def list_tasks(self):
        for task in self.todoList:
            print(f'{task} {'✅' if self.todoList[task]["completed"] else '❌'}')
        print()


todo = ToDoList()

todo.add_task('Заняться пайтоном')

todo.add_task('Потрогать траву')

todo.list_tasks()

todo.complete_task('Заняться пайтоном')

todo.list_tasks()

todo.remove_task('Потрогать траву')

todo.list_tasks()