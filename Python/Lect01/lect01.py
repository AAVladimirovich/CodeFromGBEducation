print ('Hello World')

# print('Введите а')
# a = int(input()) 
# print('Введите b')
# b = int(input())
# print('Введите c')
# c = int(input())
a = 12
b = 8
c = a-b
print(a, ' + ', b, ' + ',c, ' = ', a+b+c) 
print('{2} + {1} = {0}'.format(a, b, c))


list  = [a,b,c,'Hello',a+b+c, 'vsyakie stroki']
print (list)

# проверка операторов
# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной программы
# Если помните математику – проблем не будет
# +, -,*, /, %, //,**
# Приоритет операций **, ⊕, ⊖, * , /, //, %, +, -
# ( ) Скобки меняют приоритет


print ('a = 12, b = 8')
a = 12
b = 8
c = a-b
print ('вычитание "-" = ',c)

a = 12
b = 8
c = a*b
print ('умножение "*" = ',c)

a = 12
b = 8
c = a/b
print ('деление "/" = ',c)

a = 12
b = 8
c = a//b
print ('деление до целых "//" = ',c)

a = 12
b = 8
c = a%b
print ('остаток от деления  "%" = ',c)

a = 12
b = 8
c = a**b
print ('возведение в степень  "**" = ',c)

print ('округление a = 1.3, b = 3')
a = 1.3
b = 3
c = round(a * b,5)
print ('округление "*round(a * b,5)" = ',c)

print ('простые приращивания a = 4, приращиваем на 3')
a = 4
a += 3
print('приращивание пишется a "+,/,*" и потом добавляется "=" и того чтобы прирастить на три a += 3', a)

a = int (input('a = '))
b = int (input('b = '))
if a > b:
    print(a)
else:
    print(b)

for i in 1,2,3,4,5:
    print(i**2)

for i in range(1,10,2):
    print(i)

for i in 'Hello World!':
    print(i)

x = 11
if 5 < x < 9:
    print(x)