import re


# функция вызова меню
def main_menu():
    # input_field_list = ['name', 'surname', 'address', 'telephone', 'description']
    menu_list = ['********ОСНОВНОЕ МЕНЮ(выберите пункт)********\n']
    menu_list.append('* 1) посмотреть текущую базу (view_list)    *\n')
    menu_list.append('* 2) добавить новую запись в bd             *\n')
    menu_list.append('* 3) Найти значения по полю в bd            *\n')
    menu_list.append('* 4) считать файл csv и сохранить в bd      *\n')
    menu_list.append('* 5) сохранить прямой ввод в json           *\n')
    menu_list.append('* 6) считать файл json и сохранить в bd     *\n')
    menu_list.append('* 7) удалить запись по индексу              *\n')
    menu_list.append('*                                           *\n')
    menu_list.append('* для выхода введите "x"                    *\n')
    menu_list.append('********ОСНОВНОЕ МЕНЮ(x для выхода)**********\n')
    while True:
        print(1 * '\n')  # отступ до формирования меню
        [print(element, end='', flush=True) for element in menu_list]
        print(1 * '\n')  # отступ после формирования меню
        user_choice = input('выберите пункт меню от 1 до 7, или x для выхода = ')
        if re.match("^[x1-7]$", user_choice):
            if user_choice == 'x':
                return user_choice
            else:
                return menu_list[int(user_choice)]


def clean(word):
    return re.sub(r"[`x^+=!?.:;,'\"()-]", " ", word.strip())


# функция для отображения входных данных
def view_data(title, data):
    print(f'{title} = {data}')


# функция для отображения входных данных итерируемая
def view_list(title, data):
    count = 0
    for element in data:
        print(f'{count}) {title} = {element}')
        count += 1


# функция получения обратного словаря вводов
def input_by_dictionary(arg_dictionary, arg_use_input_dict: bool = True):
    if arg_use_input_dict:
        dictionary = arg_dictionary
    else:
        dictionary = ['name', 'surname', 'telephone', 'description']
    values_dictionary = {value: input(f'Укажите {value} для ввода ') for value in dictionary}
    return values_dictionary


# функция получения обратного словаря вводов
def input_by_incremental(arg_lenght):
    input_field_list = []
    for i in range(arg_lenght):
        input_field_list.append(str(i))
    field_input = (input(f"введите индекс для удаления: {input_field_list} "))
    while field_input not in input_field_list:
        field_input = (input(f"введите индекс для удаления: {input_field_list} "))
    return field_input


# функция получения обратного словаря вводов
def input_by_list(arg_list):
    field_input = (input(f"Введите поле по которому будем делать поиск : {arg_list} "))
    while field_input not in arg_list:
        field_input = (input(f"Введите поле по которому будем делать поиск : {arg_list} "))
    return field_input


# косметическая функция для вызова оповещения о начале операции
def task_header_inform(arg_user_choice):
    print(f'****Пользователь выбрал задачу : {arg_user_choice}****')  # оповещение начала операции
    pass


# косметическая функция для вызова оповещения о конце операции
def task_footer_inform(arg_user_choice):
    print(f'****Работа по задаче {arg_user_choice} выполнена****')  # оповещение конца операции
    pass
