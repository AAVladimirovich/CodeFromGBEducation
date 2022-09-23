# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

import utils_v3 as hh  # hh - homework helper
import random

print(
    'PyCharm\n'
    'В файле находится N натуральных чисел, записанных через пробел. Среди чисел не\n'
    'хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число\n'
    )
len_of_list = int(input('введите длину списка '))
task_string = ''
missed_number = random.randrange(len_of_list)

for i in range(len_of_list):
    if i is not missed_number:
        task_string += str(i) + ' '

hh.write_to_file("HWS05_01.txt", task_string, 'w')
work_list = hh.read_from_file("HWS05_01.txt", True)   # получаем строку с файла и присваиваем стринговой переменной
work_list = work_list.split()   # разбиваем полученую строку по пробелам и переводим её в лист
print(f'Лист полученный с файла {work_list}')

enum_list = []
[enum_list.append(val) for val in enumerate(work_list, start=0)]
print(f'enum_list = {enum_list}')
[print(f'найдено несоответствие в числе =  {i}') for i, val in enum_list if i != int(val)]

current_number = 0
next_number = 0
for i in range(len_of_list):
    if i == 0:  # так как лист начинается с 0 индекса и это значение может быть пропущено, то приравниваем в ручную на проверку
        current_number = 0
        if current_number != int(work_list[i]):
            print(f'Отсутствующая цифра = {current_number}')
            exit()
    current_number = int(work_list[i])
    try:
        next_number = int(work_list[i+1])  # так как лист может оканчиваться на последний элемент который отличный от общего списка, то проверяем на существование элемента
    except IndexError:
        print(f'Отсутствующая цифра = {current_number + 1}')
        exit()
    if next_number - 1 != current_number:
        print(f'Отсутствующая цифра = {next_number - 1}')
        exit()
