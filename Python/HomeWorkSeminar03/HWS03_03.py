# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import FunctionHolder as hh  # hh - homework helper

print('*PyCharm*. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным')
print('*PyCharm*. и минимальным значением дробной части элементов. Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19')
print('*' * 16, 'Решение', '*' * 16)

initial_list = [1.1, 1.2, 3.1, 5, 10.01]
max_value = 0
min_value = max(initial_list)
for item in initial_list:
    if type(hh.get_fractional_part(item)) is float: # проверка на то является ли возвращаемое число дробным?
        cur_fractional_part = hh.get_fractional_part(item) # записываем в переменую, ддля того чтобы ниже не вызывать функции
        if cur_fractional_part > max_value:
            max_value = cur_fractional_part
        if cur_fractional_part < min_value:
            min_value = cur_fractional_part

print(f'максимальная дробная часть = {max_value}')
print(f'минимальная дробная часть = {min_value}')
print(f'разница между максимальным и минимальным числом = {max_value - min_value}')