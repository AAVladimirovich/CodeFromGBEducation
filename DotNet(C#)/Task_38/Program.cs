// Задача 38: Задайте массив вещественных чисел. 
// Найдите разницу между максимальным и минимальным элементов массива.
// [3.5, 7.1, 22.9, 2.3, 78.5] -> 76.2

Console.Clear();

Console.WriteLine(@"Задача 38: Задайте массив вещественных чисел. 
Найдите разницу между максимальным и минимальным элементов массива.
[3.5, 7.1, 22.9, 2.3, 78.5] -> 76.2
");

double[] RandomArrayCreator(int in_arrSize, double in_minDblRndValue, double in_maxDblRndValue)
{
    var randomGod = new Random();
    double[] vFrRtrn = new double[in_arrSize];

    for (int i = 0; i < vFrRtrn.Length; i++)
    {
        vFrRtrn[i] = Math.Round(randomGod.NextDouble()
                                    * (in_maxDblRndValue - in_minDblRndValue)
                                    + in_minDblRndValue, 1);
    }

    return vFrRtrn;

}

double MinMaxDiscrepancy(double[] in_array)
{

    double maxValue = in_array[0];
    double minValue = in_array[0];

    for (int i = 1; i < in_array.Length; i++)
    {
        if (in_array[i] > maxValue)
        {
            maxValue = in_array[i];
        }
        else if (in_array[i] < minValue)
        {
            minValue = in_array[i];
        }

    }

    Console.WriteLine($" максимальное число = {maxValue}");
    Console.WriteLine($" минимальное число = {minValue}");

    return maxValue - minValue;

}

void PrintResult(double[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (i == 0) Console.Write("Массив = [");
        if (i < arr.Length - 1) Console.Write(arr[i] + ",");
        else Console.WriteLine(arr[i] + "]");
    }
}

double[] arrayForTask = RandomArrayCreator(8, 1, 100);
PrintResult(arrayForTask);
double taskAnswer = MinMaxDiscrepancy(arrayForTask);
Console.WriteLine($" Разница между максимальным и минимальным числом = {taskAnswer}");