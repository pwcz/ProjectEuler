import timeit


def fibonacci():
    yield 1
    x, y = 0, 1
    while True:
        x, y = y, x + y
        yield y


def calculate():
    for i, x in enumerate(fibonacci()):
        if x >= 10**1000:
            print(i+1, x)
            break


if __name__ == "__main__":
    print(f"{timeit.timeit(stmt=calculate, number=1):.3f} s")