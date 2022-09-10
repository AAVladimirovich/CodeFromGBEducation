// Задача 34: Задайте массив заполненный случайными положительными 
// трёхзначными числами. Напишите программу, 
// которая покажет количество чётных чисел в массиве.
// [345, 897, 568, 234] -> 2

Console.Clear();

Console.WriteLine(@"Задача 34: Задайте массив заполненный случайными положительными 
трёхзначными числами. Напишите программу, 
которая покажет количество чётных чисел в массиве.
[345, 897, 568, 234] -> 2
");

int[] ThreeElementRandomArrayCreator(int in_arrSize)
{
    var randomGod = new Random();
    int[] vFrRtrn = new int[in_arrSize];

    for (int i = 0; i < vFrRtrn.Length; i++)
    {
        vFrRtrn[i] = randomGod.Next(100, 1000);
    }

    return vFrRtrn;

}

int EvenDetector(int[] in_array)
{
    int vFrRtrn = 0;
    for (int i = 0; i < in_array.Length; i++)
    {

        bool isEven = Convert.ToBoolean(in_array[i] % 2) ? false : true;
        if (isEven) vFrRtrn++;

    }

    return vFrRtrn;

}

void PrintResult(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (i == 0) Console.Write("Массив = [");
        if (i < arr.Length - 1) Console.Write(arr[i] + ",");
        else Console.Write(arr[i] + "]");
    }
}

int[] arrayForTask = ThreeElementRandomArrayCreator(8);
PrintResult(arrayForTask);
int evenCounter = EvenDetector(arrayForTask);
Console.WriteLine($" Количество чётных чисел = {evenCounter}");