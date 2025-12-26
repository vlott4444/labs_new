using System;

class Program
{
    static void Main(string[] args)
    {
        double a = 0, b = 0, c = 0;
        bool useConsoleColors = true;

        try
        {
            if (args.Length >= 3)
            {


                if (!TryParseCoefficient(args[0], out a))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Ошибка: коэффициент A задан некорректно");
                    Console.ResetColor();
                    return;
                }

                if (!TryParseCoefficient(args[1], out b))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Ошибка: коэффициент B задан некорректно");
                    Console.ResetColor();
                    return;
                }

                if (!TryParseCoefficient(args[2], out c))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Ошибка: коэффициент C задан некорректно");
                    Console.ResetColor();
                    return;
                }

                Console.WriteLine($"Коэффициенты: A = {a}, B = {b}, C = {c}");
            }
            else
            {
                Console.WriteLine("Ввод коэффициентов с клавиатуры...");
                a = GetCoefficientFromConsole("A");
                b = GetCoefficientFromConsole("B");
                c = GetCoefficientFromConsole("C");
            }


            if (Math.Abs(a) < 0.0000001)
            {
                if (useConsoleColors) Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nКоэффициент A = 0. Уравнение не является квадратным!");


                if (Math.Abs(b) < 0.0000001)
                {
                    if (Math.Abs(c) < 0.0000001)
                    {
                        Console.WriteLine("Уравнение 0 = 0 имеет бесконечное множество решений");
                    }
                    else
                    {
                        Console.WriteLine($"Уравнение {c} = 0 не имеет решений");
                    }
                }
                else
                {
                    double x = -c / b;
                    if (useConsoleColors) Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"Это линейное уравнение. Корень: x = {x:F4}");
                }

                if (useConsoleColors) Console.ResetColor();
                WaitForExit();
                return;
            }


            double discriminant = b * b - 4 * a * c;
            Console.WriteLine($"\nДискриминант D = b² - 4ac = {discriminant:F4}");


            if (discriminant > 0)
            {

                double x1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
                double x2 = (-b - Math.Sqrt(discriminant)) / (2 * a);

                if (useConsoleColors) Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"\nУравнение имеет два различных вещественных корня:");
                Console.WriteLine($"x₁ = {x1:F4}");
                Console.WriteLine($"x₂ = {x2:F4}");


                Console.WriteLine($"\nПроверка:");
                Console.WriteLine($"Для x₁: {a:F2}*({x1:F4})² + {b:F2}*({x1:F4}) + {c:F2} = " +
                                $"{a * x1 * x1 + b * x1 + c:E2}");
                Console.WriteLine($"Для x₂: {a:F2}*({x2:F4})² + {b:F2}*({x2:F4}) + {c:F2} = " +
                                $"{a * x2 * x2 + b * x2 + c:E2}");
            }
            else if (Math.Abs(discriminant) < 0.0001)
            {

                double x = -b / (2 * a);

                if (useConsoleColors) Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"\nУравнение имеет один вещественный корень (кратности 2):");
                Console.WriteLine($"x = {x:F4}");


                Console.WriteLine($"\nПроверка: {a:F2}*({x:F4})² + {b:F2}*({x:F4}) + {c:F2} = " +
                                $"{a * x * x + b * x + c:E2}");
            }
            else
            {

                double realPart = -b / (2 * a);
                double imaginaryPart = Math.Sqrt(-discriminant) / (2 * a);

                if (useConsoleColors) Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"\nУравнение имеет два комплексных корня:");
                Console.WriteLine($"x₁ = {realPart:F4} + {imaginaryPart:F4}i");
                Console.WriteLine($"x₂ = {realPart:F4} - {imaginaryPart:F4}i");
            }

            if (useConsoleColors) Console.ResetColor();
        }
        catch (Exception ex)
        {
            if (useConsoleColors) Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"\nПроизошла непредвиденная ошибка: {ex.Message}");
            if (useConsoleColors) Console.ResetColor();
        }

        WaitForExit();
    }







    static double GetCoefficientFromConsole(string coefficientName)
    {
        while (true)
        {
            Console.Write($"Введите коэффициент {coefficientName}: ");
            string input = Console.ReadLine();

            if (TryParseCoefficient(input, out double value))
            {
                return value;
            }

            Console.WriteLine($"Некорректный ввод. Пожалуйста, введите действительное число.");
        }
    }





    static bool TryParseCoefficient(string input, out double result)
    {

        if (double.TryParse(input, out result))
        {
            return true;
        }


        input = input.Replace(',', '.').Trim();

        if (double.TryParse(input, System.Globalization.NumberStyles.Any,
            System.Globalization.CultureInfo.InvariantCulture, out result))
        {
            return true;
        }

        result = 0;
        return false;
    }






    static void WaitForExit()
    {
        Console.WriteLine("\nНажмите любую клавишу для выхода...");
        Console.ReadKey();
    }
}
