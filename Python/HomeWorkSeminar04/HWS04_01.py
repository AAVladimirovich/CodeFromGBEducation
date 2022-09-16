# Вычислить число c заданной точностью d
# Пример:при d = 0.001, π = 3.141 диапазон 10-1 <= d <= 10-10

import utils_v2 as hh  # hh - homework helper
import math

print('*PyCharm*. Вычислить число c заданной точностью d')
print('*PyCharm*. Пример:при d = 0.001, π = 3.141 диапазон 10-1 <= d <= 10-10')
print('*' * 16, 'Решение', '*' * 16)
print('задайте d от 1 до 10 знаков после запятой = ')
d = int(input())   # стоило бы запилить проверку на число
if 10 >= d >= 1:
    # pi = float('{:.4f}'.format(math.pi))
    # print(pi)
    # print('%.4f' % math.pi)
    print(round(math.pi, d))
else:
    print('d установлен 3')
    d = 3
    print(round(math.pi, d))
