// Напишите программу, которая на вход
// принимает число и выдаёт его квадрат (число
// умноженное на само себя).
// Например:
// 4 -> 16
// -3 -> 9
// -7 -> 49

Console.WriteLine("введите число");
//String str = Convert.ToString(Console.ReadLine());
int num = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"kvadrat chisla {num} budet raven {num * num}");
double d = 5.55;
int i = (int)d;
Console.WriteLine(i);

if (num > 5)
{
    Console.WriteLine("eto chislo bolshe 5");
}
else Console.WriteLine("chislo menshe 5");

// while (num > 5)
// {

// }