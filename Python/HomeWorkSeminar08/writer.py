import json
import reader


# функция записи json
def write_line(filename, arg_data):
    # Открываем файл на запись
    with open(filename, 'w') as fp:
        # Преобразование объекта Python в данные
        # формата JSON, а так же запись в файл 'main_db.json'
        json.dump(arg_data, fp)


# функция записи напрямую
def add_person_direct_to_db(arg_db_filename, arg_main_db_name, arg_new_username, arg_new_usersurname,
                            arg_new_useraddress,
                            arg_new_usertelephone, arg_new_userdiscription):
    # создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
    new_data = {'name': arg_new_username, 'surname': arg_new_usersurname, 'address': arg_new_useraddress,
                'telephone': arg_new_usertelephone, 'description': arg_new_userdiscription}
    with open(arg_db_filename, encoding='utf8') as inputfile:  # Открываем файл
        data = json.load(inputfile)  # Получае все данные из файла
        data[arg_main_db_name].append(new_data)  # Добавляем данные
        write_db_overwrite(data, arg_db_filename)


# записываем строчку new_data в json file
def add_person_to_json(arg_new_filename, arg_new_username, arg_new_usersurname, arg_new_useraddress, arg_new_usertelephone,
                       arg_new_userdiscription):
    new_data = {'name': arg_new_username, 'surname': arg_new_usersurname, 'address': arg_new_useraddress,
                'telephone': arg_new_usertelephone, 'description': arg_new_userdiscription}
    write_db_overwrite(new_data, arg_new_filename)


# запись листа в базу данных
def add_list_to_db(arg_new_data, arg_db_filename, arg_main_db_name):
    with open(arg_db_filename, encoding='utf8') as db_file:  # Открываем файл
        db_data = json.load(db_file)  # Получае все данные из файла
        for element in arg_new_data:
            db_data[arg_main_db_name].append(element)  # Добавляем данные поэлементно
        write_db_overwrite(db_data, arg_db_filename)
        [print(f' Запись {element} в базу добавлены') for element in arg_new_data]


# функция получения, затем сохранения данных из внешнего файла в базу
def add_json_to_db(arg_new_filename, arg_db_filename, arg_main_db_name):
    with open(arg_new_filename, encoding='utf8') as outer_file:  # Открываем файл
        data_from_file = json.load(outer_file)  # Получае все данные из файла
    with open(arg_db_filename, encoding='utf8') as db_file:  # Открываем файл
        db_data = json.load(db_file)  # Получае все данные из файла
    db_data[arg_main_db_name].append(data_from_file)  # Добавляем данные
    write_db_overwrite(db_data, arg_db_filename)
    print(f'из файла {arg_new_filename} добавлена запись {data_from_file} в базу ')


# функция получения, затем сохранения данных из внешнего файла в базу
def write_db_overwrite(arg_db_data, arg_db_filename):
    with open(arg_db_filename, 'w', encoding='utf8') as result_file:  # Открываем файл для записи
        json.dump(arg_db_data, result_file, ensure_ascii=False,
                  indent=2)  # Добавляем данные (все, что было ДО добавления данных + добавленные данные)


# подумать как сделать опрос записи переменных
def get_value():
    return int(input('value = '))


# функция индексации базы данных
def index_db(arg_data_read, arg_main_db_name):
    list(map(lambda element: element.setdefault('index'), arg_data_read[arg_main_db_name]))
    count = 0
    for element in arg_data_read[arg_main_db_name]:
        element['index'] = count
        count += 1


def delete_by_index(arg_data_read, arg_main_db_name, arg_index_for_deletion):
    arg_data_read[arg_main_db_name] = list(
        filter(lambda element: element['index'] != int(arg_index_for_deletion), arg_data_read[arg_main_db_name]))
