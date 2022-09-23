# Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.
import re
import utils_v2 as hh  # hh - homework helper


#посмотрел в интернете позволяет очистить строку от разных символов, заменить на " " указано до определения Word.strip()
def clean(word):
    return re.sub(r"[`x^+=!?.:;,'\"()-]", " ", word.strip())


print('*PyCharm*. Даны два файла, в каждом из которых находится запись многочлена. Задача -')
print('*PyCharm*. сформировать файл, содержащий сумму многочленов.')
print('*' * 16, 'Решение', '*' * 16)
k = int(input('Введите коэффициент K: '))
hh.write_to_file('HWS04_05_01.txt', hh.polynomial(k, 100), 'w')
hh.write_to_file('HWS04_05_02.txt', hh.polynomial(k, 50), 'w')
print('Первый файл:')
string_polynomial_one = hh.read_from_file('HWS04_05_01.txt', True)
print('Второй файл:')
string_polynomial_two = hh.read_from_file('HWS04_05_02.txt', True)

string_polynomial_one = string_polynomial_one.split()
print(f'Лист из первого файла до map и функции clean:{string_polynomial_one}')
string_polynomial_one = map(clean, string_polynomial_one)   # Map - применение функции clean - к каждому итерируемому объёкту в данном случае string_polynomial_one
string_polynomial_one = ' '.join(string_polynomial_one)
string_polynomial_one = string_polynomial_one.split()

string_polynomial_two = string_polynomial_two.split()
print(f'Лист из второго файла до map и функции clean:{string_polynomial_two}')
string_polynomial_two = map(clean, string_polynomial_two)
string_polynomial_two = ' '.join(string_polynomial_two)
string_polynomial_two = string_polynomial_two.split()

print(f'Лист из первого файла после map и функции clean:{string_polynomial_one}')
print(f'Лист из второго файла после map и функции clean:{string_polynomial_two}')

complex_string = ''

for item in zip(string_polynomial_one, string_polynomial_two):
    item2 = map(int, item)
    if item2 != k or item2 != 0:
        item2 = sum(item2)
        complex_string += str(item2) + '+'

complex_list = complex_string[0:-1].split('+')
print(f' Сумма многочленов равна = {complex_list[0]}x^{k} + {complex_list[1]}x + {complex_list[2]} = 0')

answer_string = f'{complex_list[0]}x^{k} + {complex_list[1]}x + {complex_list[2]} = 0'
hh.write_to_file('HWS04_05_03.txt', answer_string, 'w')