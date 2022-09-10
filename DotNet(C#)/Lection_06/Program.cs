using System.Linq;

void PrintMatrix((int x, int y)[]arr)
{
    //Console.WriteLine(arr.GetLength(0));

    foreach (var e in arr)
    {

            Console.WriteLine($"{e}");
            //Console.WriteLine($"{y}");
    }
    //  for (int i = 0; i < arr.GetLength(0); i++)
    //  {

    //     //  for (int j = 0; j < arr.GetLength(1); j++)
    //     //  {
    //         //  if (i == 0) Console.Write("");
    //         //  if (i < arr.GetLength(0) - 1) Console.Write($"| [{i}] = {arr[i],4} |");
    //         //  else Console.Write($"| [{i}] = {arr[i],4} |");

    //         if (i == 0) Console.Write("");
    //          if (i < arr.GetLength(0) - 1) Console.Write($"| [{e[i]} |");
    //          else Console.Write($"| [{e[i]} |");
    //     //  }

    //      Console.WriteLine();

    //  }

}

string text = "(1,2) (2,3) (4,5) (6,7)" 
                .Replace("(","")
                .Replace(")","");

Console.WriteLine(text);                
// if (e.KeyCode == Keys.Enter) 
// {
//     e.SuppressKeyPress = true;
// }
// Console.Write("Введите число a ");
// int a = Convert.ToInt32(Console.ReadLine());
// if (a % 2 == 0) Console.WriteLine("Чётное"); else Console.WriteLine("Нечётное");
var data = text.Split(" ")
            .Select(item => item.Split(','))
            .Select(e => ( x: int.Parse(e[0]), y: int.Parse(e[1])))
            .Where(e => e.y % 2 == 1)
            .Select(point => ( point.x , point.y * 10))
            .ToArray();

//data.Type() == typeof(int);

// (int, int)[] intervals = new (int, int)[3];
// var interval = intervals[0];
// var item1 = interval.Item1;
// var item2 = interval.Item2;

// for (int i = 0; i < data.Length; i++)
// {
//         Console.WriteLine(data[i]);
//         // Console.WriteLine(data[i].x*10);
//         // Console.WriteLine(data[i].y);
// }

// {
//     // Console.WriteLine(data[i]);
//     for (int k = 0; k < data[i].Length; k++)
//     {
//         Console.WriteLine(data[i][k]);
//     }
// }


PrintMatrix(data);