// Задача 31: 
// 1/Задайте массив из 12 элементов, заполненный
// случайными числами из промежутка [-9, 9]. 
// 2.Найдите сумму
// отрицательных и положительных элементов массива.
// 3. Вывести результат. Например, в массиве [3,9,-8,1,0,-7,2,-1,8,-3,-1,6] сумма
// положительных чисел равна 29, сумма отрицательных равна
// -20.

int[] CreateArrayRndInt(int size, int min, int max)
{
    int[] arr = new int[size];
    Random rnd = new Random();
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rnd.Next(min, max + 1);
    }
    return arr;
}

int[] GetSumPosNegElement(int[] arr)
{
    int sumPos = 0;
    int sumNeg = 0;
    for (int i = 0; i < arr.Length; i++)
    {

        if (arr[i] >= 0)
        {
            sumPos = sumPos + arr[i];
        }
        else
        {
            sumNeg = sumNeg + arr[i];
        }

    }

    return new int[] { sumPos, sumNeg };
}

void PrintResult(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (i == 0) Console.Write("[");
        if (i < arr.Length - 1) Console.Write(arr[i] + ",");
        else Console.Write(arr[i] + "]");
    }
}

int[] array = CreateArrayRndInt(12, -9, 9);
int[] sumArr = GetSumPosNegElement(array);
PrintResult(array);
PrintResult(sumArr);

string str = "привет";
char ch = 'a';