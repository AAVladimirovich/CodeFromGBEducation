// 11. Напишите программу, которая выводит случайное
// трёхзначное число и удаляет вторую цифру этого
// числа.
// 456 -> 46
// 782 -> 72
// 918 -> 98


// 12. Напишите программу, которая будет принимать на
// вход два числа и выводить, является ли второе число
// кратным первому. Если число 2 не кратно числу 1, то
// программа выводит остаток от деления.
// 34, 5 -> не кратно, остаток 4
// 16, 4 -> кратно

// int rndNum = new Random().Next(10, 100);
// Console.WriteLine($"Случайное число из отрезка 10 - 99 => {rndNum}");

// int MaxDigit(int num)
// {
//     int firstDigit = num / 10;
//     int secondDigit = num % 10;
//     if(firstDigit == secondDigit) return 0;
//     return firstDigit > secondDigit ? firstDigit : secondDigit;
// }

// int maxDigit = MaxDigit(rndNum);
// string result = maxDigit > 0 ? maxDigit.ToString() : "числа равны";
// Console.WriteLine($"Наибольшая цифра числа {rndNum} => {result}");
