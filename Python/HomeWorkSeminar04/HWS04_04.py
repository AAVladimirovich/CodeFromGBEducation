# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import utils_v2 as hh  # hh - homework helper

print('*PyCharm*. Задана натуральная степень k. Сформировать случайным образом список')
print('*PyCharm*. коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен')
print('*PyCharm*. степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0')
print('*' * 16, 'Решение', '*' * 16)
k = int(input('Введите коэффициент K: '))
a = int(random.randint(0, 100))
b = int(random.randint(0, 100))
c = int(random.randint(0, 100))

if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())

if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())

if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())

answer_string = first + second + third

hh.write_to_file('HWS04_04.txt', answer_string, 'w')
hh.read_from_file('HWS04_04.txt')
