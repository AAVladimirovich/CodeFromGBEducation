# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('*PyCharm*. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.')
print('*PyCharm*. Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}.')
print('введите число N = ')
n = int(input())

def reshalo(argn):
    return round((1 + (1/argn)) ** argn,2)

list = []
summ = 0
for i in range(1, n+1):
    list.append(reshalo(i))
    summ += list[i-1]

print(list)
print(f'сумма последовательности = {summ}')