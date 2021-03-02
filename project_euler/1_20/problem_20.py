import timeit
import math
from functools import reduce
import operator


def power_1(n):
    if n < 3:
        return n
    else:
        return n * power_1(n-1)


def power_2(n):
    result = 1
    for x in range(2, n+1):
        result *= x

    return result


def power_3(n):
    return math.factorial(n)


def power_4(n):
    return reduce(operator.mul, range(1, n+1), 1)


def method(n):
    return sum([int(x) for x in str(globals()[f"power_{n}"](100))])


for method_number in range(1, 5):
    print(f"method {method_number} {timeit.timeit(stmt=lambda: method(method_number), number=1000)*1000:.2f} ms")


"""
method 1 45.74 ms
method 2 30.10 ms
method 3 23.86 ms
method 4 29.76 ms
"""