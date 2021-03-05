"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import timeit


def permutation(data: str):
    pool = list(data)
    last_index = len(pool) - 1

    if last_index <= 0:
        return data   # return the same string if n is less than 1
    
    yield ''.join(pool)  # output the first permutation as itself

    while True:
        try:
            j = next(j for j in range(last_index-1, -1, -1) if pool[j] < pool[j+1])
        except StopIteration:
            break

        # Increase pool[j] by the smallest feasible amount
        # in this case pool[i] is the smallest element greater than
        # pool[j] that can legitimately follow pool[0] ... pool[j-1] in a permutation
        i = next(i for i in range(last_index, -1, -1) if pool[j] < pool[i])
        pool[j], pool[i] = pool[i], pool[j]

        # Reverse pool[j+1] ... pool[n]
        # Find the lexicographically least way to extend the new
        # pool[0]...pool[j] to a complete pattern
        if j <= last_index - 2:
            pool[j + 1:] = pool[-1:j:-1]

        yield ''.join(pool)


def calculate():
    for i, x in enumerate(permutation("0123456789")):
        if i + 1 == 10**6:
            print(x)
            break


if __name__ == "__main__":
    print(f"{timeit.timeit(stmt=calculate, number=1):.3f} s")
