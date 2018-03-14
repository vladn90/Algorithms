""" Different algorithms to check if n is a power of 3.
"""
import random


def is_power_three_1(n):
    """ Returns True if n is a power of 3, False otherwise.
    Algorithm decription:
    1) Divide n by 3 while remainder == 0.
    2) If last n == 1, then n is a power of 3.
    Time complexity: O(lg(n)). Space complexity: O(1).
    """
    if n < 1:
        return False

    while n % 3 == 0:
        n //= 3
    return n == 1


def is_power_three_2(n):
    """ Returns True if n is a power of 3, False otherwise.
    Algorithm compares n with biggest n-power of 3 for Python.
    Time complexity: O(1). Space complexity: O(1).
    """
    if n < 1:
        return False
    return 3 ** 39 % n == 0


if __name__ == "__main__":
    # check all powers of 3 from 0 to 32
    for y in range(32):
        n = 3 ** y
        assert is_power_three_1(n) == is_power_three_2(n)

    # check random numbers, stress testing algorithms against each other
    while True:
        n = random.randrange(1, 10**18)
        if is_power_three_1(n) == is_power_three_2(n):
            print("OK")
            print(n)
        else:
            print("Results are different.")
            print(f"n = {n}")
            break
