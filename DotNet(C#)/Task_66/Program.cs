// Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30

void SummaOfNaturalNumbers(int argM, int argN, int argSumma)
{
    if (argM < argN)
    {
        if (argM > 0) SummaOfNaturalNumbers(argM + 1, argN, argSumma + argM); else SummaOfNaturalNumbers(argM + 1, argN, argSumma + 0);
    }
    else if (argM > argN)
    {
        if (argM > 0) SummaOfNaturalNumbers(argM - 1, argN, argSumma + argM); else SummaOfNaturalNumbers(argM - 1, argN, argSumma + 0);
        
    }
    else if (argM == argN)
    {
        if (argM > 0) Console.Write($" {argSumma + argM} "); else Console.Write($" {argSumma} ");
        return;
    }

}

Console.Clear();
Console.WriteLine(@"Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
M = 1; N = 15 -> 120
M = 4; N = 8. -> 30
");

Console.WriteLine("Задайте число M");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Задайте число N");
int n = Convert.ToInt32(Console.ReadLine());

SummaOfNaturalNumbers(m, n, 0);