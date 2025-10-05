class ToDoList:
    def __init__(self):
        self.todoList = {}


    def add_task(self, task):
        self.todoList[task] = {'completed': False}


    def complete_task(self, task_name):
        if task_name in self.todoList:
            self.todoList[task_name]['completed'] = True

            return

        print("Таска нет в списке")


    def remove_task(self, task_name):
        if task_name in self.todoList:
            del self.todoList[task_name]

            return

        print("Таска нет в списке")


    def list_tasks(self):
        if self.todoList:
            for task, task_status in self.todoList.items():
                print(f'{task} {"✅" if task_status["completed"] else "❌"}')
            print()
        else:
            print('Список пуст')


options = '''\n1. Вывести таски.
2. Добавить таск.
3. Отметить таск, как выполненный.
4. Удалить таск.
5. Выйти из программы\n'''

todo = ToDoList()

func_dict = {
    '1': lambda: todo.list_tasks(),
    '2': lambda: todo.add_task(input('Введите название добавляемого таска: ')),
    '3': lambda: todo.complete_task(input('Введите название выполненного таска: ')),
    '4': lambda: todo.remove_task(input('Введите название удаляемого таска: ')),
}

while True:
    print(options)

    user_input = input('Введите опцию из меню: ').strip()

    if user_input == '5':
        break

    if user_input in func_dict:
        func_dict[user_input]()
    else:
        print('Введите номер опции!')