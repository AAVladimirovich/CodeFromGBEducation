# Создайте программу для игры в "Крестики-нолики".


#функция вызова меню ходов
def menu_turn(arg_lines):
    count = 1
    count_list = []
    for i in range(len(arg_lines[0])):
        if arg_lines[i][0] == '   ':
            count_list.append(f'a{i + 1}')
            print(f'{count}) свободные клетки поля a{i + 1}')
            count += 1
    for i in range(len(arg_lines[1])):
        if arg_lines[i][1] == '   ':
            count_list.append(f'b{i + 1}')
            print(f'{count}) свободные клетки поля b{i + 1}')
            count += 1
    for i in range(len(arg_lines[2])):
        if arg_lines[i][2] == '   ':
            count_list.append(f'c{i + 1}')
            print(f'{count}) свободные клетки поля c{i + 1}')
            count += 1
    return count_list


# делаем ход
def make_turn(arg_turn, arg_choice, arg_field_list):
    print(arg_choice)
    if arg_choice == 'a1':
        arg_field_list[0][0] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'b1':
        arg_field_list[0][1] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'c1':
        arg_field_list[0][2] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'a2':
        arg_field_list[1][0] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'b2':
        arg_field_list[1][1] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'c2':
        arg_field_list[1][2] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'a3':
        arg_field_list[2][0] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'b3':
        arg_field_list[2][1] = ' X ' if arg_turn % 2 == 0 else ' O '
    elif arg_choice == 'c3':
        arg_field_list[2][2] = ' X ' if arg_turn % 2 == 0 else ' O '
    return arg_field_list


# функция отрисовки поля
def prepare_field(arg_lines_h, arg_lines_v, arg_field_list):
    cls = lambda: print('\n' * 100)
    cls()
    print(arg_lines_h)
    for index, element in enumerate(arg_field_list):
        print(arg_lines_v[index], '|'.join(element), end='\n ==== === ====\n')


# определение победителя
def check_victory(arg_turn, arg_field_list):
    marker = ' X ' if arg_turn % 2 == 0 else ' O '
    if arg_field_list[0][0] == marker and arg_field_list[1][0] == marker and arg_field_list[2][0] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[0][1] == marker and arg_field_list[1][1] == marker and arg_field_list[2][1] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[0][2] == marker and arg_field_list[1][2] == marker and arg_field_list[2][2] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[0][0] == marker and arg_field_list[0][1] == marker and arg_field_list[0][2] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[1][0] == marker and arg_field_list[1][1] == marker and arg_field_list[1][2] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[2][0] == marker and arg_field_list[2][1] == marker and arg_field_list[2][2] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[0][0] == marker and arg_field_list[1][1] == marker and arg_field_list[2][2] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True
    elif arg_field_list[0][2] == marker and arg_field_list[1][1] == marker and arg_field_list[2][0] == marker:
        print(f'Игрок {n % 2 + 1} победил. Победила команда {marker} ')
        return True


print(
    'PyCharm\n'
    'Создайте программу для игры в "Крестики-нолики".\n'
    )

lines_v = ['1', '2', '3']
lines_h = ['a', 'b', 'c']
field_list = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]
n = 1
victory = False
prepare_field(lines_h, lines_v, field_list)
while not victory:
    player_num = n % 2 + 1
    choice_menu_list = menu_turn(field_list)
    x = input(f'Ход {player_num} игрока. Сделайте выбор от 1 до {len(choice_menu_list)} ')
    while int(x) > len(choice_menu_list) or int(x) < 1:  # ограничение выбора для меню
        x = input(f'Ход {player_num} игрока. Сделайте выбор от 1 до {len(choice_menu_list)} ')
    field_list = make_turn(n, choice_menu_list[int(x)-1], field_list)
    prepare_field(lines_h, lines_v, field_list)
    victory = check_victory(n, field_list)
    n = n + 1

