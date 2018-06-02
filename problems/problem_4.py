"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

MAX_POSSIBLE_NUMBER = 999 ** 2


def is_polidrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


def check_if_can_be_made_by_product_of_3_digit_numbers(j):
    for m in range(999, 99, -1):
        if j % m == 0:
            if 999 > j/m > 100:
                print(m)
                return True
    return False


for k in range(MAX_POSSIBLE_NUMBER, 1, -1):
    if is_polidrome(k):
        if check_if_can_be_made_by_product_of_3_digit_numbers(k):
            print(k)
            break
print("Program stop")
