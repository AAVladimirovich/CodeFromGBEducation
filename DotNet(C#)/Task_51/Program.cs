Console.Clear();
Console.WriteLine(@"Задача 51: Задайте двумерный массив. Найдите сумму
элементов, находящихся на главной диагонали (с индексами
(0,0); (1;1) и т.д.
");

int[,] CreateMatrixRndInt(int maxRow, int maxColumn, int min, int max)
{
    int[,] arr = new int[maxRow, maxColumn];
    Random rnd = new Random();
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            arr[i, j] = rnd.Next(min, max + 1);
        }

    }
    return arr;
}

void PrintMatrix(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {

        for (int j = 0; j < arr.GetLength(1); j++)
        {
            if (j == 0) Console.Write("[");
            if (j < arr.GetLength(1) - 1) Console.Write($"| [{i}][{j}] = {arr[i, j],4} |");
            else Console.Write($"| [{i}][{j}] = {arr[i, j],4} |]");
        }

        Console.WriteLine();

    }
}

int SumDiaganaleMatrix(int[,] in_array)
{
    int sum = 0;

    for (int i = 0; i < in_array.GetLength(0); i++)
    {
        for (int j = 0; j < in_array.GetLength(1); j++)
        {
            if (i == j) sum += in_array[i, j];
        }

    }
    return sum;
}

int[,] arrayResult = CreateMatrixRndInt(7, 7, 1, 23);
PrintMatrix(arrayResult);
Console.WriteLine(@$"
Сумма основной диагонали = {SumDiaganaleMatrix(arrayResult)} 
");
//Console.WriteLine(SumDiagMatrix(arrayResult));
