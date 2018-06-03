"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import log
import time


t = time.process_time()
PRIME_INDEX = 10001
MAXSIZE = int(1.2 * PRIME_INDEX * log(PRIME_INDEX))

sieve = [x for x in range(0, MAXSIZE)]
sieve[0] = 0
sieve[1] = 0
primes = []
for x in range(2, MAXSIZE - 1):
    if sieve[x] != 0:
        for j in range(x**2, MAXSIZE, x):
                sieve[j] = 0
sieve = list(filter(lambda x: x != 0, sieve))
print(sieve[PRIME_INDEX-1])
print("TIME: ", time.process_time() - t)

