# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random


# логика бота
def bot_logic(arg_total_sweets):
    target = 29
    if arg_total_sweets <= 56:
        if arg_total_sweets == target:
            return random.randrange(1, arg_total_sweets-1)
        elif arg_total_sweets < target:
            return arg_total_sweets
        else:
            return arg_total_sweets - target
    else:
        return random.randrange(1, 28)


# шестое чувство
def sixth_sense(arg_total_sweets):
    if arg_total_sweets > 56:
        sense_choice = arg_total_sweets - ((arg_total_sweets // 28) * 28)-1
        if sense_choice < 0:
            sense_choice = 1
        print(f"****** Что-то подсказывает тебе взять {sense_choice} конфет ******")
    if 28 < arg_total_sweets <= 56:
        print(f"****** Что-то подсказывает тебе взять {arg_total_sweets - 29} конфет ******")
    elif arg_total_sweets <= 28:
        print(f"****** Что-то подсказывает тебе взять {arg_total_sweets} конфет ******")


# инверсируем ход для передачи
def change_turn(arg_turn):
    return arg_turn ^ True


# проверка победителя
def check_win(total_sweets, player_turn):
    if player_turn == True and total_sweets <= 0:
        print(f'Победил игрок !!!!!!')
    elif player_turn == False and total_sweets <= 0:
        print(f'Победил AI !!!!!')


# логика игры
def game(arg_ttls_sweets, arg_pl_turn):
    while arg_ttls_sweets > 0:
        if arg_pl_turn:
            sixth_sense(arg_ttls_sweets)
            player_choice = int(input('Сколько конфет возьмёт игрок? '))
            while not 0 < player_choice < 29:
                player_choice = int(input('конфет можно взять от 1 до 28, введите повторно '))
            print(f'игрок взял = {player_choice} конфет')
            arg_ttls_sweets -= player_choice
        else:
            bot_choice = bot_logic(arg_ttls_sweets)
            print(f'бот взял = {bot_choice} конфет')
            arg_ttls_sweets -= bot_choice
        print(f'конфет осталось = {arg_ttls_sweets}')
        check_win(arg_ttls_sweets, arg_pl_turn)   # проверка на выигрышь
        arg_pl_turn = change_turn(arg_pl_turn)   # смена хода


# ниже приведены инициализирующие параметры, определения конфет, определения хода
total_sweets = 2021
print(
    '"Игра с конфетами"\n'
    'В игре участвуют игрок и бот\n'
    'Первый ход определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры\n'
    f'У нас есть некоторое количество конфет {total_sweets}\n'
    'За один ход можно забрать не более 28 конфет\n'
    'Тот, кому достанется последняя конфета - выиграл\n'
    )

player_turn = random.randrange(2)
if player_turn:
    print('Первым ход делает игрок')
else:
    print('Первым ход делает бот')

game(total_sweets, player_turn) # запуск игры
