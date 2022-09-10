# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import *

print('*PyCharm*. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на')
print('*PyCharm*. указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')
print('введите число N = ')
n = int(input())

if n < 4:
    print ('n меньше 4тырех, устанавлю по умолчанию 4')
    n = 4

listForAction = []
for i in range(-n, n+1):
    listForAction.append(i)
print(f'Перечень чисел = {listForAction}')

path = 'HWS02_04.txt'

with open(path, 'w') as data: #открываем файл для изменения 'w' - значит перезапись - изменяем содержимое с чистого листа
    data.write('1\n')
    data.write('2\n')
    data.write('3\n')
    data.write('5\n')
data.close()

multOfArray = 1
data = open(path, 'r')   # открываем файл для чтения
for line in data:        # перебираем файл по строкам и печатаем
    multOfArray *= listForAction[int(line)]
data.close()

print(multOfArray)