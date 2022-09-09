# 5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print ('Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
coordPointOne = []
coordPointTwo = []
for i in range(2):
    print('введите ', i+1, " значение первой координаты")
    a = int(input())
    coordPointOne.append(a)
for i in range(2):
    print('введите ', i+1, " значение второй координаты")
    b = int(input())
    coordPointTwo.append(b)

LengthBetweenPoint = round((((coordPointTwo[0] - coordPointOne[0]) ** 2) + ((coordPointTwo[1] - coordPointOne[1]) ** 2)) ** (0.5),2) # ** (0.5) - квадратный корень

print ('расстояние между точкой', coordPointOne, ' и точкой ' , coordPointTwo, ' = ', LengthBetweenPoint)
