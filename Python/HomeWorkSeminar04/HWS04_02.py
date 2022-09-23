# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

import utils_v2 as hh  # hh - homework helper


print('*PyCharm*. Задайте натуральное число N. Напишите программу, которая составит список')
print('*PyCharm*. простых множителей числа N.')
print('*' * 16, 'Решение', '*' * 16)
print('Задайте натуральное число N = ')
n = int(input())  # стоило бы запилить проверку на число
memory_n = n
answer_list = []   # лист для ответа
while n != 1:
    prime_list = hh.sieve_list(n)
    first_min_prime = False
    for current_prime in prime_list:
        if n % current_prime == 0 and first_min_prime == False:
            first_min_prime = True
            answer_list.append(current_prime)
            n = int(n / current_prime)

print(f'Список простых множителeй числа {answer_list}')

answer_string = ''
while answer_list:
    answer_string = answer_string + str(answer_list.pop(0)) + '*'

print(f'Простые множители числа {memory_n} = {answer_string[0:-1]}')



