Console.Clear();
Console.WriteLine(@"Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
");

void FillMatrixWithRandomIntValue(int[,] in_array, int in_minValue, int in_maxValue)
{
    var rndGenerator = new Random();

    for (int i = 0; i < in_array.GetLength(0); i++)
    {
        for (int j = 0; j < in_array.GetLength(1); j++)
        {
            in_array[i, j] = rndGenerator.Next(in_minValue, in_maxValue + 1);
        }

    }

}

void PrintMatrix(int[,] in_array)
{
    Console.WriteLine(@$"
    Массив размерности [{in_array.GetLength(0)},{in_array.GetLength(1)}] ↓
    ");

    for (int i = 0; i < in_array.GetLength(0); i++)
    {

        for (int j = 0; j < in_array.GetLength(1); j++)
        {
            if (j == 0) Console.Write("|");
            if (j < in_array.GetLength(1) - 1) Console.Write($"| [{i}][{j}] = {in_array[i, j],4} |");
            else Console.Write($"| [{i}][{j}] = {in_array[i, j],4} ||");
        }

        Console.WriteLine();

    }
}

void PrintArray(double[] in_array)
{
    Console.WriteLine(@$"
    Среднее арифметическое каждого столбца ↓
    ");

    for (int i = 0; i < in_array.GetLength(0); i++)
    {


        if (i == 0) Console.Write("[");
        if (i < in_array.GetLength(0) - 1) Console.Write($" {in_array[i],4};");
        else Console.Write($" {in_array[i],4} ]");


    }
}

double[] SummarizeElementsByRow(int[,] in_array)
{
    double[] valueForReturn = new double[in_array.GetLength(0)];

    for (int i = 0; i < in_array.GetLength(0); i++)
    {

        for (int j = 0; j < in_array.GetLength(1); j++)
        {
            valueForReturn[i] += in_array[i, j];
        }

        valueForReturn[i] = valueForReturn[i] / in_array.GetLength(1);

    }

    return valueForReturn;

}

Console.Write("Введите количество строк в двумерном массиве m = ");
int m = int.Parse(Console.ReadLine());
Console.Write("Введите количество столбцов в двумерном массиве n = ");
int n = int.Parse(Console.ReadLine());

int[,] arrayResult = new int[m, n];
FillMatrixWithRandomIntValue(arrayResult, 0, 40);
PrintMatrix(arrayResult);

double[] summarizedArray = SummarizeElementsByRow(arrayResult);
PrintArray(summarizedArray);