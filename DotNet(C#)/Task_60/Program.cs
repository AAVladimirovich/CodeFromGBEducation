// Задача 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
// Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
// массив размером 2 x 2 x 2
// 66(0,0,0) 25(0,1,0)
// 34(1,0,0) 41(1,1,0)
// 27(0,0,1) 90(0,1,1)
// 26(1,0,1) 55(1,1,1)

Console.Clear();
Console.WriteLine(@"Задача 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
массив размером 2 x 2 x 2
66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1)
");

List<int> CreateNumberList(int argMaxValue = 1000)
{
    
    List<int> numbersList = new List<int>();
    for (int i = 10; i < argMaxValue; i++)
        numbersList.Add(i);
    //Console.WriteLine(string.Join(",", numbersList)); // подсмотренно с интернета
    return numbersList;
}

void FillMatrixElementsWithListIntValues(int[,,] argArray, List<int> numbersList)
{
    var rndGenerator = new Random();
    int memoryIndex = 0;

    for (int i = 0; i < argArray.GetLength(0); i++)
    {
        for (int j = 0; j < argArray.GetLength(1); j++)
        {
            for (int k = 0; k < argArray.GetLength(2); k++)
            {
                memoryIndex = rndGenerator.Next(0, numbersList.Count);
                argArray[i, j, k] = numbersList[memoryIndex];
                numbersList.RemoveAt(memoryIndex);
            }
        }
    }

}

void PrintMatrix(int[,,] argArray, string argText = "")
{
    Console.WriteLine();
    if (argText != "") Console.WriteLine(@$" [{argText}] ");

    Console.WriteLine(@$"
    Массив размерности [{argArray.GetLength(0)},{argArray.GetLength(1)},{argArray.GetLength(2)}] ↓
    ");

    // for (int i = 0; i < argArray.GetLength(0); i++)
    // {

    //     for (int j = 0; j < argArray.GetLength(1); j++)
    //     {
    //         for (int k = 0; k < argArray.GetLength(2); k++)
    //         {
    //             if (k == 0) Console.Write("|");
    //             if (k < argArray.GetLength(2) - 1) Console.Write($"| [{i}][{j}][{k}] = {argArray[i, j, k],4} |");
    //             else Console.Write($"| [{i}][{j}][{k}] = {argArray[i, j, k],4} ||");
    //         }

    //     }

    //     Console.WriteLine();

    // }

    for (int i = 0; i < argArray.GetLength(0); i++)
    {

        for (int j = 0; j < argArray.GetLength(1); j++)
        {
            for (int k = 0; k < argArray.GetLength(2); k++)
            {
                if (k < argArray.GetLength(2) - 1) Console.Write($" {argArray[i, j, k],4}({i},{j},{k}) ");
                else Console.Write($" {argArray[i, j, k],4}({i},{j},{k})");
            }
            Console.WriteLine();
        }

    }
}

Console.Write("Введите количество строк для трёхмерного массива A m = ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов для трёхмерного массива A n = ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите глубина ширины для трёхмерного массива A z = ");
int z = Convert.ToInt32(Console.ReadLine());
int[,,] firstArrayForTask = new int[m, n, z];
List<int> listForNumbers = CreateNumberList(firstArrayForTask.Length);
FillMatrixElementsWithListIntValues(firstArrayForTask,listForNumbers);
PrintMatrix(firstArrayForTask, "************* трёхмерный массив с неповторяющимися числами *************");