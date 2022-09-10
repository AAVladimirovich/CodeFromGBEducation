// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// В итоге получается вот такой массив:
// 1 2 4 7
// 2 3 5 9
// 2 4 4 8.

Console.Clear();

Console.WriteLine(@"Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
1 2 4 7
2 3 5 9
2 4 4 8.
");

void FillMatrixElementsWithRandomIntValue(int[,] argArray, int argMinRndValue = 1, int argMaxRndValue = 99)
{
    var rndGenerator = new Random();

    for (int i = 0; i < argArray.GetLength(0); i++)
    {
        for (int j = 0; j < argArray.GetLength(1); j++)
        {
            argArray[i, j] = rndGenerator.Next(argMinRndValue, argMaxRndValue + 1);
        }

    }

}

void PrintMatrix(int[,] argArray, string argText = "")
{
    Console.WriteLine();
    if (argText != "") Console.WriteLine(@$" [{argText}] ");

    Console.WriteLine(@$"
    Массив размерности [{argArray.GetLength(0)},{argArray.GetLength(1)}] ↓
    ");

    for (int i = 0; i < argArray.GetLength(0); i++)
    {

        for (int j = 0; j < argArray.GetLength(1); j++)
        {
            if (j == 0) Console.Write("|");
            if (j < argArray.GetLength(1) - 1) Console.Write($"| [{i}][{j}] = {argArray[i, j],4} |");
            else Console.Write($"| [{i}][{j}] = {argArray[i, j],4} ||");
        }

        Console.WriteLine();

    }
}

void PrintArray(int[] argArray, string argText = "")
{
    Console.WriteLine();
    if (argText != "") Console.WriteLine(@$" [{argText}] ");

    for (int i = 0; i < argArray.GetLength(0); i++)
    {
        if (i == 0) Console.Write("[");
        if (i < argArray.GetLength(0) - 1) Console.Write($" {argArray[i],4};");
        else Console.Write($" {argArray[i],4} ]");
    }
}


int[] ConvertToOneDimensionArray(int[,] argArray)
{

    int[] valueForMethodReturn = new int[argArray.Length];
    int count = 0;
    
    foreach(var element in argArray)
    {
        valueForMethodReturn[count++] = element;
    }

    return valueForMethodReturn;

}

int[] SummUniqValuesInArray(int[] argArray, int[] argArray2)
{
    int count = 0;
    int actualValue = argArray[0];
    int iForSecondArray = 0;

    for (int i = 0; i < argArray.Length; i++)
    {
        if (actualValue == argArray[i])
        {
            count++;
        }
        else
        {
            actualValue = argArray[i];
            argArray2[iForSecondArray++] = count;
            count = 1;
        }

        if (i == argArray.Length - 1)
        {
            argArray2[iForSecondArray] = count;
        }

    }

    return argArray2;

}

Console.Write("Введите количество строк в двумерном массиве m = ");
int m = int.Parse(Console.ReadLine());
Console.Write("Введите количество столбцов в двумерном массиве n = ");
int n = int.Parse(Console.ReadLine());
int[,] arrayForTask = new int[m, n];

FillMatrixElementsWithRandomIntValue(arrayForTask, argMaxRndValue: 10);
PrintMatrix(arrayForTask,"Первоначальный массив:");

int[] oneDimensionArray = ConvertToOneDimensionArray(arrayForTask);
Array.Sort(oneDimensionArray);
PrintArray(oneDimensionArray,"Массив после метода ConvertToOneDimensionArray и метода Array.Sort(oneDimensionArray)");

int[] uniqArray = oneDimensionArray.Distinct().ToArray();
PrintArray(uniqArray,"Массив уникальных значений после int[] uniqArray = oneDimensionArray.Distinct().ToArray() ");

uniqArray = SummUniqValuesInArray(oneDimensionArray, uniqArray);
PrintArray(uniqArray,"Массив после использования метода SummUniqValuesInArray = ");
