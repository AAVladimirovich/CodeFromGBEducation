# 5 Реализовать алгоритм перемешивания списка.
import random
from random import * # пробуем импортировать рандом

print('*PyCharm*. Реализовать алгоритм перемешивания списка.')
print('введите число элементов списка  N = ')
listLen = int(input())

mainList = [] # Задаём переменную списка
for i in range(listLen): # заполняем рандомными числами от 0 до 100
    mainList.append(randrange(start=0, stop= 100))

print(f'основной список из {listLen} чисел = {mainList}')

mainList.reverse()

print(f'основной список из {listLen} чисел после метода реверс = {mainList}')

memoryVariable = 0 # переменная для хранения истинного значения списка
memoryIndex = 0 # переменная для рандома индекса
for i in range(listLen):
    memoryIndex = randrange(start=0, stop= listLen)
    while memoryIndex == i:
        memoryIndex = randrange(start=0, stop=listLen)
    memoryVariable = mainList[i]
    mainList[i] = mainList[memoryIndex]
    mainList[memoryIndex] = memoryVariable

print(f'основной список из {listLen} чисел после перемещивания = {mainList}')