Console.WriteLine(@"Задача 24: Напишите программу, которая
принимает на вход число (А) и выдаёт сумму чисел
от 1 до А.
7 -> 28
4 -> 10
8 -> 36
");

int Sum(int in_numer)
{

    int valueForReturn = 0;

    for (int i = 1; i <= in_numer; i++)
    {
        valueForReturn += i; // приравниваем к valueForReturn + i на каждом цикле
    }

    return valueForReturn;
}

Console.Write("Введите число А = ");
int num = int.Parse(Console.ReadLine());

int sum = Sum(num);
Console.WriteLine($"Сумма всех чисел от 1 до {num} = {sum}");