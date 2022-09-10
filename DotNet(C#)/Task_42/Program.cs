// Задача 42: Напишите программу, которая будет преобразовывать
// десятичное число в двоичное.
// 45 -> 101101
// 3 -> 11
// 2 -> 10
Console.Clear();

Console.WriteLine("Введите число: ");
int a = int.Parse(Console.ReadLine());

int TenToTwo(int n)
{
    if (n == 1) return 1;
    if (n == 0) return 0;
    return n % 2 + 10 * TenToTwo(n / 2);
}

Console.WriteLine(TenToTwo(a));

int b = 13;
void ToBin(int n, int basenum)
{
    if (n == 0) return;
    ToBin(n / basenum, basenum);
    Console.Write(n % basenum);
}

ToBin(b,2);
