def fib_eo(n):
    if n <= 1:
        return "even" if n == 0 else "odd"
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return "even" if b % 2 == 0 else "odd"

print(f"fib_eo(841645) = {fib_eo(841645)}")
