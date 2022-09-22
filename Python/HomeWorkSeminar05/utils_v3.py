import random
import re


# функция определения числа, чётного или нет
def is_it_odd(arg_number):
    if arg_number % 2 == 1:
        return True
    else:
        return False


# функция возврата дробной части
def get_fractional_part(arg_number):
    whole_part = arg_number // 1
    fractional_part = round(arg_number - whole_part, 5)
    if fractional_part == 0:
        return
    else:
        return fractional_part

# функция преобразования в двоичный код
def to_decimal(arg_number):
    if arg_number == 1:
        return 1
    elif arg_number == 0:
        return 0
    return arg_number % 2 + 10 * to_decimal(arg_number // 2)

# функция преобразования в код заданный basenum - ограничение 2 до 9 наверное.
def to_basenum_system_conversion(arg_number, basenum):
    if arg_number == 1:
        return 1
    elif arg_number == 0:
        return 0
    return arg_number % basenum + 10 * to_basenum_system_conversion(arg_number // basenum, basenum)

# фибоначчи ряд, возвращающий от негативного числа
def negafibonacci(arg_number):
    if arg_number >= 0:
        if arg_number == 1 or arg_number == 2:
            return 1
        elif arg_number == 0:
            return 0
        else:
            return negafibonacci(arg_number - 1) + negafibonacci(arg_number - 2)
    elif arg_number < 0:
        if arg_number == -1 or arg_number == -2:
            return -1
        else:
            return negafibonacci(arg_number + 1) + negafibonacci(arg_number + 2)


# определение наименьшего общего делителя???
def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


# функция определения наименьшего общего кратного
def nok(a, b):
    return int(a * b) / nod(a, b)


# функция решета Эратосфена
def sieve_list(arg_int):
    sieve = set(range(2, arg_int+1))
    prime_list = []
    while sieve:
        prime = min(sieve)
        prime_list.append(prime)
        #print(sieve)
        #print(prime)
        sieve -= set(range(prime, arg_int + 1, prime))
        #print(sieve)
    #print(prime_list)
    return prime_list


# функция возвращения уникальных значений из списка
def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


# проверка ввода
def key_check(arg_string, arg_wich_check='int', arg_len=15):
    if any([i > 'z' or i < 'a' for i in arg_string]) and arg_wich_check == 'string':
        print(f'Error: Contains illegal characters, not {arg_wich_check}')
        return False
    if any([i > '9' or i < '0' for i in arg_string]) and arg_wich_check == 'int':
        print(f'Error: Contains illegal characters, not {arg_wich_check}')
        return False
    elif len(arg_string) > arg_len:
        print("Very long string")
    return True


# функция работы с файлом, когда-нибудь переделать правильнее, может распределить отдельно на запись и на чтение
def write_to_file(arg_filename, arg_data, arg_write_func: str = 'a'):
    # открываем файл для изменения 'w' - значит перезапись - изменяем содержимое с чистого листа
    # открываем файл для изменения 'a' - значит добавление - добовляем содержимое в файл
    # открываем файл для изменения 'r' - значит чтение содержимого файла
    if arg_write_func == 'w' or arg_write_func == 'a':
        with open(arg_filename, arg_write_func) as data:
            data.write(arg_data)
            data.write('\n')
        data.close()


# функция чтения из файла
def read_from_file(arg_filename, return_required: bool = False):
    string_to_return = ''
    data = open(arg_filename)  # открываем файл для чтения
    for line in data:  # перебираем файл по строкам и печатаем
        if line != '\n':
            print(f'значение строки внутри файла {arg_filename} : {line}')
            string_to_return += line
    data.close()
    if return_required:
        return string_to_return


# функция задачи рандомного многочлена, дичь лютая конечно
def polynomial(arg_koef, arg_max_rnd: int = 100):
    a = int(random.randint(1, arg_max_rnd))
    b = int(random.randint(1, arg_max_rnd))
    c = int(random.randint(1, arg_max_rnd))

    if a != 0:
        first = (str(a) + "x^" + str(arg_koef) + " + ")
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

    return first + second + third


# посмотрел в интернете позволяет очистить строку от разных символов, заменить на " " указано до определения Word.strip()
def clean(word):
    return re.sub(r"[`x^+=!?.:;,'\"()-]", " ", word.strip())


# функция инверсии бита
def inverse_bit(arg_bit):
    return arg_bit ^ True


# проверка на наличие индекса в листе
def is_exist(arg_list, arg_index):
    try:
        return int(arg_list[arg_index])
    except IndexError:
        print(f'Index {arg_index} отсутствует в листе {arg_list}') # при ошибке возвращает NoneType - можно отлавливать
        #  return 0


# функция кодирования в RLE
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 0

    if not data:
        return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


# функция декодирования с RLE
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    return decode

# list comprehansion
# [print(f' множитель числа {n} = {item} *') for item in answer_list if item > 5]
# [answer_list.append(task_list[i]) for i in range(len(task_list)) if task_list[i] < hh.is_exist(task_list, i + 1)]
# [print(f'{count + i}) свободные клетки поля a{i+1} ') for i in range(len(arg_lines[0])) if arg_lines[0][i] == '   ']
# [count_list.append(f'a{i + 1}') for i, val in enumerate(arg_lines[0], start=0) if val == '   ']
# [print(f'{len(count_list) - len(count_list) + i + 1}) свободные клетки поля a{i + 1} ') for i, val in enumerate(arg_lines[0], start=0) if val

# использование map, lambda, filter
# def lambda_la(x):
#     if 'абв' not in x:
#         return x
#
# answer_list3 = list(map(lambda_la, task_string2.split(' ')))
# answer_list2 = ' '.join(list(filter(lambda_la, task_string2.split(' '))))
# answer_list = ' '.join(list(filter(lambda x: 'абв' not in x, task_string2.split(' '))))

# проверка на тип переменной
# if type(hh.is_exist(task_list, i + 1)) != type(None):
# if not isinstance(hh.is_exist(task_list, i + 1), type(None)):
# if type(hh.get_fractional_part(item)) is float:

# мусорка. когда-нибудь разобрать
# void Fibonacci(int in_num)
# {
#     int f1 = 0;
#     int f2 = 1;
#     int sum = 0;
#     Console.Write($"{f1} {f2}");
#
#     for (int i = 1; i <= in_num; i++)
#     {
#         sum = f1 + f2;
#         f1 = f2;
#         f2 = sum;
#         Console.WriteLine($"F({i}) = {sum}");
#     }
# }

# #функция определения простых множителей числа
# def pmc(arg_number):
#     pmc_list = []
#     while arg_number != 1:
#         prime_list = sieve_list(arg_number)
#         first_min_prime = False
#         for current_prime in prime_list:
#             if arg_number % current_prime == 0 and first_min_prime == False:
#                 first_min_prime = True
#                 pmc_list.append(current_prime)
#                 pmc(arg_number / current_prime)
#                 return pmc_list.append(current_prime)
