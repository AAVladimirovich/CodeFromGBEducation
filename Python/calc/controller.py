from statistics import mode
import model_math as model
import view


def button_click():
    menu()


def menu():
    while True:
        print('1) простые числа int\n'
              '2) комплексные числа complex\n'
              'для выхода введите "x"\n'
              )
        user_choice = input('выберите операцию = ')
        if user_choice == '1':
            menu_int()
        elif user_choice == '2':
            menu_complex()
        elif user_choice == 'x':
            break
        else:
            print('введите корректное значение меню')

def menu_complex():
    value_a = view.get_value_complex()
    value_b = view.get_value_complex()
    model.init_complex(value_a, value_b)
    while True:
        print('КОМЛЕКСНЫЕ ЧИСЛА\n'
              '1) умножение complex\n'
              '2) деление complex\n'
              '3) сложение complex\n'
              '4) вычитание complex\n'
              '5) вывести комплексные числа\n'
              'для выхода введите "x"\n'
              )
        user_choice = input('выберите операцию = ')
        if user_choice == '1':
            result, string = model.mult_complex()
            view.view_data(result, string)
        elif user_choice == '2':
            result, string = model.division_complex()
            view.view_data(result, string)
        elif user_choice == '3':
            result, string = model.summ_complex()
            view.view_data(result, string)
        elif user_choice == '4':
            result, string = model.sub_complex()
            view.view_data(result, string)
        elif user_choice == '5':
            a, b = model.get_complex()
            view.view_data(a, b)
        elif user_choice == 'x':
            break
        else:
            print('введите корректное значение меню')



def menu_int():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    while True:
        print('INT ЧИСЛА\n'
              '1) умножение\n'
              '2) деление\n'
              '3) сложение\n'
              '4) вычитание\n'
              'для выхода введите "x"\n'
              )
        user_choice = input('выберите операцию = ')
        if user_choice == '1':
            result, string = model.mult()
            view.view_data(result, string)
        elif user_choice == '2':
            result, string = model.division()
            view.view_data(result, string)
        elif user_choice == '3':
            result, string = model.summ()
            view.view_data(result, string)
        elif user_choice == '4':
            result, string = model.sub()
            view.view_data(result, string)
        elif user_choice == 'x':
            break
        else:
            print('введите корректное значение меню')


