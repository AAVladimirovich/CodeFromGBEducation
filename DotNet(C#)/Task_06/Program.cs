// Задача 6: Напишите программу,
// которая на вход принимает число и выдаёт, 
// является ли число чётным (делится ли оно на два без остатка).
// 4 -> да
// -3 -> нет
// 7 -> нет

Console.Write("Введите число a ");
int a = Convert.ToInt32(Console.ReadLine());

int ostatok = a % 2;
Console.Write($"Остаток равен {ostatok} ");
if (ostatok == 0)
    Console.Write($"Число {a} = чётное");
else
    Console.Write($"Число {a} = нечётное");
