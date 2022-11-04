import numpy as np
import matplotlib.pyplot as plt
import re

from sympy import Symbol
from sympy.calculus.util import minimum, maximum

# задача по семинару f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

x_list = [i for i in range(-60,60)]
print(x_list)

input_string = '-12x^4*sin(cos(x))-18x^3+5x^2+10x-30'
pattern = r'([-+]?\d*)(x\^*\d*)*'

res = re.findall(pattern, input_string)
print(res)
compl_pattern = re.compile(pattern)
result = compl_pattern.findall(input_string)
print(result)

x  = Symbol('x')
f = 2*x**2 + 3*x + 5

print(minimum(f, x))
print(maximum(f, x))


res_list = []
key_list = []
max_x = 0
for i in result:
    try:
        koef = float(i[0])
    except ValueError:
        continue
    if i[1]:
        # x1 = re.findall('[\d*]', i[1])
        x1 = i[1]
        x1 = x1.replace('x', '')
        x1 = x1.replace('^', '')
    res_list.append(koef)
    key_list.append(x1)
    print(type(x1))

float_list =[]
# float_list = [list(map(int, key_list)) for ]
for x in key_list:
    if x:
        float_list.append(int(x))
# float_list = int(map(int, key_list))
# float_list = [list(map(int, x)) for x in key_list if x]
max_x = max(key_list)
print(max_x)
print(key_list)
print(float_list)
print(res_list)
print(np.roots(res_list))

x = 54
print(f'форматирование или что ? {x:+f}')

#
# def my_func(x):
#     return 5 * x ** 2 + 10 * x - 30
#
#
# def my_homework_func(x):
#     return -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
#
#
# y_list = list(map(my_homework_func, x_list))
# print(y_list)
#
# my_diff = np.diff(y_list)
# print(my_diff)
# print(len(my_diff))
#
#
# # корни взяты с формулы 5 * x ** 2 + 10 * x - 30
# coeff = [-12, 18, 5, 10]
# print(np.roots(coeff))
#
# plt.plot(x_list, y_list)
#
# plt.xlabel(x_list)
# plt.ylabel(y_list)
# plt.text(4, 4e7, r'$\mu=100,\ \delta=15$')
# plt.axis([min(x_list), max(x_list), min(y_list), max(y_list)])
# plt.grid(True)
#
# # xy = max(x_list, y_list)
#
# plt.annotate('local max', xy = (1, 2), xytext=(3, 1.5),
#                 arrowprops= dict(facecolor='black', shrink= 0.05),
#              )
#
# plt.show()
#
#
# x = np.linspace(0, 10, 100)
# y = -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
#
# np_diff = list(np.diff(y))
# np_diff.append(11)
#
#
# fig, ax = plt.subplots()
#
# ax.plot(x, y, linewidth=2.0)
# ax.plot(x, np_diff, linewidth=2.0)
# plt.grid(True)
# plt.show()
#
# if __name__ == '__main__':
#     print(__name__)

