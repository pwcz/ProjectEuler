from math import sqrt
from timeit import timeit


def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def number_of_consecutive_primes(a, b):
    n = 0
    while is_prime(n**2 + a * n + b):
        n += 1

    return n


def input_data():
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            yield a, b


def calculate():
    result = max(((a, b, number_of_consecutive_primes(a, b)) for a, b in input_data()), key=lambda x: x[2])
    print(result)


if __name__ == "__main__":
    print(f"{timeit(stmt=calculate, number=1):.3f} s")