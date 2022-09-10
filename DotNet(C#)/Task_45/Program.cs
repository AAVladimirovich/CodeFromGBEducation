// Задача 45: Напишите программу, которая будет создавать
// копию заданного массива с помощью поэлементного
// копирования.

int[] RandomArrayCreator(int in_arrSize, int in_minVal, int in_maxVal)
{
    var randomGod = new Random();
    int[] vFrRtrn = new int[in_arrSize];

    for (int i = 0; i < vFrRtrn.Length; i++)
    {
        vFrRtrn[i] = randomGod.Next(in_minVal, in_maxVal);
    }

    return vFrRtrn;

}

void PrintResult(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (i == 0) Console.Write(" Массив = [");
        if (i < arr.Length - 1) Console.Write(arr[i] + ",");
        else Console.Write(arr[i] + "]");
    }
}

int[] CopyArray (int[] in_array)
{
    int [] vFrRtrn = new int[in_array.Length];

    for (int i = 0; i < in_array.Length; i++)
    {
        vFrRtrn[i] = in_array[i];
    }

    return vFrRtrn;
}


int[] arVal = RandomArrayCreator(8, 1, 100);
PrintResult(arVal);
int[] answer = CopyArray(arVal);
PrintResult(answer);
