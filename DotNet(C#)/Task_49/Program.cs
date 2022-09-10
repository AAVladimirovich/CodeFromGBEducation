Console.Clear();
Console.WriteLine(@"Задача 49: Задайте двумерный массив. Найдите элементы, у
которых оба индекса чётные, и замените эти элементы на их
квадраты.
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

int[,] MatrixEvenElementSqr(int[,] in_array)
{

    for (int i = 2; i < in_array.GetLength(0); i++)
    {
        for (int j = 2; j < in_array.GetLength(1); j++)
        {
            int ostatokI = i % 2;
            int ostatokJ = j % 2;
            if (ostatokJ == 0 && ostatokI == 0) in_array[i, j] = in_array[i, j] * in_array[i, j];
        }

    }
    return in_array;
}

int[,] arrayResult = CreateMatrixRndInt(3, 4, 1, 23);
PrintMatrix(arrayResult);
Console.WriteLine(@"
Возводим в квадрат чётные элементы массива
");

arrayResult = MatrixEvenElementSqr(arrayResult);
PrintMatrix(arrayResult);