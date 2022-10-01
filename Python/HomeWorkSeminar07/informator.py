

# функция для отображения чего либо
def view_data(title, data):
    print(f'{title} = {data}')



# функция для отображения чего либо
def view_list(title, data):
    count = 1
    for element in data:
        print(f'{count}) {title} = {element}')
        count += 1


# функция получения обратного словаря вводов
def input_by_dictionary(arg_dictionary, arg_use_input_dict: bool = True):
    if arg_use_input_dict:
        dictionary = arg_dictionary
    else:
        dictionary = ['name', 'surname', 'telephone', 'description']
    values_dictionary = {value: input(f'Укажите {value} для новой записи') for value in dictionary}
    return values_dictionary
