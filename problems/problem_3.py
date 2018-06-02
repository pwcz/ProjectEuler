"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


NUMBER = 600851475143


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


dividers = []
k = 2
number = NUMBER
while True:
    if number % k == 0:
        number /= k
        dividers.append(k)
    k += 1
    number = int(number)
    if k > number:
        break
print(dividers)
filter(is_prime, dividers)
print(max(dividers))
