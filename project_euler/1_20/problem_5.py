"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import defaultdict
NUMBER = 20


def get_dividers(n):
    divs = defaultdict(int)
    k = 2
    while True:
        if n % k == 0:
            divs[k] += 1
            n /= k
        else:
            k += 1
        if k > n:
            return divs.items()


result = defaultdict(int)
for i in range(2, NUMBER+1):
    for key, val in get_dividers(i):
        if result[key] < val:
            result[key] = val

numb = 1
for key, val in result.items():
    numb *= key ** val

print(numb)
