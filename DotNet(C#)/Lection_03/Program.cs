// программа для упорядочивания массива от максимального числа
void PrintArray(int[] in_array)
{
    for (int i = 0; i < in_array.Length; i++)
    {
        Console.Write($"{in_array[i]},");
    }
    Console.WriteLine();
}

void SelectionMaxSort(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        int maxPosition = i;
        for (int j = i + 1; j < array.Length; j++)
        {
            if (array[j] > array[maxPosition])
            {
                maxPosition = j;
            }
        }
        int temporary = array[i];
        array[i] = array[maxPosition];
        array[maxPosition] = temporary;
        PrintArray(array);
    }
}

int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 };

SelectionMaxSort(arr);
PrintArray(arr);

