# Напишите программу, удаляющую из текста все слова, содержащие "абв".

print('*PyCharm*. Напишите программу, удаляющую из текста все слова, содержащие "абв".')
print('*' * 16, 'Решение', '*' * 16)
task_string2 = 'абвваф ожвылоаб влдмоджлвоа абвжлофжы влп офабв'
print(f'строка условия задачи = {task_string2}')
find_string = 'абв'
answer_list = ' '.join(list(filter(lambda x: 'абв' not in x, task_string2.split(' '))))
print(f'ответ 1= {answer_list}')


