
def find_recurring_fraction(d: int):
    i = 0
    remainders = set()
    n = 1
    while i < d:
        if n < d:
            n *= 10

        n %= d
        if n in remainders:
            return d, i
        else:
            remainders.add(n)

        i += 1


result = max((find_recurring_fraction(x) for x in range(2, 1000)), key=lambda r: r[1])
print(result)
