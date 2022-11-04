import json
import csv

# функция чтения json
def read_json_get_data(filename):
    # теперь прочитаем данные из файла 'main_db.json'
    with open(filename, 'r',  encoding='utf-8') as fp:
        # Чтение файла 'main_db.json' и преобразование
        # данных JSON в объект Python
        data = json.load(fp)
    return data


# получить запись со словаря
def _get_from_db(dct: dict,  value_to_find, value, field_name, arg_main_db_name):
    result = list(filter(lambda element: element.get(field_name) == value_to_find, dct[arg_main_db_name]))
    return result if result else False
    # return result[0][value] if result else False # возвращает первую строчку


# открытие csv файла
def read_csv_get_data(arg_csv_filename):
    with open(arg_csv_filename, encoding='utf-8') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        data_from_csv = []
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", [".join(row)}+"]"')
            # Вывод строк
            print(f' {row["name"]} {row["surname"]}', end='')
            print(f' номер телефона {row["telephone"]} описание {row["description"]}.')
            new_data = {'name': row["name"], 'surname': row["surname"], 'address': row["address"], 'telephone': row["telephone"],
                        'description': row["description"]}
            # d = dict(name=row["name"], surname=row["surname"], telephone=row["telephone"], description=row["description"])
            # print(d)
            data_from_csv.append(new_data)
            count += 1
        print(f'Всего в файле {count + 1} строк.')
        return data_from_csv
