
# функция определения числа, чётного или нет
def is_it_odd(arg_number):
    if arg_number % 2 == 1:
        return True
    else:
        return False


def get_fractional_part(arg_number):
    whole_part = arg_number // 1
    fractional_part = round(arg_number - whole_part, 5)
    if fractional_part == 0:
        return
    else:
        return fractional_part


def to_decimal(arg_number):
    if arg_number == 1:
        return 1
    elif arg_number == 0:
        return 0
    return arg_number % 2 + 10 * to_decimal(arg_number // 2)


def to_basenum_system_conversion(arg_number, basenum):
    if arg_number == 1:
        return 1
    elif arg_number == 0:
        return 0
    return arg_number % basenum + 10 * to_basenum_system_conversion(arg_number // basenum, basenum)


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
