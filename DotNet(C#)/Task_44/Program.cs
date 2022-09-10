// Задача 44: Не используя рекурсию, выведите первые N чисел
// Фибоначчи. Первые два числа Фибоначчи: 0 и 1.
// Если N = 5 -> 0 1 1 2 3
// Если N = 3 -> 0 1 1
// Если N = 7 -> 0 1 1 2 3 5 8
Console.Clear();
// Console.WriteLine("Введите число N: ");
// int n = int.Parse(Console.ReadLine());

// void Fibona(int in_num)
// {
//     int f1 = 0;
//     int f2 = 1;
//     int f3 = 0;
//     int fSum = 0;
//     int [] fib = new int [in_num];
//     if (in_num < 2)
//     {
//         Console.WriteLine($"fibonachi dlya {in_num} = ");
//         return;
//     }

//     for (int i = 2; i < in_num; i++)
//     {
//         // f3 = i + f1; 

//         fib[i] = i-1 + i -2;
//         Console.WriteLine($"f = {fib[i]}");
//     }
// }



// Fibona(n);

Console.WriteLine("Введите число N: ");
int n = Convert.ToInt32(Console.ReadLine());

void Fibonacci(int in_num)
{
    int f1 = 0;
    int f2 = 1;
    int sum = 0;
    Console.Write($"{f1} {f2}");

    for (int i = 1; i <= in_num; i++)
    {
        sum = f1 + f2;
        f1 = f2;
        f2 = sum;
        Console.WriteLine($"F({i}) = {sum}");
    }
}

Fibonacci(n);
