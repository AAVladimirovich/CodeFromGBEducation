# 2 Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import utils_v3 as hh  # hh - homework helper

print(
    'PyCharm\n'
    'Дан список чисел. Создайте список, в который попадают числа, описываемые\n'
    'возрастающую последовательность. Порядок элементов менять нельзя.\n'
    'Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.\n'
    )

task_list = [1, 5, 2, 3, 4, 6, 1, 7]
print(f'Лист для задания {task_list}')

answer_list = [hh.is_exist(task_list, 0)]
for i in range(len(task_list)):
    # if type(hh.is_exist(task_list, i + 1)) != type(None):  # сохранил код по мне так лучше читаемость чем ниже
    if not isinstance(hh.is_exist(task_list, i + 1), type(None)):  # isinstance - сравнивает значение с типом если не Ноне то делаем
        next_value = hh.is_exist(task_list, i + 1)
    if answer_list[-1] < next_value:
        answer_list.append(next_value)
print(answer_list)

