import timeit
from math import sqrt


def sum_divisors(n):
    return sum([x for x in range(1, n) if n % x == 0])


def sum_div(n):
    if n == 1:
        return 0
    r = int(sqrt(n))
    result = 0
    if r*r == n:
        result = r
        r -= 1

    for x in range(2, r+1):
        if n % x == 0:
            k = n//x
            result += k + x

    return result + 1


def is_amicable(a):
    b = sum_div(a)
    if a != b:
        return sum_div(b) == a
    else:
        return False


def calculate():
    print((sum([x for x in range(2, 10000) if is_amicable(x)])))


print(f"{timeit.timeit(stmt=lambda: calculate(), number=1):.3f} s")
