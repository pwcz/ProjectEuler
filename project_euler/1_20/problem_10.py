"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time


t = time.process_time()
PRIME_INDEX = 10001
MAXSIZE = 2000000

sieve = [x for x in range(0, MAXSIZE)]
sieve[1] = 0
primes = []
for x in range(2, MAXSIZE - 1):
    if sieve[x] != 0:
        for j in range(x**2, MAXSIZE, x):
            sieve[j] = 0
sieve = list(filter(lambda x: x != 0, sieve))
print(sum(sieve))
print("TIME: ", time.process_time() - t)

