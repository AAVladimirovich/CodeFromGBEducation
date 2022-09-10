// Задача 19
// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// 14212 -> нет
// 12821 -> да
// 23432 -> да

int RazryadOpredelitel(int in_number)
{
    int _Razryad = 0;
    while (in_number != 0)
    {
        in_number /= 10;
        _Razryad++;
    }
    return _Razryad;

}

int ChisloIdentifier(int in_number, int in_razryadVhodnogoChisla, int in_kakoeChisloNaiti)
{
    int i = in_kakoeChisloNaiti;
    while (i < in_razryadVhodnogoChisla)
    {
        //отсекаем ненужные разряды
        in_number /= 10;
        i++;
    }

    return in_number % 10;

}

Console.WriteLine(@"Задача 19
Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");

Console.WriteLine("введите 5-ти значное число N ");
int N = Convert.ToInt32(Console.ReadLine());

if (N < 10000)
{
    Console.WriteLine("число N не пятизначное");
}
else
{

    bool polindrom = true;
    int frstCifra = 0;
    int scndCifra = 0;
    int vsegoRazryadov = RazryadOpredelitel(N);
    int i = 1;

    while (i <= vsegoRazryadov)
    {
        frstCifra = ChisloIdentifier(N, vsegoRazryadov, i);
        scndCifra = ChisloIdentifier(N, vsegoRazryadov, vsegoRazryadov - i + 1);

        if (frstCifra != scndCifra)
        {
            Console.WriteLine($"Число {N} не является полиндромом");
            polindrom = false;
            break;
        }
        i++;
    }

    if (polindrom == true) Console.WriteLine($"Число {N} является полиндромом");

}