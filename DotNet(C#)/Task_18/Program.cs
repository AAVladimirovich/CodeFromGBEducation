// Задача 18: Напишите программу, которая по
// заданному номеру четверти, показывает диапазон
// возможных координат точек в этой четверти (x и y).
//Console.Clear();

Console.WriteLine("введите номер четверти");
Console.Write("Четвер?!: ");
int X = Convert.ToInt32(Console.ReadLine()); //номер четверти переменная

void Opredelitel(int in_X)
{

    switch (in_X)
    {
        case 1: Console.WriteLine("X > 0 до 2 147 483 647  и Y > 0 до 2 147 483 647"); break;
        case 2: Console.WriteLine("X < 0 до -2 147 483 648 и Y > 0 до 2 147 483 647"); break;
        case 3: Console.WriteLine("X < 0 до -2 147 483 648 и Y < 0 до -2 147 483 648"); break;
        case 4: Console.WriteLine("X > 0 до 2 147 483 647 и Y < 0 до -2 147 483 648"); break;
        default: Console.WriteLine("нет такой четверти"); break;
    }

}

Opredelitel(X);