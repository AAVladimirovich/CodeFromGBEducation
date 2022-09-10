// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// В итоге получается вот такой массив:
// 1 2 4 7
// 2 3 5 9
// 2 4 4 8.

using System.Linq;

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

void FillMatrixElementsWithRandomIntValue(int[,] argArray, int argMinRndValue = 1, int argMaxRndValue = 20)
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

string RowToString(int[,] argArray, int argI, string textSeparator = ",")
{

    string valueForMethodReturn = "";

    for (int j = 0; j < argArray.GetLength(1); j++)
    {
        if (j == 0) valueForMethodReturn = Convert.ToString(argArray[argI, j]); else valueForMethodReturn += textSeparator + Convert.ToString(argArray[argI, j]);
    }

    return valueForMethodReturn;
}

void StringToIntArray(string[] argStringArray, int[] argIntArray)
{

    int cnt = 0;
    foreach (var element in argStringArray)
    {
        argIntArray[cnt++] = Convert.ToInt32(element);
    }
}

void ColumnSeparatorChanger(int[,] argArray)
{

    string rowToOneString = "";
    string[] stringArray = new string[argArray.GetLength(1)];
    int[] intArray = new int[argArray.GetLength(1)];

    for (int i = 0; i < argArray.GetLength(0); i++)
    {
        //цикл для присваивания значений массива в одну строку и добавляем сепаратор ","
        rowToOneString = RowToString(argArray, i);

        //присваиваем в массив через метод Split строки
        stringArray = rowToOneString.Split(",");

        //конвертируем значения строкового массива в инт массив
        StringToIntArray(stringArray,intArray);

        //упорядочиваем по возрастанию и переворачиваем массив
        Array.Sort(intArray);
        Array.Reverse(intArray);

        //присваиваем уже перевернутый отсортированный массив intVar в целевой массив задачи
        for (int j = 0; j < argArray.GetLength(1); j++)
        {
            argArray[i, j] = intArray[j];
        }

    }

}

Console.Write("Введите количество строк в двумерном массиве m = ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов в двумерном массиве n = ");
int n = Convert.ToInt32(Console.ReadLine());
int[,] arrayForTask = new int[m, n];

FillMatrixElementsWithRandomIntValue(arrayForTask);
PrintMatrix(arrayForTask, "!!!!!!Первоначальный массив:");

ColumnSeparatorChanger(arrayForTask);
PrintMatrix(arrayForTask, "!!!!!!Переформатированный массив после метода ColumnSeparatorChanger(arrayForTask)");