// Задача 64: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
// M = 1; N = 5. -> ""1, 2, 3, 4, 5""
// M = 4; N = 8. -> ""4, 6, 7, 8""

void NaturalNumbers(int argM, int argN)
{
    if (argM < argN)
    {
        if (argM > 0) Console.Write($"{argM} ");
        NaturalNumbers(argM + 1, argN);
    }
    else if (argM > argN)
    {
        NaturalNumbers(argM - 1, argN);
        if (argM > 0) Console.Write($"{argM} ");
    }
    else if (argM == argN)
    {
        if (argM > 0) Console.Write($"{argM} ");
        return;
    }

}

Console.Clear();
Console.WriteLine(@"Задача 64: Задайте значения M и N. Напишите программу, 
которая выведет все натуральные числа в промежутке от M до N.
M = 1; N = 5. -> 1, 2, 3, 4, 5
M = 4; N = 8. -> 4, 5, 6, 7, 8
");

Console.WriteLine("Задайте число M");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Задайте число N");
int n = Convert.ToInt32(Console.ReadLine());

NaturalNumbers(m, n);