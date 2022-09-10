// Задача 25: Напишите цикл, который принимает
// на вход два числа (A и B) и возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16

int Stepen(int in_chislo, int in_stepen)
{
    int valueForReturn = in_chislo;
    
    checked
    {
        for (int i = 1; i < in_stepen; i++)
        {
            valueForReturn *= in_chislo;
        }
    }
    
    return valueForReturn;

}

Console.WriteLine(@"Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
3, 5 -> 243 (3⁵)
2, 4 -> 16
");

Console.WriteLine("введите число A = ");
int a = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("введите число B = ");
int b = Convert.ToInt32(Console.ReadLine());

int result = Stepen(a,b);
Console.WriteLine($"-> {result}");