// 11. Напишите программу, которая выводит случайное
// трёхзначное число и удаляет вторую цифру этого
// числа.
// 456 -> 46
// 782 -> 72
// 918 -> 98
var randomGod = new Random();
int rndNum = randomGod.Next(101, 1000);
Console.WriteLine($"Случайное число из отрезка 100 - 999 => {rndNum}");

// int MaxDigit(int num)
// {
//     int firstDigit = num / 100;
//     int lastDigit = num % 10;
//     //if(firstDigit == lastDigit) return 0;
//     //return firstDigit > lastDigit ? firstDigit : lastDigit;
// }

int firstDigit = rndNum / 100;
int lastDigit = rndNum % 10;

//int maxDigit = MaxDigit(rndNum);
//string result = maxDigit > 0 ? maxDigit.ToString() : "числа равны";
//Console.WriteLine($"Наибольшая цифра числа {firstDigit} => {lastDigit}");

Console.WriteLine($"{firstDigit}{lastDigit}");
Console.WriteLine(firstDigit*10 + lastDigit);