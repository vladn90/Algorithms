""" Two ways to reverse a number in Python, i.e. 12345 > 54321.
"""
import random
from time import time


def reverse_number_1(n):
    """ Pythonic way to reverse a number.
    """
    return int(str(n)[::-1])


def reverse_number_2(n):
    """ Using arithmetic operations to reverse a number.
    """
    # special case, n == 0
    if n == 0:
        return 0

    # reverse number
    result = 0  # reversed number
    while n > 0:
        digit = n % 10  # current digit, starting from the last one
        result *= 10
        result += digit
        n //= 10
    return result


if __name__ == "__main__":
    # benchmarking
    t = 10**5  # number of tests
    time1, time2 = 0, 0
    for i in range(t):
        n = random.randrange(10**6, 10**12)

        start = time()
        r1 = reverse_number_1(n)
        time1 += time() - start

        start = time()
        r2 = reverse_number_2(n)
        time2 += time() - start

        assert r1 == r2

    print(f"time 1: {time1}")
    print(f"time 2: {time2}")
