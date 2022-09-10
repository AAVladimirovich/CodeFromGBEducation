// Задача 39: Напишите программу, которая перевернёт
// одномерный массив (последний элемент будет на первом
// месте, а первый - на последнем и т.д.)
// [1 2 3 4 5] -> [5 4 3 2 1]
// [6 7 3 6] -> [6 3 7 6]

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

int[] Reverse(int[] in_array)
{

    int index1=0;
    int index2=in_array.Length-1;
    int[] temp_array = new int[in_array.Length]; 

    while(index1<in_array.Length)
    {
        temp_array[index2] = in_array[index1];
        index1 ++;
        index2 --;
    }

    return temp_array;
}

int[] arVal = RandomArrayCreator(8, 1, 100);
PrintResult(arVal);
arVal = Reverse(arVal);
//Array.Reverse(arVal);
PrintResult(arVal);