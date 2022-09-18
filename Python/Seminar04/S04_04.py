# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random

# print('Сколько конфет возьмёт первый игрок?')
# int_first = int(input())
total_sweets = 57
player_turn = True
int_bot = 0

def correct_logic(arg_int):
    target = 29
    if arg_int == target:
        return 28
    elif arg_int < target:
        return arg_int
    else:
        return arg_int - target


while total_sweets > 0:
    if player_turn == True:
        print('Сколько конфет возьмёт первый игрок?')
        int_player = int(input())
        if 28 >= int_player <= 0:
            int_player = 13
        print(f'игрок взял = {int_player}')
        total_sweets -= int_player
        player_turn = False
        print(f'конфет осталось = {total_sweets}')
    else:
        if total_sweets <= 56:
            print(f'correct_logic')
            int_bot = correct_logic(total_sweets)
            print(f'бот взял = {int_bot}')
            total_sweets -= int_bot
            print(f'конфет осталось = {total_sweets}')
        else:
            int_bot = random.randrange(1, 28)
            print(f'бот взял = {int_bot}')
            total_sweets -= int_bot
            player_turn = True
            print(f'конфет осталось = {total_sweets}')

if player_turn == True:
    print(f'победил игрок = конфет осталось {total_sweets}')
else:
    print(f'победил AI = конфет осталось {total_sweets}')
