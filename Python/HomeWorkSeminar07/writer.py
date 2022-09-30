import json


# функция записи json
def write_line(filename, arg_data):
    # Открываем файл на запись
    with open(filename, 'w') as fp:
        # Преобразование объекта Python в данные
        # формата JSON, а так же запись в файл 'phone_db.json'
        json.dump(arg_data, fp)


# функция записи напрямую
def add_person_direct_to_db(arg_db_filename, arg_new_username, arg_new_usersurname, arg_new_usertelephone, arg_new_userdiscription):
    # создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
    new_data = {'name': arg_new_username, 'surname': arg_new_usersurname, 'telephone': arg_new_usertelephone, 'description': arg_new_userdiscription}
    with open(arg_db_filename, encoding='utf8') as f: #Открываем файл
        data = json.load(f) # Получае все данные из файла
        data['peoples'].append(new_data) # Добавляем данные
        with open(arg_db_filename, 'w', encoding='utf8') as outfile: #Открываем файл для записи
            json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)


# записываем строчку new_data = {'name': arg_new_username, 'surname': arg_new_usersurname, 'telephone': arg_new_usertelephone, 'description': arg_new_userdiscription} в json file
def add_person_to_file(arg_new_filename, arg_new_username, arg_new_usersurname, arg_new_usertelephone, arg_new_userdiscription):
    new_data = {'name': arg_new_username, 'surname': arg_new_usersurname, 'telephone': arg_new_usertelephone, 'description': arg_new_userdiscription}
    with open(arg_new_filename, 'w', encoding='utf8') as outfile: # Открываем файл для записи
        json.dump(new_data, outfile, ensure_ascii=False, indent=2) # Добавляем данные


# запись листа в базу данных
def add_list_to_db(arg_new_data, arg_db_filename):
    with open(arg_db_filename, encoding='utf8') as db_file: #Открываем файл
        db_data = json.load(db_file) #Получае все данные из файла
        for element in arg_new_data:
            db_data['peoples'].append(element) #Добавляем данные поэлементно
    with open(arg_db_filename, 'w', encoding='utf8') as result_file: # Открываем файл для записи
        json.dump(db_data, result_file, ensure_ascii=False, indent=2) # Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        print(f' добавлена запись {arg_new_data} в базу ')


# функция получения, затем сохранения данных из внешнего файла в базу
def add_file_to_db(arg_new_filename, arg_db_filename):
    with open(arg_new_filename, encoding='utf8') as outer_file:  # Открываем файл
        data_from_file = json.load(outer_file)  # Получае все данные из файла
    with open(arg_db_filename, encoding='utf8') as db_file: #Открываем файл
        db_data = json.load(db_file) #Получае все данные из файла
        db_data['peoples'].append(data_from_file) #Добавляем данные
    with open(arg_db_filename, 'w', encoding='utf8') as result_file: # Открываем файл для записи
        json.dump(db_data, result_file, ensure_ascii=False, indent=2) # Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        print(f'из файла {arg_new_filename} добавлена запись {data_from_file} в базу ')


# подумать как сделать опрос записи переменных
def get_value():
    return int(input('value = '))





