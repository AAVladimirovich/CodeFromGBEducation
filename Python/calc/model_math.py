x = 0
y = 0
x_complex = 0
y_complex = 0
# val_memory =[]
# x_complex = []
# y_complex = []


def init(a, b):
    global x
    global y
    x = a
    y = b


# функция умножение
def mult():
    # val_memory = list(map(int, val_memory))
    string = 'умножение'
    return x * y, string


# функция вычитание
def sub():
    string = 'вычитание'
    return x - y, string


# функция сумма
def summ():
    string = 'сумма'
    return x + y, string


# функция деления
def division():
    string = 'деление'
    return x / y, string


# ************* КОМПЛЕКСНЫЕ ЧИСЛА ************************
def get_complex():
    return x_complex, y_complex


# инициализация
def init_complex(a, b):
    global x_complex
    global y_complex
    x_complex = list(map(float,a))
    y_complex = list(map(float,b))


def summ_complex_lambda(a, b):
    return a + b


def division_complex_lambda(a, b):
    return a - b


# функция умножение
def mult_complex():
    # answer_list = list(map(,x_complex,y_complex))
    string = 'умножение complex'
    # print(val_memory)
    return x_complex * y_complex, string
    # return 'mult', 'mult complex'


# функция вычитание
def division_complex():
    string = 'вычитание complex'
    return x_complex - y_complex, string


# функция деления
def sub_complex():
    # answer_list = list(map(division_complex_lambda, x_complex, y_complex))
    string = 'вычитание complex'
    # return str(answer_list[0]) + '+' + str(answer_list[1]) + 'i', string
    return x_complex - y_complex, string


# функция сумма
def summ_complex():
    # answer_list = list(map(summ_complex_lambda, x_complex, y_complex))
    string = 'сумма complex'
    return x_complex + y_complex, string
    # return str(answer_list[0]) + '+' + str(answer_list[1]) + 'i', string