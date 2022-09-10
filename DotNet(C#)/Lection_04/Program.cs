// работа с двумерными массивами

// string[,] table = new string[2,5];
// table[1,2] = "слово";

// for (int row = 0; row < 2; row++)
// {
//     for (int column = 0; column < 5; column++)
//     {
//         Console.WriteLine($"-{table[row,column]}-");
//     }

// }

void PrintArray(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            Console.Write($"{matr[i, j]} ");
        }

        Console.WriteLine();

    }
}

void FillArray(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            matr[i, j] = new Random().Next(1, 10);
        }
    }
}

int[,] matrix = new int[3, 4];
FillArray(matrix);
Console.WriteLine();
PrintArray(matrix);

// int Factorial (int n)
// {
//     if (n == 1) return 1;
//     else return n * Factorial (n-1);
// }

// Console.WriteLine(Factorial(5));

int Fibonacci(int n)
{
    if (n == 1 || n == 2) return 1;
    else return Fibonacci(n-1) + Fibonacci(n-2);
}

for (int i = 1; i < 50; i++)
{
    Console.WriteLine($"f({i}) = {Fibonacci(i)}");
}
