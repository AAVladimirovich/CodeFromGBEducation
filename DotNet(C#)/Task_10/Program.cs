// Задача 10: Напишите программу, которая принимает на вход 
//трёхзначное число и на выходе показывает вторую цифру этого числа.
// 456 -> 5
// 782 -> 8
// 918 -> 1

var randomGod = new Random();
int rndNum = randomGod.Next(100, 1000);

string num2identifier (int in_number)
{
    return ($"вторая цифра числа {in_number} -> {in_number % 100 / 10}");
}

Console.Write(num2identifier(rndNum));