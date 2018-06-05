"""
 Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time


def get_b(a):
    return 1000*(a-500)/(a-1000)


def get_c(a, b):
    return 1000 - (a+b)


t = time.process_time()
for a in range(1, 1000):
    b = get_b(a)
    c = get_c(a, b)
    if float(a).is_integer() and float(b).is_integer() and float(c).is_integer() and min([a, b, c]) > 0:
        print(a, b, c)
        print(a*b*c)
        break
print("TIME: {:.5f} ms".format(1000*(time.process_time() - t)))