// Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
// m = 3, n = 2 -> A(m,n) = 29

int Akkerman(int m, int n)
{
    if (m == 0) return n + 1;
    else if (m > 0 && n == 0) return Akkerman(m - 1, 1);
    else if (m > 0 && n > 0) return Akkerman(m - 1, Akkerman(m, n - 1));
    return 0;
}

Console.Clear();
Console.WriteLine(@"Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. 
Даны два неотрицательных числа m и n.
m = 3, n = 2 -> A(m,n) = 29
");

Console.WriteLine("Задайте число M");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Задайте число N");
int n = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"Функция Аккермана = {Akkerman(m, n)}");
