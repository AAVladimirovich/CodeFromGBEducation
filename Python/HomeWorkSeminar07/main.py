# Домашнее задание:
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# нескольких форматах.
# под форматами понимаем структуру файлов, например:в файле на одной строке
# хранится одна часть записи, пустая строка - разделитель

# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
# (разделитель - пробел)
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2

# и т.д.в файле на одной строке хранится все записи, символ разделитель - ;
# Фамилия_1,Имя_1,Телефон_1,Описание_1
# Фамилия_2,Имя_2,Телефон_2,Описание_2
# и т.д.

import writer
import reader
import informator

db_filename = 'phone_db.json'
csv_filename = 'new_user.csv'
new_json_file = 'new_user.json'
data_read = []

def menu():
    input_field_list = ['name', 'surname', 'telephone', 'description']
    while True:
        print('*' * 16, "ОСНОВНОЕ МЕНЮ", '*' * 16 + '\n'
              '* 1) считать с файла csv и сохранить в bd     *\n'           
              '* 2) создать файл Json                        *\n'                                      
              '* 3) загрузить данные с Json файла            *\n'
              '* 4) записать данные напрямую                 *\n'
              '* 5) Посмотреть текущую базу                  *\n'
              '* 6) Найти значения по полю в базе            *\n'
              '*                                             *\n'
              '* для выхода введите "x"                      *\n' +
              '*' * 16, "ОСНОВНОЕ МЕНЮ", '*' * 16 + '\n'
              )
        user_choice = input('выберите операцию = ')
        if user_choice == '1':
            data_read = reader.open_csv_file(csv_filename)
            writer.add_list_to_db(data_read, db_filename)
        if user_choice == '2':
            field_values = informator.input_by_dictionary(input_field_list)
            writer.add_person_to_file(new_json_file, field_values['name'], field_values['surname'], field_values['telephone'], field_values['description'])
        if user_choice == '3':
            writer.add_file_to_db(new_json_file, db_filename)
        elif user_choice == '4':
            field_values = informator.input_by_dictionary(input_field_list)
            writer.add_person_direct_to_db(db_filename, field_values['name'], field_values['surname'], field_values['telephone'], field_values['description'])
        elif user_choice == '5':
            data_read = reader.read_file_get_data(db_filename)
            informator.view_list('значение в базе', data_read['peoples'])
            # print(data_read['peoples'][3]['telephone'])
            # print(data_read['peoples'][2]['telephone'])
        elif user_choice == '6':
            data_read = reader.read_file_get_data(db_filename)
            field_input = (input(f"введите название поля по которому будем искать: {input_field_list} "))
            while field_input not in input_field_list:
                field_input = (input(f"введите название поля по которому будем искать: {input_field_list} "))
            value_input = (input(f"введите значение для поиска "))
            result = reader._get_from_db(data_read, value_input, "telephone", field_input)
            if result:
                informator.view_list(f'Запрос по полю : "{field_input}", значения : "{value_input}". Совпадение', result)
            else:
                print(f'Запрос по полю : "{field_input}", значения : "{value_input}". Совпадений не найдено!!!!')
        elif user_choice == 'x':
            break
        else:
            print('введите корректное значение меню')


menu()
