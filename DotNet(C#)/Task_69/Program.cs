// Задача 69: Напишите программу, которая на вход принимает два числа A и B, и
// возводит число А в целую степень B с помощью рекурсии.
// A = 3; B = 5 -> 243 (3⁵)
// A = 2; B = 3 -> 8

void PowerNumber(int argN, int argPower, int argMemory)
{
    if (argPower == 0) 
    {
        Console.Write("1");
        return;
    }
    if (argPower > 1)
    {
        argN *=  argMemory;
        PowerNumber(argN, argPower - 1, argMemory);
        return; 
    }
    else
    {
        Console.Write($"{argN} ");
    }

}

Console.Clear();
Console.WriteLine(@"Задача 69: Напишите программу, которая на вход принимает два числа A и B, и
возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
");

Console.WriteLine("Задайте число для возведения в степень");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Задайте степень для числа");
int m = Convert.ToInt32(Console.ReadLine());

PowerNumber(n, m, n);


// int SquareNumber(int a, int b)
// {
//     if (b == 0) return 1;
//    return SquareNumber(a, b - 1) * a;
    
// }
// int number = SquareNumber(a, b);
// Console.WriteLine(number);

// int NaturalNumber(int n)
// {
//     if (n != 0) return n % 10 + NaturalNumber(n / 10);
//     return 0;
// }
// int number = NaturalNumber(num);
// Console.WriteLine(number);

