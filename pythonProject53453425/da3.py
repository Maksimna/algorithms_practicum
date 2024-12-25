import time

def fib_array(n):
    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    return fib_numbers

start_time = time.time()
result = fib_array(20)
elapsed_time = (time.time() - start_time) * 1000
print(f"Result: {result}, Time: {elapsed_time:.2f} ms")
