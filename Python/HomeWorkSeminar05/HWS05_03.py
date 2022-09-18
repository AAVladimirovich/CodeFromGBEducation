# Напишите программу, удаляющую из текста все слова, содержащие "абв".

print('*PyCharm*. Напишите программу, удаляющую из текста все слова, содержащие "абв".')
print('*' * 16, 'Решение', '*' * 16)
task_string = 'абввафожвылоабвлдмоджлвоаабвжлофжывлпофабв'
print(f'строка условия задачи = {task_string}')
find_string = 'абв'
answer = "".join(task_string.split(find_string))
# answer = "*".join(task_string.split(string))
# print(f'ответ = {task_string.split(find_string)}')
print(f'ответ = {answer}')
