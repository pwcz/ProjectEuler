"""
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

MAX_POSSIBLE_NUMBER = 999 ** 2


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def check_if_can_be_made_by_product_of_3_digit_numbers(j):
    for m in range(999, 99, -1):
        if j % m == 0 and 999 > j/m > 100:
            print(f"product: {m}")
            return True
    return False


for k in range(MAX_POSSIBLE_NUMBER, 10000, -1):
    if is_palindrome(k) and check_if_can_be_made_by_product_of_3_digit_numbers(k):
        print(f"palindrome: {k}")
        break
