class ToDoList:
    def __init__(self):
        self.todoList = []


    def add_task(self, task):
        self.todoList.append({'name': task, 'completed': False})


    def complete_task(self, task_name):
        for task in self.todoList:
            if task['name'] == task_name and not task['completed']:
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
        if self.todoList:
            for task in self.todoList:
                print(f'{task['name']} {"✅" if task["completed"] else "❌"}')
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