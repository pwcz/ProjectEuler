import timeit
from problem_21 import sum_div


abundant_numbers = {x for x in range(1, 28123) if sum_div(x) > x}


def can_be_written_as_sum(n):
    for x in abundant_numbers:
        if n - x in abundant_numbers:
            return True
    return False


def calculate():
    data = sum([x for x in range(1, 28123) if not can_be_written_as_sum(x)])
    assert data == 4179871


if __name__ == "__main__":
    print(f"{timeit.timeit(stmt=calculate, number=1):.3f} s")
