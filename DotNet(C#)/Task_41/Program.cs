// Задача 41: Пользователь вводит с клавиатуры M чисел. 
// Посчитайте, сколько чисел больше 0 ввёл пользователь.
// 0, 7, 8, -2, -2 -> 2
// -1, -7, 567, 89, 223-> 3

void FindMinusValueInArray(int[] in_array)
{
    int minusCounter = 0;
    for (int i = 0; i < in_array.Length; i++)
    {
        if (in_array[i] < 0) minusCounter++;
    }

    Console.WriteLine($"Отрицательных чисел = {minusCounter}");
}

int[] UserInputValueInArray(int[] in_array)
{

    for (int i = 0; i < in_array.Length; i++)
    {
        Console.WriteLine($"Введите число № {i + 1} ");
        in_array[i] = int.Parse(Console.ReadLine());
    }

    return in_array;
}


Console.Clear();
Console.WriteLine(@"Задача 41: Пользователь вводит с клавиатуры M чисел. 
Посчитайте, сколько чисел больше 0 ввёл пользователь.
0, 7, 8, -2, -2 -> 2
 -1, -7, 567, 89, 223-> 3
");
Console.WriteLine("Введите множество от 0 до 10! M = ");
int m = int.Parse(Console.ReadLine());

if (m > 0 && m <= 10)
{
    int[] minusArray = new int[m];
    FindMinusValueInArray(UserInputValueInArray(minusArray));
}
else
{
    Console.WriteLine("Чисел больше 10 или меньше 0 перезапустите программу ");
}