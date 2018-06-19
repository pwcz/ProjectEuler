"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import operator



class CollatzSequence:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 1:
            raise StopIteration()
        if self.n % 2 == 0:
            self.n /= 2
        else:
            self.n = 3 * self.n + 1
        return int(self.n)


results = []
for n in range(2,1000000):
    i = 0
    for _ in CollatzSequence(n):
        i += 1
    results.append([n, i])


print(max(results, key=operator.itemgetter(1)))
