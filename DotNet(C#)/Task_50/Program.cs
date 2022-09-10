Console.Clear();
Console.WriteLine(@"Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,
 и возвращает значение этого элемента или же указание, что такого элемента нет.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
1, 7 -> такого числа в массиве нет
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

string FindElementInMatrix(int[,] in_array, int in_rowToFind, int in_columnToFind)
{

    if (in_rowToFind >= in_array.GetLength(0) || in_columnToFind >= in_array.GetLength(1) || in_rowToFind <= 0 || in_columnToFind <= 0)
        return $"[{in_rowToFind},{in_columnToFind}] = такого элемента в матрице нет";
    else return $"[{in_rowToFind},{in_columnToFind}] = {in_array[in_rowToFind, in_columnToFind]}";

}

Console.Write("Введите количество строк в двумерном массиве m = ");
int m = int.Parse(Console.ReadLine());
Console.Write("Введите количество столбцов в двумерном массиве n = ");
int n = int.Parse(Console.ReadLine());

int[,] arrayResult = new int[m, n];

FillMatrixWithRandomIntValue(arrayResult, 0, 40);
PrintMatrix(arrayResult);

Console.Write("введите строку для поиска элемента = ");
int rowToFind = int.Parse(Console.ReadLine());
Console.Write("Введите столбец для поиска элемента = ");
int columnToFind = int.Parse(Console.ReadLine());

Console.WriteLine($"для поиска выбран элемент {FindElementInMatrix(arrayResult, rowToFind, columnToFind)}");