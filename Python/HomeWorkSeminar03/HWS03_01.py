# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('*PyCharm*. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,')
print('*PyCharm*. стоящих на нечётной позиции. Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12')


def is_odd(arg_number):
    if arg_number % 2 == 1:
        return True
    else:
        return False


homework_list = [2, 3, 5, 9, 3]
sum_of_odd_element = 0
for index in range(len(homework_list)):
    if is_odd(index):
        print(f'индекс {index} является нечётным, число в индексе = {homework_list[index]}')
        sum_of_odd_element += homework_list[index]
print(f'сумма чисел в нечётных индексах списка = {sum_of_odd_element}')

