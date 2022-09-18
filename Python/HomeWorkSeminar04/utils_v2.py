
# функция определения числа, чётного или нет
def is_it_odd(arg_number):
    if arg_number % 2 == 1:
        return True
    else:
        return False


#функция возврата дробной части
def get_fractional_part(arg_number):
    whole_part = arg_number // 1
    fractional_part = round(arg_number - whole_part, 5)
    if fractional_part == 0:
        return
    else:
        return fractional_part

#функция преобразования в двоичный код
def to_decimal(arg_number):
    if arg_number == 1:
        return 1
    elif arg_number == 0:
        return 0
    return arg_number % 2 + 10 * to_decimal(arg_number // 2)

#функция преобразования в код заданный basenum - ограничение 2 до 9 наверное.
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


#определение наименьшего общего делителя???
def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


#функция определения наименьшего общего кратного
def nok(a, b):
    return int(a * b) / nod(a, b)


#функция решета Эратосфена
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


# list comprehansion
# [print(f' множитель числа {n} = {item} *') for item in answer_list if item > 5]

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
