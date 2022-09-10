// Задача 67: Напишите программу, которая будет принимать на вход число и
// возвращать сумму его цифр.
// 453 -> 12
// 45 -> 9

void SummNumbers(int argNum, int sum)
{
    int remain = argNum % 10;
    sum += remain;
    if (remain == 0) 
    {
        Console.Write($"{sum} ");
        return;
    }
    SummNumbers(argNum / 10, sum );
}

Console.Clear();
Console.WriteLine(@"Задача 67: Напишите программу, которая будет принимать на вход число и
возвращать сумму его цифр.
453 -> 12
45 -> 9
");

Console.WriteLine("Задайте число ");
int n = Convert.ToInt32(Console.ReadLine());

SummNumbers(n,0);