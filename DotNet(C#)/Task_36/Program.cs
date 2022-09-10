// Задача 36: Задайте одномерный массив, заполненный случайными числами. 
// Найдите сумму элементов, стоящих на нечётных позициях.
// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0

Console.Clear();

Console.WriteLine(@"Задача 36: Задайте одномерный массив, заполненный случайными числами. 
Найдите сумму элементов, стоящих на нечётных позициях.
[3, 7, 23, 12] -> 19
[-4, -6, 89, 6] -> 0
");

int[] RandomArrayCreator(int in_arrSize)
{
    var randomGod = new Random();
    int[] vFrRtrn = new int[in_arrSize];

    for (int i = 0; i < vFrRtrn.Length; i++)
    {
        vFrRtrn[i] = randomGod.Next(1, 100);
    }

    return vFrRtrn;

}

int OddSummator(int[] in_array)
{
    int vFrRtrn = 0;
    for (int i = 0; i < in_array.Length; i++)
    {

        vFrRtrn = Convert.ToBoolean(i % 2) ? vFrRtrn + in_array[i] : vFrRtrn;

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

int[] arrayForTask = RandomArrayCreator(8);
PrintResult(arrayForTask);
int oddSummator = OddSummator(arrayForTask);
Console.WriteLine($" Сумма нечётных индексов массива = {oddSummator}");