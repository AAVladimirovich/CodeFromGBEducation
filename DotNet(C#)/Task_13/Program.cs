// Задача 13: Напишите программу, которая выводит 
//третью цифру заданного числа или сообщает, что третьей цифры нет.
// 645 -> 5
// 78 -> третьей цифры нет
// 32679 -> 6

int Razryad(int in_number)
{
    int _Razryad = 0;
    while (in_number != 0)
    {
        in_number /= 10;
        _Razryad++;
    }

    return _Razryad;

}

void ThirdChisloIdentifier(int in_number, int in_razryadVhodnogoChisla, int in_kakoeChisloNaiti)
{
    int i = in_kakoeChisloNaiti;
    while (i < in_razryadVhodnogoChisla)
    {
        //отсекаем ненужные разряды
        in_number /= 10;
        i++;
    }

    Console.Write($"{in_kakoeChisloNaiti} - тье число равно -> {in_number % 10}");

}

Console.Write("Введите число a = ");
int a = Convert.ToInt32(Console.ReadLine());

if (a < 100)
{
    Console.Write("третьей цифры нет");
}
else
{
    ThirdChisloIdentifier(a, Razryad(a), 3);
}
