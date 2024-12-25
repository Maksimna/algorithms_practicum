def fib_array(n):
    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])

    return fib_numbers

n = 8
result = fib_array(n)
print(f"Fibonacci sequence up to {n}: {result}")
