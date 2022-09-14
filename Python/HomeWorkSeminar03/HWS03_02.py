# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д. Пример:  - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

print('*PyCharm*. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний')
print('*PyCharm*. элемент, второй и предпоследний и т.д. Пример:  - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]')
print('*' * 16, 'Решение', '*' * 16)
homework_list = [2, 3, 5, 6]
print(f'список условия задачи = {homework_list}')
answer_list = []
sum_of_elements = 0
half_of_array_index = int(len(homework_list)//2) + int(len(homework_list)%2)
for index in range(half_of_array_index):
    sum_of_elements = homework_list[index] * homework_list[-1-index]
    answer_list.append(sum_of_elements)
print(f'список решения задачи = {answer_list}')