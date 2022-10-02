# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
import writer as w
import reader as r
import view as v

db_filename = 'main_db.json'
db2_filename = 'main_db2.json'
main_db_name = 'main'
csv_filename = 'new_user.csv'
new_json_file = 'new_user.json'
data_read = []


# основная программа
def main():
    input_field_list = ['name', 'surname', 'address', 'telephone', 'description']
    while True:
        user_choice = v.main_menu()
        if user_choice == '* 1) посмотреть текущую базу (view_list)    *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            data_read = r.read_json_get_data(db_filename)
            w.index_db(data_read, main_db_name)
            w.write_db_overwrite(data_read, db_filename)
            data_read = r.read_json_get_data(db_filename)
            v.view_list('значение в базе', data_read[main_db_name])
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == '* 2) добавить новую запись в bd             *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            field_values_list = v.input_by_dictionary(input_field_list)
            w.add_person_direct_to_db(db_filename, main_db_name, field_values_list['name'],
                                      field_values_list['surname'],
                                      field_values_list['address'], field_values_list['telephone'],
                                      field_values_list['description'])
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == '* 3) Найти значения по полю в bd            *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            data_read = r.read_json_get_data(db_filename)
            field_input = v.input_by_list(input_field_list)
            value_input = (input(f"введите значение для поиска "))
            result = r._get_from_db(data_read, value_input, "description", field_input, main_db_name)
            if result:
                v.view_list(f'Запрос по полю : "{field_input}", значения : "{value_input}". Совпадение', result)
            else:
                print(f'Запрос по полю : "{field_input}", значения : "{value_input}". Совпадений не найдено!!!!')
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == '* 4) считать файл csv и сохранить в bd      *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            data_read = r.read_csv_get_data(csv_filename)
            w.add_list_to_db(data_read, db_filename, main_db_name)
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == '* 5) сохранить прямой ввод в json           *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            field_values_list = v.input_by_dictionary(input_field_list)
            w.add_person_to_json(new_json_file, field_values_list['name'],
                                      field_values_list['surname'],
                                      field_values_list['address'], field_values_list['telephone'],
                                      field_values_list['description'])
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == '* 6) считать файл json и сохранить в bd     *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            w.add_json_to_db(new_json_file, db_filename, main_db_name)
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == '* 7) удалить запись по индексу              *\n':
            v.task_header_inform(user_choice) # оповещение начала операции
            data_read = r.read_json_get_data(db_filename)
            w.index_db(data_read, main_db_name)
            w.write_db_overwrite(data_read, db_filename)
            v.view_list('значение в базе', data_read[main_db_name])
            w.delete_by_index(data_read, main_db_name, v.input_by_incremental(int(len(data_read[main_db_name]))))
            w.write_db_overwrite(data_read, db_filename)
            v.task_footer_inform(user_choice) # оповещение конца операции
        elif user_choice == 'x':
            break
        else:
            print('введите корректное значение меню')


main()
