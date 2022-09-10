import ClassHolder #импортируем файл ClassHolder.py

with open('Lection02Python.txt', 'w') as data: # открываем файл для изменения 'w' - значит перезапись - изменяем содержимое с чистого листа
    data.write('line 1\n') 
    data.write('line 2\n')

colors = ['red', 'green', 'blue'] 
data = open('Lection02Python.txt', 'a') # открываем файл для изменения 'a' - значит добавление - не меняя содержимого
data.writelines(colors) # разделителей не будет 
data.write('\n')
data.write(data.name)
data.write('\n')
data.write('Скрипт создания и заполнения файла находится в Lect02/Lection02.py')
# data.write(str(help(data)))
data.close() 

path = 'Lection02Python.txt' 
data = open(path, 'r') # открываем файл для чтения
for line in data: # перебираем файл по строкам и печатаем
    print(line) 
data.close()

print(ClassHolder.f(1)) #используем функцию из ClassHolder

# with open(path, 'w') as data: #открываем файл для изменения 'w' - значит перезапись - изменяем содержимое с чистого листа
#     for i in range(len(listForAction)):
#         if listForAction[i] == 0:
#             data.write(f'{listForAction[i+1]}\n')
#         else:
#             data.write(f'{listForAction[i]}\n')
# data.close()