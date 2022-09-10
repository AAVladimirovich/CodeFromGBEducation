// Задача 21
// Напишите программу, которая принимает на вход 
// координаты двух точек и находит расстояние между ними в 3D пространстве.
// A (3,6,8); B (2,1,-7), -> 15.84
// A (7,-5, 0); B (1,-1,9) -> 11.53

Console.WriteLine(@"Задача 21
Напишите программу, которая принимает на вход 
координаты двух точек и находит расстояние между ними в 3D пространстве.");

Console.WriteLine("введите координаты X1,Y1,Z1 первой точки");
Console.Write("X1: ");
int X1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Y1: ");
int Y1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Z1: ");
int Z1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("введите координаты X2,Y2,Z2 второй точки");
Console.Write("X2: ");
int X2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Y2: ");
int Y2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Z2: ");
int Z2 = Convert.ToInt32(Console.ReadLine());

double result = Convert.ToDouble(Math.Sqrt(Math.Pow((X2 - X1),2) + Math.Pow((Y2-Y1),2) + Math.Pow((Z2-Z1),2)));
Console.WriteLine($"Расстояние равно = {Math.Round(result,2)}");