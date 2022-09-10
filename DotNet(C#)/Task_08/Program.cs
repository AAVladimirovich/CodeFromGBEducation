// Задача 8: Напишите программу, которая на вход принимает число (N), 
// а на выходе показывает все чётные числа от 1 до N.
// 5 -> 2, 4
// 8 -> 2, 4, 6, 8

Console.Write("Введите число N ");
int N = Convert.ToInt32(Console.ReadLine());

int length = N / 2;
int[] nums = new int[length];

int cnt = 0;
int i = 1;

if (N <= 1)
    Console.Write($"Число N слишком маленькое");
else
    while (i <= N)
    {
        //int ostatok = i % 2;
        if (i % 2 == 0)
        {
            nums[cnt] = i;
            cnt++;
        }
        i++;
    }

if (N > 1)
{
    Console.Write($"Чётные числа от 1 до {N} = ");

    foreach (int var in nums)
        Console.Write($"{var} ");
}
