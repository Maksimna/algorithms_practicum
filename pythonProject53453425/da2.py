import time

def fib_loop(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

start_time = time.time()
result = fib_loop(20)
elapsed_time = (time.time() - start_time) * 1000
print(f"Result: {result}, Time: {elapsed_time:.2f} ms")
