# Напишите программу, удаляющую из текста все слова, содержащие "абв".

print('*PyCharm*. Напишите программу, удаляющую из текста все слова, содержащие "абв".')
print('*' * 16, 'Решение', '*' * 16)
task_string = 'asdfkksdgj;askdjg;hasdsdfghlsasdfhlakasdhaasdsdhgljka'
print(f'строка условия задачи = {task_string}')
print('Задайте строку поиска')
# string = str(input())
string = 'asd'

answer = "ввввввввв".join(task_string.split(string))

print(f'ответ = {task_string.split(string)}')
print(f'ответ = {answer}')

