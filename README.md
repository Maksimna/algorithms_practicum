## 1.1. Вычисление n-го числа Фибоначчи с использованием рекурсивного алгоритма

- [Код пункта 1.1](https://github.com/Maksimna/algorithms_practicum/blob/main/pythonProject53453425/da.py)
> Дано целое число 1≤n≤24 , необходимо написать функцию `fib(n)` для вычисления n-го числа Фибоначчи с использованием рекурсии. Функция `fib(n)` должна вызывать сама себя в теле функции для вычисления соответствующих (n−1) и (n−2).

## 1.2. Вычисление n-го числа Фибоначчи с использованием цикла

- [Код пункта 1.2](https://github.com/Maksimna/algorithms_practicum/blob/main/pythonProject53453425/da2.py)
> Дано целое число 1≤n≤32 , необходимо написать функцию fib(n) для вычисления n-го числа Фибоначчи с использованием цикла. Функция `fib(n)` должна производить расчет от 1 до n, на каждой последующей итерации используя значение числа(чисел), необходимых для расчета, полученных на предыдущей итерации.

## 1.3. Вычисление n-го числа Фибоначчи с записью числового ряда в массив

- [Код пункта 1.3](https://github.com/Maksimna/algorithms_practicum/blob/main/pythonProject53453425/da3.py)
> Дано целое число 1≤n≤40 , необходимо написать функцию fib(n) для вычисления n-го числа Фибоначчи. Функция `fib(n)` должна в процессе выполнения записывать вычисленные значения в массив таким образом что индекс записанного числа в массиве должен соответствовать порядковому номеру числа Фибоначчи. При этом уже вычисленные значения должны браться из массива, а вновь вычисляемые должны записываться в массив только в случае если они еще не были вычислены.

## 1.4 Вычисление n-го числа Фибоначчи при помощи формулы Бине
- [Код пункта 1.4](https://github.com/Maksimna/algorithms_practicum/blob/main/pythonProject53453425/da4.py)
> Дано целое число 1≤n≤64 , необходимо написать функцию fib(n) для вычисления n-го числа Фибоначчи. Функция `fib(n)` должна производить вычисление по формуле Бине.
> $F(n) = 5 \left( 2 + \frac{5}{1} \right)^n - \left( 2 - \frac{5}{1} \right)^n$


## 1.5. Определение четности n-го большого числа Фибоначчи

- [Код пункта 1.5](https://github.com/Maksimna/algorithms_practicum/blob/main/pythonProject53453425/da5.py)
> Дано целое число 1≤n≤10<sup>6</sup> необходимо написать функцию `fib_eo(n)` для определения четности n-го числа Фибоначчи.
> Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением. В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи: если 0≤a,b≤9 — последние цифры чисел F<sub>n</sub> и F<sub>n+1</sub> соответственно, то (a+b)mod10 — последняя цифра числа F<sub>n+2</sub>
