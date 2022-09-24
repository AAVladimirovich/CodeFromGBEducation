# функция отображения результата
def view_data(data, title):
    print(f'{title} = {data}')


# функция получения значений
def get_value():
    return int(input('value = '))


def get_value_complex():
    real_part = float(input('введите значение действительной части'))
    imag_part = float(input('введите значение мнимой части'))
    return complex(real_part, imag_part)
    # real_part = input('введите значение действительной части')
    # imag_part = input('введите значение мнимой части')
    # complex_list = [real_part, imag_part]
    # return complex_list
