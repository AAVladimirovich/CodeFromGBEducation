// Задача 63: Задайте значение N. Напишите программу, которая выведет
// все натуральные числа в промежутке от 1 до N.
// N = 5 -> "1, 2, 3, 4, 5"
// N = 6 -> "1, 2, 3, 4, 5, 6"

void NaturalNumbers(int argNum)
{
    if (argNum == 0) return;
    NaturalNumbers(argNum -1);
    Console.Write($"{argNum} ");
}

Console.Clear();
Console.WriteLine(@"Задача 63: Задайте значение N. Напишите программу, которая выведет
все натуральные числа в промежутке от 1 до N.
N = 5 -> 1, 2, 3, 4, 5
N = 6 -> 1, 2, 3, 4, 5, 6
");

Console.WriteLine("Задайте число");
int num = Convert.ToInt32(Console.ReadLine());


NaturalNumbers(num);