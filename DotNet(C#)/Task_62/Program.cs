// Задача 62. Заполните спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07

Console.Clear();
Console.WriteLine(@"Задача 62. Заполните спирально массив 4 на 4.
Например, на выходе получается вот такой массив:
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
");

void FillMatrixBySpiral(int[,] argArray, int argCurrentNumber, int argI, int argJ, int prohodRight, int prohodDown, int prohodLeft, int prohodUp, string direction = "Right")
{
    if (argCurrentNumber > argArray.Length ) return;
    switch (direction)
    {
        case "Right":
            argI = prohodRight;
            for (argJ = 0 + prohodUp; argJ < argArray.GetLength(1) - prohodDown; argJ++)
            {
                argArray[argI, argJ] = argCurrentNumber++;
            }
            prohodRight++;
            FillMatrixBySpiral(argArray, argCurrentNumber, argI, argJ, prohodRight, prohodDown, prohodLeft, prohodUp, "Down");
            break;
        case "Down":
            argJ = argArray.GetLength(1)-prohodRight;
            for (argI = 0 + prohodRight; argI < argArray.GetLength(0) - prohodLeft; argI++)
            {
                argArray[argI, argJ] = argCurrentNumber++;
            }
            prohodDown++;
            FillMatrixBySpiral(argArray, argCurrentNumber, argI, argJ, prohodRight, prohodDown, prohodLeft, prohodUp, "Left");
            break;
        case "Left":
            argI = argArray.GetLength(0)-prohodDown;
            for (argJ = argArray.GetLength(1) - 1 - prohodDown; argJ >= 0 + prohodUp; argJ--)
            {
                argArray[argI, argJ] = argCurrentNumber++;
            }
            prohodLeft++;
            FillMatrixBySpiral(argArray, argCurrentNumber, argI, argJ, prohodRight, prohodDown, prohodLeft, prohodUp, "Up");
            break;
        case "Up":
            argJ = prohodUp;
            for (argI = argArray.GetLength(0) - 1 - prohodLeft; argI >= 0 + prohodRight; argI--)
            {
                argArray[argI, argJ] = argCurrentNumber++;
            }
            prohodUp++;
            FillMatrixBySpiral(argArray, argCurrentNumber, argI, argJ, prohodRight, prohodDown, prohodLeft, prohodUp, "Right");
            break;
        default:
            Console.WriteLine($"SPIRAL RECURSIA!");
            break;
    }

}

void PrintMatrix(int[,] argArray, bool showIndexes, string argText = "")
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
            if (showIndexes == true)
            {
                if (j == 0) Console.Write("|");
                if (j < argArray.GetLength(1) - 1) Console.Write($"| [{i}][{j}] = {argArray[i, j],4} |");
                else Console.Write($"| [{i}][{j}] = {argArray[i, j],4} ||");
            }
            else
            {
                if (j == 0) Console.Write("|");
                if (j < argArray.GetLength(1) - 1) Console.Write($"| {argArray[i, j],4} |");
                else Console.Write($"| {argArray[i, j],4} ||");
            }
        }
        Console.WriteLine();
    }
}

Console.Write("Введите размер строк и столбцов для массива = ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите размер строк и столбцов для массива = ");
int n = Convert.ToInt32(Console.ReadLine());
int[,] firstArrayForTask = new int[m, n];
FillMatrixBySpiral(firstArrayForTask, 1, 0, 0, 0, 0, 0, 0);
PrintMatrix(firstArrayForTask, false, "************* МАТРИЦА ЗАПОЛНЕННАЯ СПИРАЛЬЮ ЦИФР *************");