Console.Clear();
Console.WriteLine(@"Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
m = 3, n = 4.
0,5 7 -2 -0,2
1 -3,3 8 -9,9
8 7,8 -7,1 9
");

void FillMatrixWithRandomDoubleValue(double[,] in_array, double in_minValue, double in_maxValue)
{
    var rndGenerator = new Random();

    for (int i = 0; i < in_array.GetLength(0); i++)
    {
        for (int j = 0; j < in_array.GetLength(1); j++)
        {
            in_array[i, j] = Math.Round(rndGenerator.NextDouble()
                             * (in_maxValue - in_minValue)
                             + in_minValue, 1);
        }

    }

}

void PrintMatrix(double[,] in_array)
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

Console.Write("Введите количество строк в двумерном массиве m = ");
int m = int.Parse(Console.ReadLine());

Console.Write("Введите количество столбцов в двумерном массиве n = ");
int n = int.Parse(Console.ReadLine());

double[,] arrayResult = new double[m, n];
FillMatrixWithRandomDoubleValue(arrayResult, 0, 40);
PrintMatrix(arrayResult);
