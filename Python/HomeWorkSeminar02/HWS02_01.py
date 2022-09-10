# 1 Подсчитать сумму цифр в вещественном числе.
import numbers

print('*PyCharm*. Подсчитать сумму цифр в вещественном числе.')
print('введите вещественное число')
strValue = input()
sumNumber = 0
for i in range(len(strValue)):
    if strValue[i].isdigit():
        sumNumber += int(strValue[i])

print(sumNumber)
