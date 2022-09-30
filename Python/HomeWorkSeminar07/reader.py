import json
import csv

# функция чтения json
def read_file_get_data(filename):
    # теперь прочитаем данные из файла 'phone_db.json'
    with open(filename, 'r',  encoding='utf-8') as fp:
        # Чтение файла 'phone_db.json' и преобразование
        # данных JSON в объект Python
        data = json.load(fp)
    return data


# получить запись со словаря
def _get_from_db(dct: dict,  value_to_find, value, field_name):
    result = list(filter(lambda x: x.get(field_name) == value_to_find, dct['peoples']))
    return result if result else False
    # return result[0][value] if result else False # возвращает первую строчку


# открытие csv файла
def open_csv_file(arg_csv_filename):
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
                print(f'Файл содержит столбцы: {", ".join(row)}')
            # Вывод строк
            print(f' {row["name"]} {row["surname"]}', end='')
            print(f' номер телефона {row["telephone"]} описание {row["description"]}.')
            new_data = {'name': row["name"], 'surname': row["surname"], 'telephone': row["telephone"],
                        'description': row["description"]}
            # d = dict(name=row["name"], surname=row["surname"], telephone=row["telephone"], description=row["description"])
            # print(d)
            data_from_csv.append(new_data)
            count += 1
        print(f'Всего в файле {count + 1} строк.')
        print(f'data_from_csv {data_from_csv}')
        return data_from_csv
