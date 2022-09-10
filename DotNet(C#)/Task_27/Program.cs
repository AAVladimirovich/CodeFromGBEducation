// Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
// 452 -> 11
// 82 -> 10
// 9012 -> 12

Console.Clear();

Console.WriteLine(@"Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
452 -> 11
82 -> 10
9012 -> 12
");

int Summator(int in_chislo)
{
    int valueForReturn = 0;

    checked
    {
        while (in_chislo > 0)
        {
            valueForReturn += in_chislo % 10;
            in_chislo /= 10;
        }
    }


    return valueForReturn;

}

Console.WriteLine("введите число N = ");
int n = Convert.ToInt32(Console.ReadLine());


int result = Summator(n);
Console.WriteLine($"-> {result}");