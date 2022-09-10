Console.WriteLine(@"Задача 26: Напишите программу, которая принимает
на вход число и выдаёт количество цифр в числе.
456 -> 3
78 -> 2
89126 -> 5
");

Console.WriteLine("Введите число:  ");
int num = int.Parse(Console.ReadLine());
int count = 0;
while (num != 0)
{
    num /= 10;
    count++;
    // Console.WriteLine(num%10);
}
Console.WriteLine($"-> {count}");
