"""
1--1--1
|  |  |
1--2--3
|  |  |
1--3--6

Pascal Triangle

 0                     1
 1                   1   1
 2                 1   2   1
 3               1   3   3   1
 4             1   4   6   4   1


/2n\    (2n)!
|  |  = ----
\n /     (n!)^2
"""
import math
from functools import lru_cache

GRID_SIZE = 20


def lattice_paths(n):
    return math.factorial(2*n)//(math.factorial(n)**2)


@lru_cache
def lattice_paths_2(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return lattice_paths_2(x, y - 1) + lattice_paths_2(x - 1, y)


print(lattice_paths_2(GRID_SIZE, GRID_SIZE))






