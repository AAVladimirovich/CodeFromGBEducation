// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18

Console.Clear();
Console.WriteLine(@"Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18
");

void FillMatrixElementsWithRandomIntValue(int[,] argArray, int argMinRndValue = 1, int argMaxRndValue = 20)
{
    var rndGenerator = new Random();
    int[] intArray = new int[argArray.GetLength(1)];

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

int[,] ProductOfMatrixes(int[,] argMatrixA, int[,] argMatrixB)
{

    int[,] arrayForMethodReturn = new int[argMatrixA.GetLength(0), argMatrixB.GetLength(1)];

    if (argMatrixA.GetLength(1) != argMatrixB.GetLength(0))
    {
        Console.WriteLine(@$"!!!. Внимание. Ошибка выполнения условия произведения матриц. Количество столбцов матрицы А = {argMatrixA.GetLength(0)} 
        должно совпадать с количеством строк Матрицы В = {argMatrixB.GetLength(1)}");
    }
    else
    {
        for (int i = 0; i < arrayForMethodReturn.GetLength(0); i++)
        {
            for (int j = 0; j < arrayForMethodReturn.GetLength(1); j++)
            {
                arrayForMethodReturn[i, j] = ProductExp(i, j, argMatrixA, argMatrixB);
            }
        }
        return arrayForMethodReturn;
    }
    return arrayForMethodReturn;
}

int ProductExp(int argI, int argJ, int[,] argMatrixA, int[,] argMatrixB)
{
    int valueForReturn = 0;
    for (int i = 0; i < argMatrixA.GetLength(1); i++)
    {
        valueForReturn += argMatrixA[argI, i] * argMatrixB[i, argJ];
    }
    return valueForReturn;
}

Console.Write("Введите количество строк для двумерного массива A m = ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов для двумерного массива A n = ");
int n = Convert.ToInt32(Console.ReadLine());
int[,] firstArrayForTask = new int[m, n];
Console.Write("Введите количество строк для двумерного массива B m = ");
m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов для двумерного массива B n = ");
n = Convert.ToInt32(Console.ReadLine());
int[,] secondArrayForTask = new int[m, n];

FillMatrixElementsWithRandomIntValue(firstArrayForTask);
FillMatrixElementsWithRandomIntValue(secondArrayForTask);
PrintMatrix(firstArrayForTask, "************* МАТРИЦА A *************");
PrintMatrix(secondArrayForTask, "************* МАТРИЦА B *************");

int[,] productArray = ProductOfMatrixes(firstArrayForTask, secondArrayForTask);
if (productArray[0, 0] != 0) PrintMatrix(productArray, "*************  ПРОИЗВЕДЕНИЕ МАТРИЦЫ А И B *************");