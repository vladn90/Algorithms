""" Comparing two algorithms for finding factors of a number.
"""
import math
import random


def all_factors_1(n):
    """ Returns a list of all factors of n.
    Naive algorithm.
    Time complexity: O(n). Space complexity: O(1), output array is not
    included in the space complexity.
    """
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors


def all_factors_2(n):
    """ Returns a list of all factors of n.
    Improved algorithm.
    Time complexity: O(sqrt(n)). Space complexity: O(n), output array is not
    included in the space complexity.
    """
    factors = []  # factors from 1 to sqrt(n)
    inv_factors = []  # factors from n to sqrt(n)
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)
            inv_factors.append(n // i)
    # remove duplicate factor, which is sqrt(n)
    if sqrt_n ** 2 == n:
        factors.pop()

    # combine two factors arrays in sorted order
    m = len(inv_factors)
    for i in range(m - 1, -1, -1):
        factors.append(inv_factors[i])
    return factors


if __name__ == "__main__":
    # stress testing naive algorithm against improved algorithm
    while True:
        n = random.randrange(1, 10**6)
        res1 = all_factors_1(n)
        res2 = all_factors_2(n)
        if res1 == res2:
            print("OK")
            print(f"{res1}")
        else:
            print("Results are different.")
            print(f"initial number: {n}")
            print(f"naive algorithm result: {res1}")
            print(f"improved algorithm result: {res2}")
            break
