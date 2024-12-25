import math
import time

def fib_binet(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return round((phi**n - psi**n) / sqrt_5)

start_time = time.time()
result = fib_binet(20)
elapsed_time = (time.time() - start_time) * 1000
print(f"Result: {result}, Time: {elapsed_time:.2f} ms")
