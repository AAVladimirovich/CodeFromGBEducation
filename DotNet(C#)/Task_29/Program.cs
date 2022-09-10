// Задача 29: Напишите программу, которая задаёт массив из 8 элементов, 
// заполненный псевдослучайными числами и выводит их на экран.
// 1, 2, 5, 7, 19, 6, 1, 33 -> [1, 2, 5, 7, 19, 6, 1, 33]

Console.Clear();

Console.WriteLine(@"Задача 29: Напишите программу, которая задаёт массив из 8 элементов, 
заполненный псевдослучайными числами и выводит их на экран.
1, 2, 5, 7, 19, 6, 1, 33 -> [1, 2, 5, 7, 19, 6, 1, 33]
");

int[] EightElementRandomArrayCreator()
{
    var randomGod = new Random();
    int[] valueForReturn = new int[8];

    checked
    {
        for (int i = 0; i < valueForReturn.Length; i++)
        {
            valueForReturn[i] = randomGod.Next(1, 999);
        }
    }

    return valueForReturn;

}

string ArrayToString(int[] in_array)
{
    string valueForReturn = "";

    for (int i = 0; i < in_array.Length; i++)
    {
        if (in_array[i] != in_array.Last())
        {
            valueForReturn = valueForReturn + Convert.ToString(in_array[i]) + ",";
        }
        else
        {
            valueForReturn = valueForReturn + Convert.ToString(in_array[i]);
        }

    }

    valueForReturn = "[" + valueForReturn + "]";
    return valueForReturn;
}

int[] result = EightElementRandomArrayCreator();
string answer = ArrayToString(result);
Console.WriteLine($"-> {answer}");