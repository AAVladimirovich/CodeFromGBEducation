
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